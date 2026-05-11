#!/usr/bin/env python3
"""COGS Sentinel — executable economic gate for hplan.

Why this exists:
- Replit went from ~$2M ARR to $144M ARR while gross margin dropped to single
  digits before pricing changes lifted it back to 20-30%. The lesson is that
  AI SaaS COGS is a build blocker, not a finance afterthought.
- competitive-landscape doc identifies COGS as hplan's signature differentiator
  vs Superpowers/GStack/Spec-Kit. Words are not enough — hplan needs to
  *calculate* the margin envelope.

This module accepts a JSON or CLI input describing provider pricing + usage
patterns and emits:
- p50 / p90 / worst-case COGS per paid user / month
- gross margin scenarios at the configured ARPU
- free-user abuse breakeven multiplier
- decision: GREEN / CONDITIONAL_GO / RED

Pricing snapshots are intentionally kept in `references/provider_pricing.json`
so they can be updated without code changes. CLI overrides win over snapshot.
"""

from __future__ import annotations

import argparse
import json
import math
import statistics
from datetime import date
from pathlib import Path


PRICING_FALLBACK = {
    "anthropic": {
        "claude-opus-4-7": {"input_per_mtok": 15.0, "output_per_mtok": 75.0},
        "claude-sonnet-4-6": {"input_per_mtok": 3.0, "output_per_mtok": 15.0},
        "claude-haiku-4-5": {"input_per_mtok": 0.80, "output_per_mtok": 4.0},
    },
    "openai": {
        "gpt-5": {"input_per_mtok": 5.0, "output_per_mtok": 20.0},
        "gpt-5-mini": {"input_per_mtok": 0.25, "output_per_mtok": 1.5},
    },
    "google": {
        "gemini-2.5-pro": {"input_per_mtok": 1.25, "output_per_mtok": 10.0},
        "gemini-2.5-flash": {"input_per_mtok": 0.10, "output_per_mtok": 0.40},
    },
}


def load_pricing(skill_root: Path | None = None) -> dict:
    if skill_root is None:
        skill_root = Path(__file__).resolve().parent.parent
    snap = skill_root / "references" / "provider_pricing.json"
    if snap.exists():
        try:
            return json.loads(snap.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            pass
    return PRICING_FALLBACK


def cost_per_call(prices: dict, tokens_in: int, tokens_out: int) -> float:
    return (tokens_in / 1_000_000) * prices["input_per_mtok"] + (
        tokens_out / 1_000_000
    ) * prices["output_per_mtok"]


def lognormal_samples(median: float, p90: float, n: int = 1000, seed: int = 7) -> list[float]:
    """Approximate per-call cost spread with a lognormal distribution.

    Median and p90 anchor the shape. We use a deterministic seed so the sentinel
    output is reproducible across runs (no `random` module needed for that).
    """
    import random

    if median <= 0:
        return [0.0] * n
    if p90 <= median:
        p90 = median * 1.5
    mu = math.log(median)
    sigma = (math.log(p90) - mu) / 1.2816  # 90th percentile z-score
    rng = random.Random(seed)
    return [math.exp(rng.gauss(mu, sigma)) for _ in range(n)]


def run(params: dict) -> dict:
    pricing = params.get("pricing") or load_pricing()
    provider = params.get("provider", "anthropic")
    model = params.get("model", "claude-sonnet-4-6")
    try:
        prices = pricing[provider][model]
    except KeyError:
        raise SystemExit(f"unknown provider/model: {provider}/{model}")

    tokens_in = int(params.get("tokens_in", 4000))
    tokens_out = int(params.get("tokens_out", 1000))
    calls_per_user_month = float(params.get("calls_per_user_month", 60))
    arpu = float(params.get("arpu", 19))
    paid_conversion = float(params.get("paid_conversion", 0.05))
    free_abuse_multiplier = float(params.get("free_abuse_multiplier", 5))
    target_margin = float(params.get("target_gross_margin", 0.70))
    payment_fee_pct = float(params.get("payment_fee_pct", 0.03))

    median_call = cost_per_call(prices, tokens_in, tokens_out)
    p90_call = median_call * 2.2  # realistic variance for token-heavy calls
    samples = lognormal_samples(median_call, p90_call)
    samples.sort()

    def pct(values, p):
        idx = max(0, min(len(values) - 1, int(p * len(values))))
        return values[idx]

    cogs_p50 = pct(samples, 0.5) * calls_per_user_month
    cogs_p90 = pct(samples, 0.9) * calls_per_user_month
    cogs_worst = pct(samples, 0.99) * calls_per_user_month

    net_revenue = arpu * (1 - payment_fee_pct)
    margin_p50 = (net_revenue - cogs_p50) / net_revenue if net_revenue else -1
    margin_p90 = (net_revenue - cogs_p90) / net_revenue if net_revenue else -1

    free_user_cost = median_call * calls_per_user_month * free_abuse_multiplier
    free_load_per_paid = (1 - paid_conversion) / paid_conversion if paid_conversion > 0 else 999
    blended_cogs = cogs_p50 + free_user_cost * free_load_per_paid * 0.3  # 30% of free users active
    blended_margin = (net_revenue - blended_cogs) / net_revenue if net_revenue else -1

    if margin_p90 >= target_margin and blended_margin >= target_margin * 0.7:
        decision = "GREEN"
    elif margin_p50 >= target_margin * 0.6:
        decision = "CONDITIONAL_GO"
    else:
        decision = "RED"

    reasons = []
    if margin_p90 < target_margin:
        reasons.append(
            f"p90 gross margin {margin_p90:.0%} below target {target_margin:.0%} — tighten usage caps or downgrade model."
        )
    if blended_margin < target_margin * 0.7:
        reasons.append(
            f"free-user blended margin {blended_margin:.0%} too low — abuse cap or paywall first call."
        )
    if not reasons:
        reasons.append("All scenarios within target margin.")

    return {
        "generated": date.today().isoformat(),
        "provider": provider,
        "model": model,
        "inputs": {
            "tokens_in": tokens_in,
            "tokens_out": tokens_out,
            "calls_per_user_month": calls_per_user_month,
            "arpu": arpu,
            "paid_conversion": paid_conversion,
            "free_abuse_multiplier": free_abuse_multiplier,
            "target_gross_margin": target_margin,
        },
        "per_call_cost_usd": {
            "p50": round(median_call, 6),
            "p90": round(p90_call, 6),
        },
        "monthly_cogs_per_paid_user_usd": {
            "p50": round(cogs_p50, 4),
            "p90": round(cogs_p90, 4),
            "worst": round(cogs_worst, 4),
        },
        "gross_margin": {
            "p50": round(margin_p50, 4),
            "p90": round(margin_p90, 4),
            "with_free_user_load": round(blended_margin, 4),
        },
        "decision": decision,
        "reasons": reasons,
    }


def markdown_report(result: dict) -> str:
    lines = [
        f"# COGS Sentinel Report",
        "",
        f"Generated: {result['generated']}",
        f"Provider: {result['provider']} / {result['model']}",
        "",
        "## Decision",
        f"**{result['decision']}**",
        "",
        *[f"- {r}" for r in result["reasons"]],
        "",
        "## Per-Call Cost (USD)",
        f"- p50: ${result['per_call_cost_usd']['p50']}",
        f"- p90: ${result['per_call_cost_usd']['p90']}",
        "",
        "## Monthly COGS per Paid User (USD)",
        f"- p50: ${result['monthly_cogs_per_paid_user_usd']['p50']}",
        f"- p90: ${result['monthly_cogs_per_paid_user_usd']['p90']}",
        f"- worst: ${result['monthly_cogs_per_paid_user_usd']['worst']}",
        "",
        "## Gross Margin",
        f"- p50: {result['gross_margin']['p50']:.0%}",
        f"- p90: {result['gross_margin']['p90']:.0%}",
        f"- with free-user load: {result['gross_margin']['with_free_user_load']:.0%}",
        "",
        "## Inputs",
        *[f"- {k}: {v}" for k, v in result["inputs"].items()],
    ]
    return "\n".join(lines)


def parse_args():
    p = argparse.ArgumentParser(description="hplan COGS sentinel")
    p.add_argument("--params", help="Path to JSON params file (overrides CLI flags)")
    p.add_argument("--provider", default="anthropic")
    p.add_argument("--model", default="claude-sonnet-4-6")
    p.add_argument("--tokens-in", type=int, default=4000)
    p.add_argument("--tokens-out", type=int, default=1000)
    p.add_argument("--calls-per-user-month", type=float, default=60)
    p.add_argument("--arpu", type=float, default=19)
    p.add_argument("--paid-conversion", type=float, default=0.05)
    p.add_argument("--free-abuse-multiplier", type=float, default=5)
    p.add_argument("--target-gross-margin", type=float, default=0.70)
    p.add_argument("--payment-fee-pct", type=float, default=0.03)
    p.add_argument("--json", action="store_true")
    p.add_argument("--out", help="Write markdown report to path")
    return p.parse_args()


def main():
    args = parse_args()
    if args.params:
        params = json.loads(Path(args.params).read_text(encoding="utf-8"))
    else:
        params = {
            "provider": args.provider,
            "model": args.model,
            "tokens_in": args.tokens_in,
            "tokens_out": args.tokens_out,
            "calls_per_user_month": args.calls_per_user_month,
            "arpu": args.arpu,
            "paid_conversion": args.paid_conversion,
            "free_abuse_multiplier": args.free_abuse_multiplier,
            "target_gross_margin": args.target_gross_margin,
            "payment_fee_pct": args.payment_fee_pct,
        }
    result = run(params)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        report = markdown_report(result)
        print(report)
        if args.out:
            Path(args.out).write_text(report, encoding="utf-8")


if __name__ == "__main__":
    main()

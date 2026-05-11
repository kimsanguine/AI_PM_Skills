# troubleshooting — cogs-sentinel

## "decision is GREEN but blended margin is barely 49%"

- 정상 동작. target × 0.7 임계값 통과는 했지만 안전 마진은 작음.
- free-conversion이 가정보다 낮아지면 즉시 무너짐.
- Mitigation: abuse cap + paywall first heavy call.

## "Provider not in snapshot"

`references/provider_pricing.json`을 직접 갱신하거나 `--pricing my_prices.json` 으로 오버라이드:

```json
{
  "anthropic": {"claude-sonnet-4-6": {"input_per_mtok": 3.0, "output_per_mtok": 15.0}}
}
```

## "p90 너무 보수적이라고 느낌"

기본 multiplier는 `p90_call = median × 2.2`. 사용자 트래픽이 더 균질하면 multiplier 1.5로 sampler 호출:

```python
from hplan.scripts.cogs_sentinel import run
result = run({..., "p90_multiplier": 1.5})
```

(현재 CLI 노출 안 됨 — 필요 시 PR)

## "Numbers look fine but the product flops"

cogs-sentinel은 *지속 가능성*만 본다. 제품 자체의 가치 — `evidence-rubric` 영역. COGS GREEN ≠ build.

## "p90 multiplier 어디서 나옴?"

lognormal 표준편차 추정에서 `sigma = (ln(p90) - ln(median)) / 1.2816` — 90th percentile z-score. 2.2 multiplier는 reasonable variance assumption. 사용자 환경에서는 실측해서 보정 권장.

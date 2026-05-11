#!/usr/bin/env python3
import argparse
import json
import os
import tempfile
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "hplan-matplotlib"))
os.environ.setdefault("MPLBACKEND", "Agg")

import matplotlib

matplotlib.use("Agg", force=True)
import matplotlib.pyplot as plt

from generate_report import generate


DECISION_BANDS = [
    ("Hold", 0, 35, "#5b5349"),
    ("Pivot", 35, 55, "#c95032"),
    ("Interview", 55, 75, "#f8d36b"),
    ("Build", 75, 100, "#2f6f73"),
]


def plot_report(report, output):
    items = report["score_breakdown"]
    labels = [item["label"] for item in items]
    scores = [item["score"] for item in items]
    max_scores = [item["max"] for item in items]
    score = report["score"]

    fig = plt.figure(figsize=(13, 7.5), facecolor="#f4efe6")
    grid = fig.add_gridspec(2, 1, height_ratios=[1, 3], hspace=0.36)

    ax_gauge = fig.add_subplot(grid[0])
    ax_gauge.set_facecolor("#fffaf0")
    for label, start, end, color in DECISION_BANDS:
        ax_gauge.barh([0], [end - start], left=[start], color=color, edgecolor="#221f1a", height=0.5)
        ax_gauge.text((start + end) / 2, 0, label, ha="center", va="center", fontsize=10, weight="bold")
    ax_gauge.axvline(score, color="#221f1a", linewidth=3)
    ax_gauge.text(score, 0.48, f"{score}/100", ha="center", va="bottom", fontsize=14, weight="bold")
    ax_gauge.set_xlim(0, 100)
    ax_gauge.set_yticks([])
    ax_gauge.set_title("Harness Planning Decision Threshold", loc="left", fontsize=16, weight="bold")
    ax_gauge.spines[["top", "right", "left"]].set_visible(False)

    ax_bar = fig.add_subplot(grid[1])
    ax_bar.set_facecolor("#fffaf0")
    y_positions = range(len(labels))
    ax_bar.barh(y_positions, max_scores, color="#ded3bf", edgecolor="#221f1a")
    ax_bar.barh(y_positions, scores, color="#2f6f73", edgecolor="#221f1a")
    ax_bar.set_yticks(list(y_positions), labels)
    ax_bar.invert_yaxis()
    ax_bar.set_xlim(0, max(max_scores) + 3)
    ax_bar.set_xlabel("Score contribution")
    ax_bar.set_title("Rubric Breakdown", loc="left", fontsize=16, weight="bold")
    for y, value, max_value in zip(y_positions, scores, max_scores):
        ax_bar.text(max_value + 0.4, y, f"{value}/{max_value}", va="center", fontsize=10, weight="bold")
    ax_bar.spines[["top", "right"]].set_visible(False)

    fig.suptitle(
        f"hplan Quantitative Diagnosis - {report['decision'].upper()}",
        x=0.02,
        y=0.99,
        ha="left",
        fontsize=18,
        weight="bold",
    )
    fig.text(0.02, 0.02, "Generated with matplotlib from hplan score_breakdown.", fontsize=9, color="#5b5349")
    fig.savefig(output, dpi=180, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser(description="Generate a matplotlib PNG chart for a Harness Planning diagnosis.")
    parser.add_argument("input", help="Path to JSON input")
    parser.add_argument("-o", "--output", default="hplan-analysis-chart.png", help="Output PNG path")
    args = parser.parse_args()

    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    report = generate(data)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    plot_report(report, output)
    print(output)


if __name__ == "__main__":
    main()

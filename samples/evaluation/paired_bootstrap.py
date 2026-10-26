# Standalone paired model evaluation tool.
import argparse
import json
from pathlib import Path

import numpy as np

def iter_jsonl(path):
    """Yield JSON-object records from a UTF-8 JSONL file."""
    with Path(path).open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if line.strip():
                record = json.loads(line)
                if not isinstance(record, dict) or "id" not in record:
                    raise ValueError(f"Expected a record with an id at line {line_number}")
                yield record


def write_json(path, payload):
    """Write a reproducible evaluation report."""
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")



def parse_args():
    parser = argparse.ArgumentParser(description="Paired comparison with bootstrap confidence interval.")
    parser.add_argument("--baseline", required=True)
    parser.add_argument("--candidate", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--samples", type=int, default=10000)
    parser.add_argument("--seed", type=int, default=2026)
    parser.add_argument("--confidence", type=float, default=0.95)
    parser.add_argument("--allow-partial", action="store_true")
    return parser.parse_args()


def latest_success(path):
    rows = {}
    for row in iter_jsonl(path):
        if not row.get("error"):
            rows[str(row["id"])] = row
    return rows


def main():
    args = parse_args()
    baseline = latest_success(args.baseline)
    candidate = latest_success(args.candidate)
    if args.samples <= 0 or not 0 < args.confidence < 1:
        raise ValueError("--samples must be positive and --confidence must be between 0 and 1")
    if not args.allow_partial and set(baseline) != set(candidate):
        raise RuntimeError(
            f"Prediction ID sets differ: baseline={len(baseline)}, candidate={len(candidate)}; "
            "complete both runs or pass --allow-partial"
        )
    ids = sorted(set(baseline) & set(candidate))
    if not ids:
        raise RuntimeError("No paired successful predictions")
    base = np.asarray([bool(baseline[key]["correct"]) for key in ids], dtype=np.float64)
    cand = np.asarray([bool(candidate[key]["correct"]) for key in ids], dtype=np.float64)
    delta = cand - base
    rng = np.random.default_rng(args.seed)
    bootstrap = np.empty(args.samples, dtype=np.float64)
    for start in range(0, args.samples, 1000):
        batch = min(1000, args.samples - start)
        indices = rng.integers(0, len(ids), size=(batch, len(ids)))
        bootstrap[start : start + batch] = delta[indices].mean(axis=1)
    alpha = (1.0 - args.confidence) / 2.0
    report = {
        "baseline": args.baseline,
        "candidate": args.candidate,
        "paired_samples": len(ids),
        "baseline_conditions": sorted({str(baseline[key].get("condition")) for key in ids}),
        "candidate_conditions": sorted({str(candidate[key].get("condition")) for key in ids}),
        "baseline_correct": int(base.sum()),
        "candidate_correct": int(cand.sum()),
        "baseline_accuracy": float(base.mean()),
        "candidate_accuracy": float(cand.mean()),
        "accuracy_delta": float(delta.mean()),
        "correct_to_incorrect": int(np.sum((base == 1) & (cand == 0))),
        "incorrect_to_correct": int(np.sum((base == 0) & (cand == 1))),
        "bootstrap_samples": args.samples,
        "confidence": args.confidence,
        "bootstrap_ci": [float(np.quantile(bootstrap, alpha)), float(np.quantile(bootstrap, 1 - alpha))],
        "seed": args.seed,
    }
    write_json(args.output, report)
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

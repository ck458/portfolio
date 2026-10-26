"""Quick regression checks for selected portfolio modules."""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "samples" / "novel-engine"))
from workspace_paths import WorkspacePaths
from io_utils import write_json_atomic, write_text_atomic


class WorkspaceAndAtomicTests(unittest.TestCase):
    def test_workspace_path_boundary(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = WorkspacePaths(tmp)
            expected = Path(tmp).resolve() / "runs" / "manifest.json"
            self.assertEqual(paths.path("runs", "manifest.json"), expected)
            with self.assertRaises(ValueError):
                paths.path("..", "outside.json")
            with self.assertRaises(ValueError):
                paths.path("/tmp/outside.json")

    def test_atomic_write_json_and_text(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "artifact.json"
            write_json_atomic(target, {"step": "completed"}, overwrite=False)
            self.assertEqual(json.loads(target.read_text(encoding="utf-8")), {"step": "completed"})
            with self.assertRaises(FileExistsError):
                write_text_atomic(target, "another payload", overwrite=False)
            write_text_atomic(target, "updated", overwrite=True)
            self.assertEqual(target.read_text(encoding="utf-8"), "updated")

    def test_paired_bootstrap_cli(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp)
            baseline = path / "baseline.jsonl"
            candidate = path / "candidate.jsonl"
            baseline.write_text("".join(json.dumps({"id": str(i), "correct": i % 2 == 0}) + "\n" for i in range(12)), encoding="utf-8")
            candidate.write_text("".join(json.dumps({"id": str(i), "correct": i % 3 != 1}) + "\n" for i in range(12)), encoding="utf-8")
            report = path / "paired.json"
            subprocess.run([sys.executable, str(ROOT / "samples" / "evaluation" / "paired_bootstrap.py"),
                            "--baseline", str(baseline), "--candidate", str(candidate),
                            "--output", str(report), "--samples", "500", "--seed", "11"], check=True, capture_output=True)
            payload = json.loads(report.read_text(encoding="utf-8"))
            self.assertEqual(payload["paired_samples"], 12)
            self.assertAlmostEqual(payload["baseline_accuracy"], 0.5)
            self.assertEqual(len(payload["bootstrap_ci"]), 2)
            self.assertLessEqual(payload["bootstrap_ci"][0], payload["bootstrap_ci"][1])


if __name__ == "__main__":
    unittest.main()

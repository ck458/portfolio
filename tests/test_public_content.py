"""Check the intended public artifact for contact details and infrastructure identifiers."""
from __future__ import annotations
import re
import subprocess
from pathlib import Path
from urllib.parse import urlparse
import unittest

ROOT = Path(__file__).resolve().parents[1]
CLOUD_NAMES = ["ver" + "cel", "supa" + "base"]
PERSONAL_NAMES = ["蔡" + "雨轩", "Cai " + "Yuxuan", "Yuxuan " + "Cai", "cai" + "yuxuan"]
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
PHONE_RE = re.compile(r"(?<!\d)1[3-9]\d{9}(?!\d)")
SECRET_RE = re.compile(r"(?:sk-[A-Za-z0-9_-]{20,}|AKIA[A-Z0-9]{16}|-----BEGIN [A-Z ]+PRIVATE KEY-----)")
DB_URL_RE = re.compile(r"(?:postgres(?:ql)?|mongodb|redis)://", re.I)
REMOTE_URL_RE = re.compile(r"https?://[^\s\"'<>)]+")

def tracked():
    data = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT)
    return [ROOT / item.decode("utf-8") for item in data.split(b"\0") if item]

class PublicPortfolioTests(unittest.TestCase):
    def test_public_sources_avoid_identifiers(self):
        problems = []
        for path in tracked():
            if path.suffix not in {".md", ".py", ".ts", ".html", ".svg", ".yml", ".yaml", ".txt"}:
                continue
            data = path.read_text(encoding="utf-8")
            for term in CLOUD_NAMES + PERSONAL_NAMES:
                if term.casefold() in data.casefold():
                    problems.append((str(path.relative_to(ROOT)), "restricted identifier"))
            for pattern in (EMAIL_RE, PHONE_RE, SECRET_RE, DB_URL_RE):
                if pattern.search(data):
                    problems.append((str(path.relative_to(ROOT)), "private data pattern"))
            if path.suffix in {".md", ".html"}:
                for match in REMOTE_URL_RE.finditer(data):
                    if urlparse(match.group()).hostname != "github.com":
                        problems.append((str(path.relative_to(ROOT)), "non-portfolio endpoint"))
        self.assertEqual(problems, [])

    def test_local_markdown_links(self):
        missing = []
        for path in tracked():
            if path.suffix != ".md":
                continue
            data = path.read_text(encoding="utf-8")
            for raw in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", data):
                if raw.startswith(("https:", "http:", "#")):
                    continue
                relative = raw.split("#", 1)[0]
                if relative and not (path.parent / relative).resolve().exists():
                    missing.append((str(path.relative_to(ROOT)), relative))
        self.assertEqual(missing, [])

    def test_static_page_has_mobile_viewport(self):
        html = (ROOT / "docs" / "index.html").read_text(encoding="utf-8")
        self.assertIn("name=\"viewport\"", html)
        self.assertIn("@ck458", html)
        self.assertNotIn("<script", html)

if __name__ == "__main__":
    unittest.main()

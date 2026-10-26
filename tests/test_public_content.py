"""Checks for accidentally disclosed account, runtime, and infrastructure details."""
from __future__ import annotations

from hashlib import sha256
from html.parser import HTMLParser
from pathlib import Path
import ipaddress
import re
import subprocess
import unittest
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]

# Fingerprints of restricted display names and provider identifiers.
# Keeping their original text out of this public policy file avoids publishing them here.
RESTRICTED_FINGERPRINTS = {
    3: {"e1273972001e63c6e25af0eae8d3916ae4e1b235312df7bfcfc42424f2622428"},
    6: {"9d3508a8484ee2520ca5fe0e52eab835774efa3fe533267e914eb00ad78d2579"},
    8: {"4d7594e57f7d03f35ede2d316cda4cdb7df66b28963738e836a2f16d9fc9eb4d"},
    9: {"c00ef117ed989d6713a1a9580dd5bee21124e554e0ef849678c8c8011b8cc1c7"},
    10: {"a4a643d5b2beb5437e4fe20aa895f9ace9c305d8ce3f8078eb77432c15a0429b",
         "9a8690c77d0a7c6d01dc345d34d151b925f71a8b8c2e30e9867e694ea8fc2b4c"},
}
EMAIL = re.compile(r"(?i)(?<![\w@])[\w.%+\-]+@[\w.\-]+\.[A-Za-z]{2,}")
PHONE = re.compile(r"(?<!\d)1[3-9]\d{9}(?!\d)")
SECRETS = re.compile(
    r"(?i)(?:ghp_[0-9A-Za-z]{20,}|github_pat_[0-9A-Za-z_]{25,}|"
    r"sk-[0-9A-Za-z_\-]{20,}|hf_[0-9A-Za-z]{20,}|"
    r"AKIA[0-9A-Z]{16}|AIza[0-9A-Za-z_\-]{25,}|"
    r"-----BEGIN [A-Z ]*PRIVATE KEY-----)"
)
CONNECTION = re.compile(r"(?i)(?:postgres(?:ql)?|mongodb(?:\+srv)?|redis)://")
LOCAL_PATH = re.compile(r"(?i)(?:[A-Z]:[\\/](?:Users|Games|Documents)[\\/]|/home/(?!runner/work/)[\w-]+/|/Users/[\w-]+/)")
URL = re.compile(r"https?://[^\s\"'<>),;\]]+")
SCANNED_EXTENSIONS = {".md", ".py", ".ts", ".mjs", ".html", ".svg", ".yaml", ".yml", ".txt"}
APPROVED_HOSTS = {"github.com"}
SVG_NAMESPACE_HOST = "www.w3.org"


def tracked_files():
    output = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT)
    return [ROOT / part.decode("utf-8") for part in output.split(b"\0") if part]


def restricted_name_present(text):
    lowered = text.casefold()
    for length, digests in RESTRICTED_FINGERPRINTS.items():
        for offset in range(len(lowered) - length + 1):
            fragment = lowered[offset:offset + length]
            if sha256(fragment.encode("utf-8")).hexdigest() in digests:
                return True
    return False


class AnchorParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []
        self.srcs = []
        self.has_viewport = False
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a" and attrs.get("href"):
            self.hrefs.append(attrs["href"])
        if tag == "img" and attrs.get("src"):
            self.srcs.append(attrs["src"])
        if tag == "meta" and attrs.get("name") == "viewport":
            self.has_viewport = True


class PublicContentChecks(unittest.TestCase):
    def test_no_identity_contact_secrets_or_infrastructure(self):
        problems = []
        for path in tracked_files():
            if path.suffix not in SCANNED_EXTENSIONS:
                continue
            text = path.read_text(encoding="utf-8")
            rel = str(path.relative_to(ROOT))
            if restricted_name_present(text):
                problems.append((rel, "identifier"))
            for pattern, kind in ((EMAIL, "email"), (PHONE, "phone"),
                                  (SECRETS, "credential"), (CONNECTION, "connection"),
                                  (LOCAL_PATH, "local path")):
                if pattern.search(text):
                    problems.append((rel, kind))
            for item in URL.finditer(text):
                host = urlparse(item.group(0)).hostname
                if host not in APPROVED_HOSTS and not (path.suffix == ".svg" and host == SVG_NAMESPACE_HOST):
                    problems.append((rel, "external host"))
        self.assertEqual(problems, [])

    def test_internal_markdown_links(self):
        missing = []
        for path in tracked_files():
            if path.suffix != ".md":
                continue
            for url in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
                if url.startswith(("https:", "http:", "#")):
                    continue
                relative = url.split("#", 1)[0]
                if relative and not (path.parent / relative).resolve().is_file():
                    missing.append((str(path.relative_to(ROOT)), relative))
        self.assertEqual(missing, [])

    def test_static_showcase_navigation(self):
        page = (ROOT / "docs" / "index.html").read_text(encoding="utf-8")
        parser = AnchorParser()
        parser.feed(page)
        self.assertTrue(parser.has_viewport)
        self.assertGreaterEqual(len(parser.hrefs), 6)
        self.assertIn("ck458", page)
        self.assertNotIn("<script", page.casefold())
        for item in parser.hrefs + parser.srcs:
            self.assertEqual(urlparse(item).hostname, "github.com")
            if "/portfolio/blob/main/" in item:
                relative = item.split("/portfolio/blob/main/", 1)[1]
                self.assertTrue((ROOT / relative).is_file(), item)


if __name__ == "__main__":
    unittest.main()

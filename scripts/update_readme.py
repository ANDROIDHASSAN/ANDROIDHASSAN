"""Fill the "Recently pushed" block of the profile README from real public repos.

Runs in GitHub Actions (see .github/workflows/update-readme.yml). Standard library only.
Lists the 5 most recently pushed public, non-fork, non-archived repos that have a real
description (skipping this profile repo), and rewrites the text between the README markers.
"""

import json
import os
import re
import textwrap
import urllib.request
from pathlib import Path

USER = os.environ.get("GH_USER", "ANDROIDHASSAN")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
README = Path(__file__).resolve().parent.parent / "README.md"
START, END = "<!-- recent_pushes starts -->", "<!-- recent_pushes ends -->"
MIN_DESC = 25


def fetch_repos():
    url = f"https://api.github.com/users/{USER}/repos?sort=pushed&per_page=30&type=owner"
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def build_lines(repos):
    lines = []
    for repo in repos:
        if repo.get("fork") or repo.get("private") or repo.get("archived") or repo["name"].lower() == USER.lower():
            continue
        desc = " ".join((repo.get("description") or "").split())
        # Throwaway repos ("Test", ":)", "yo") have no real description; a repo shows up once it gets one.
        if len(desc) < MIN_DESC:
            continue
        desc = textwrap.shorten(desc, 80, placeholder="…")
        date = repo["pushed_at"][:10]
        lines.append(f"- [{repo['name']}]({repo['html_url']}) — {desc} · {date}")
        if len(lines) == 5:
            break
    return lines or ["_Updates automatically every day from my public repos._"]


def main():
    text = README.read_text(encoding="utf-8")
    block = "\n".join(build_lines(fetch_repos()))
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    new_text = pattern.sub(f"{START}\n{block}\n{END}", text)
    if new_text != text:
        README.write_text(new_text, encoding="utf-8")
        print("README updated")
    else:
        print("No change")


if __name__ == "__main__":
    main()

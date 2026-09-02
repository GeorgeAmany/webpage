#!/usr/bin/env python3
"""Count GeorgeAmany commits across flagship GitHub repos (via local clones)."""

import json
import subprocess
from pathlib import Path
from typing import Optional

ROOT = Path("/Volumes/George_SSD/Work/projects")
OUT = Path(__file__).resolve().parent / "commit_stats.json"

FLAGSHIP = [
    "Fuse-mobile",
    "taleem_student",
    "taleem_employees",
    "noor-mobile",
    "zahran-mobile",
    "zahran_desktop",
    "schupply_mobile",
    "binge-app",
    "Alwefaq-Foods-Mobile-App-Webview",
    "horse_time_user",
    "proposal_desktop",
    "animated_contact_us",
    "liquid_wave_indicator",
]


def is_george(author: str, email: str) -> bool:
    author = author.strip().lower()
    email = email.strip().lower()
    return author in {"georgeamany", "george amany"} or "georgeamany" in email


def count_repo(repo: Path) -> Optional[int]:
    if not (repo / ".git").exists():
        return None
    log = subprocess.check_output(
        ["git", "-C", str(repo), "log", "--all", "--format=%an|%ae"],
        text=True,
    )
    return sum(
        1 for line in log.splitlines() if line and is_george(*line.split("|", 1))
    )


def main():
    rows = []
    total = 0
    for name in FLAGSHIP:
        repo = ROOT / name
        count = count_repo(repo)
        if count is None:
            continue
        rows.append({"project": name, "commits": count})
        total += count

    payload = {"author": "GeorgeAmany", "total": total, "projects": rows}
    OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    print(f"\nSaved: {OUT}")


if __name__ == "__main__":
    main()

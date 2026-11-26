#!/usr/bin/env python3
"""The Absurd Clause Contest — variant A (Section 14.3, the left sock).

Writes the entry clause to /output/entry.txt first, then optionally mirrors
it to the repo root (guarded so a read-only repo never crashes the run).
Deterministic: the same text on every run. The entry is one sentence of
199 chars (gate: 1-200 chars), enforced by a length check before writing.
"""

import os
import shutil

ENTRY = (
    "Section 14.3: notwithstanding anything herein, the User agrees that, "
    "upon acceptance, the User's left sock, hereinafter 'the Sock', "
    "becomes the property of the Company, wherever said Sock may reside."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(ENTRY)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Optional mirror to the repo root — never fatal on a read-only repo.
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        shutil.copy("/output/entry.txt", os.path.join(here, "entry.txt"))
    except Exception:
        pass


if __name__ == "__main__":
    main()

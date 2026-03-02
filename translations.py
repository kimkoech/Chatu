"""English <-> Swahili translations parser."""

from __future__ import annotations

import csv


def gen_map(trans_csv_file: str):
    """Read translation CSV and return (swa_to_eng, eng_to_swa)."""
    swa_to_eng = {}
    eng_to_swa = {}

    with open(trans_csv_file, newline="", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if not row:
                continue

            first_cell = row[0].strip() if row[0] else ""
            if not first_cell or first_cell.startswith("#") or first_cell.startswith("//"):
                continue

            if len(row) < 2:
                continue

            english = row[0].strip()
            swahili = row[1].strip()
            if not english or not swahili:
                continue

            swa_to_eng[swahili] = english
            eng_to_swa[english] = swahili

    return (swa_to_eng, eng_to_swa)

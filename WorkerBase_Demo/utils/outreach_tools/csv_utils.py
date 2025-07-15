import csv
import os

def read_leads_csv(filepath: str) -> list:
    with open(filepath, mode="r", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def write_enriched_leads_csv(rows: list, filepath: str) -> None:
    if not rows:
        print("⚠️ No leads to write.")
        return

    fieldnames = list(rows[0].keys())
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

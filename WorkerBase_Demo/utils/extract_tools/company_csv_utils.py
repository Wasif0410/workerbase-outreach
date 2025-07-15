import csv

def read_top_competitor_companies(csv_path: str, top_n: int = 3) -> list:
    companies = []
    with open(csv_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            is_competitor = row.get("is_competitor", "").strip().lower()
            if is_competitor == "true":
                companies.append({
                    "name": row["name"].strip(),
                    "url": row["linkedin"].strip(),
                    "reason": row.get("ai_reason", "").strip()
                })
    return companies[:top_n]

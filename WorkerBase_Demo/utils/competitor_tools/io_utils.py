import csv
import os

def save_to_csv(leads, filename):
    """Append new leads to CSV, avoiding duplicates by LinkedIn URL (case-insensitive)."""
    # Read existing leads
    existing_links = set()
    if os.path.exists(filename):
        with open(filename, mode="r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                link = row.get("linkedin")
                if link:
                    existing_links.add(link.strip().lower())
    # Filter out duplicates (case-insensitive)
    new_leads = [lead for lead in leads if lead.get("linkedin") and lead.get("linkedin").strip().lower() not in existing_links]
    # Append new leads
    with open(filename, mode="a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "linkedin", "is_competitor", "ai_reason"])
        if f.tell() == 0:
            writer.writeheader()
        for lead in new_leads:
            writer.writerow({
                "name": lead.get("name", ""),
                "linkedin": lead.get("linkedin", ""),
                "is_competitor": lead.get("is_competitor", ""),
                "ai_reason": lead.get("ai_reason", "")
            })

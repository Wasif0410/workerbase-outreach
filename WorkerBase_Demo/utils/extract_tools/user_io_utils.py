import os
import csv

def save_user_leads_to_csv(data: list, output_path: str):
    if not data:
        print("⚠️ No data to save.")
        return

    # Ensure output is saved under 'data' folder
    if not output_path.startswith("data/") and not output_path.startswith("data\\"):
        output_path = os.path.join("data", output_path)

    dir_name = os.path.dirname(output_path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)

    # Only keep specified fields
    fieldnames = [
        "name",
        "headline",
        "profileUrl",
        "reactionType",
        "post_url",
    ]
    filtered_data = [{k: entry.get(k, "") for k in fieldnames} for entry in data]

    with open(output_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(filtered_data)

    print(f"📁 Saved {len(filtered_data)} rows to {output_path}")

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../utils/outreach_tools')))
from utils.outreach_tools.gpt_utils import analyze_lead_fit
from utils.outreach_tools.csv_utils import read_leads_csv, write_enriched_leads_csv

def generate_outreach_messages(input_csv="data/linkedin_engagers.csv", output_csv="data/enriched_outreach_leads.csv", limit=10):
    """
    Generate outreach messages for leads and save to CSV.
    Only process the first `limit` users.
    """
    print(f"📥 Loading leads from: {input_csv}")
    leads = read_leads_csv(input_csv)[:limit]
    enriched_leads = []
    for lead in leads:
        name = lead.get("name", "")
        headline = lead.get("headline", "")
        profileUrl = lead.get("profileUrl", "")
        reactionType = lead.get("reactionType", "")
        post_url = lead.get("post_url", "")
        score, message = analyze_lead_fit(headline, name)
        enriched_leads.append({
            "name": name,
            "headline": headline,
            "profileUrl": profileUrl,
            "reactionType": reactionType,
            "post_url": post_url,
            "score": score,
            "outreach_message": message
        })
    print(f"📤 Writing enriched leads to: {output_csv}")
    write_enriched_leads_csv(enriched_leads, output_csv)
    print(f"✅ Outreach messages generated for {len(enriched_leads)} leads.")

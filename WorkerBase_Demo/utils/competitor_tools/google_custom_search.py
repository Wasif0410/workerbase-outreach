import os
import requests
from dotenv import load_dotenv

load_dotenv()

def run_google_custom_search(query: str) -> list:
    """Run Google Custom Search to find LinkedIn companies."""
    api_key = os.getenv("GOOGLE_SEARCH_API_KEY")
    cx = os.getenv("GOOGLE_SEARCH_ENGINE_ID")  # Programmable Search CX

    params = {
        "key": api_key,
        "cx": cx,
        "q": query,
        "num": 10
    }

    response = requests.get("https://www.googleapis.com/customsearch/v1", params=params)
    results = response.json()

    companies = [
        {
            "name": item.get("title", "").replace(" | LinkedIn", "").replace(" - LinkedIn", "").strip(),
            "linkedin": item.get("link", ""),
            "snippet": item.get("snippet", "")
        }
        for item in results.get("items", [])
        if "linkedin.com/company" in item.get("link", "")
    ]
    print(f"Google Custom Search found {len(companies)} LinkedIn companies for query: '{query}'")
    for company in companies:
        print(f"  - {company['name']} ({company['linkedin']})")
        print(f"    Snippet: {company['snippet']}")
    return companies

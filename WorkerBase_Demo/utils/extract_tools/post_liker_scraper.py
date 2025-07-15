import os
import json
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

def get_likers_from_post(post_url: str) -> list:
    api_token = os.getenv("APIFY_API_TOKEN")
    cookie_path = os.getenv("LINKEDIN_COOKIES_PATH")  # Path to JSON file
    if not cookie_path or not os.path.exists(cookie_path):
        raise FileNotFoundError("❌ linkedin_cookies.json not found or path not set in .env")

    with open(cookie_path, "r", encoding="utf-8") as f:
        cookies = json.load(f)

    client = ApifyClient(api_token)

    run_input = {
        "postUrl": post_url,
        "cookie": cookies,  # ✅ Use full array from file
        "startPage": 1,
        "minDelay": 2,
        "maxDelay": 5,
        "proxy": {
            "useApifyProxy": True,
            "apifyProxyCountry": "US"
        }
    }

    print(f"🔍 Scraping likers from: {post_url}")
    run = client.actor("GG8X5a2rlhcAT6Yo9").call(run_input=run_input)

    dataset_id = run["defaultDatasetId"]
    likers = list(client.dataset(dataset_id).iterate_items())

    print(f"✅ {len(likers)} likers extracted.")
    return likers

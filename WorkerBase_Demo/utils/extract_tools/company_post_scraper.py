import os
import json
from apify_client import ApifyClient
from dotenv import load_dotenv
load_dotenv()

# Load Apify API token from environment
APIFY_API_TOKEN = os.getenv("APIFY_API_TOKEN")
COOKIES_PATH = "linkedin_cookies.json"

def load_linkedin_cookies():
    print(f"🍪 Using cookies from: {COOKIES_PATH}")
    with open(COOKIES_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def get_post_urls_from_company(company_url: str, days_since_post: int = 35) -> list:
    print(f"🏢 Scraping posts from company: {company_url}")
    client = ApifyClient(APIFY_API_TOKEN)
    cookies = load_linkedin_cookies()

    run_input = {
        "url": company_url,
        "days_since_post": days_since_post,
        "cookies": cookies,
        "proxyConfiguration": { "useApifyProxy": True }
    }

    run = client.actor("enTKhWfYF38MorGwY").call(run_input=run_input)

    dataset_items = list(client.dataset(run["defaultDatasetId"]).iterate_items())
    if not dataset_items:
        print("⚠️ No posts found.")
        return []

    # Sort posts by timestamp descending (most recent first)
    sorted_posts = sorted(dataset_items, key=lambda x: x.get("timestamp", 0), reverse=True)

    # Only keep the most recent one
    most_recent_post = sorted_posts[0]
    return [most_recent_post.get("url")] if most_recent_post.get("url") else []

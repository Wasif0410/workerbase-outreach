from collections import defaultdict
from utils.extract_tools.company_csv_utils import read_top_competitor_companies
from utils.extract_tools.company_post_scraper import get_post_urls_from_company
from utils.extract_tools.post_liker_scraper import get_likers_from_post
from utils.extract_tools.user_io_utils import save_user_leads_to_csv

def extract_engaged_users(csv_path="data/competitors.csv", output_csv="data/linkedin_engagers.csv") -> None:
    company_data = defaultdict(lambda: {"company_url": "", "posts": []})
    all_likers = []

    print(f"📥 Reading top competitor companies from: {csv_path}")
    top_companies = read_top_competitor_companies(csv_path)

    for company in top_companies:
        name = company["name"]
        url = company["url"]
        print(f"\n🏢 Processing: {name}")
        company_data[name]["company_url"] = url
        company_data[name]["ai_reason"] = company["reason"]

        post_urls = get_post_urls_from_company(url)
        print(f"📝 {len(post_urls)} posts found for {name}")

        # Only process the most recent post
        if post_urls:
            recent_post = post_urls[0]
            print(f"🔗 Scraping likers from post: {recent_post}")
            likers = get_likers_from_post(recent_post)

            for liker in likers:
                liker["post_url"] = recent_post
                liker["ai_reason"] = company["reason"]
                # Remove source_company, keep only name, headline, profileUrl, reactionType, post_url
                liker.pop("source_company", None)

            company_data[name]["posts"].append({
                "post_url": recent_post,
                "likers": likers
            })

            all_likers.extend(likers)

    print(f"\n📊 Total engaged profiles collected: {len(all_likers)}")
    save_user_leads_to_csv(all_likers, output_path=output_csv)

    return company_data

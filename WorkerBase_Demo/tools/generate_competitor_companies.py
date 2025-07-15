import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../utils/competitor_tools')))

from utils.competitor_tools.query_generator import generate_linkedin_search_queries
from utils.competitor_tools.google_custom_search import run_google_custom_search
from utils.competitor_tools.company_evaluator import evaluate_company_fit
from utils.competitor_tools.io_utils import save_to_csv

from langchain.tools import tool

@tool
def discover_competitors(company_description: str) -> list:
    """
    Discover potential competitors to Workerbase by:
    1. Generating LinkedIn search queries
    2. Using Google Custom Search to find companies
    3. Scoring them via GPT
    4. Saving valid competitors to CSV
    """
    all_results = []
    queries = generate_linkedin_search_queries(company_description)
    
    for query in queries:
        raw_companies = run_google_custom_search(query)
        for company in raw_companies:
            result = evaluate_company_fit(company, company_description)
            if result["is_competitor"]:
                print(f"ChatGPT says: {result['ai_reason']}")
                all_results.append(result)
    
    save_to_csv(all_results, "data/competitors.csv")
    return all_results

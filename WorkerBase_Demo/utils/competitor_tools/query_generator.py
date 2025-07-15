from langchain_community.chat_models import ChatOpenAI

def generate_linkedin_search_queries(company_description: str) -> list:
    """Generate optimized Google search queries to discover competitors on LinkedIn."""
    llm = ChatOpenAI()
    prompt = f"""
    Based on the following company description, generate 3 Google search queries to find competitors on LinkedIn.

    Description: {company_description}

    Format each query like: site:linkedin.com/company keyword 1 keyword 2
    """
    response = llm.invoke(prompt)
    response_text = getattr(response, 'content', str(response))
    return [line.strip("- ").strip() for line in response_text.split("\n") if "linkedin.com/company" in line]

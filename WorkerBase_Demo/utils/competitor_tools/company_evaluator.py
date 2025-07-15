from langchain_community.chat_models import ChatOpenAI

def evaluate_company_fit(candidate: dict, target_description: str) -> dict:
    """Use GPT to determine if a company is a competitor to Workerbase."""
    llm = ChatOpenAI()
    prompt = f"""
    Workerbase description: {target_description}

    Company: {candidate['name']}
    Snippet: {candidate['snippet']}

    Is this company a competitor to Workerbase? Answer YES or NO and explain briefly.
    """
    response = llm.invoke(prompt)
    response_text = getattr(response, 'content', str(response))
    is_competitor = "yes" in response_text.lower()
    return {
        "name": candidate.get("name"),
        "linkedin": candidate.get("linkedin"),
        "is_competitor": is_competitor,
        "ai_reason": response_text
    }

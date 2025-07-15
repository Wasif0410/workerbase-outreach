import os
import openai
from typing import Tuple

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_lead_fit(headline: str, name: str) -> Tuple[int, str]:
    prompt = f"""
You are a lead qualification expert for Workerbase, an IIoT platform for smart manufacturing.

Create a personalized LinkedIn outreach message for the following lead. Use their name and headline to tailor the message and highlight how Workerbase can help them in their role or industry. Keep the message under 300 characters and make it relevant to their background.

Lead Name: {name}
Headline: {headline}

Respond in the format:
Score: <1–10>
Message: <custom LinkedIn message under 300 characters>
    """.strip()

    try:
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        content = response.choices[0].message.content.strip()
        score = None
        message = None
        for line in content.splitlines():
            if line.lower().startswith("score"):
                try:
                    score = int(line.split(":", 1)[1].strip().split()[0])
                except Exception:
                    score = 0
            elif line.lower().startswith("message"):
                message = line.split(":", 1)[1].strip()
        if score is None:
            score = 0
        if message is None:
            message = "ERROR: Unable to generate message"
        return score, message
    except Exception as e:
        print(f"❌ GPT error: {e}")
        return 0, "ERROR: Unable to generate message"

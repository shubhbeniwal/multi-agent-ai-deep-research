from utils.groq_client import client

from utils.web_search import search_web
from utils.groq_client import client

def research_business(topic):

    web_results = search_web(topic)

    prompt = f"""
You are a business strategy analyst.

Topic:
{topic}

Latest Web Research:
{web_results}

Analyze:

1. Market Impact
2. Industry Adoption
3. Business Opportunities
4. Business Risks
5. ROI Potential
6. Competitive Landscape

Return only research notes.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
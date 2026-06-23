from utils.groq_client import client

from utils.web_search import search_web
from utils.groq_client import client

def research_future(topic):

    web_results = search_web(topic)

    prompt = f"""
You are a future trends analyst.

Topic:
{topic}

Latest Web Research:
{web_results}

Analyze:

1. Emerging Trends
2. Future Opportunities
3. Future Risks
4. Research Directions
5. Industry Predictions
6. Long-Term Impact

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
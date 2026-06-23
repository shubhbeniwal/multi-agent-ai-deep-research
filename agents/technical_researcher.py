from utils.groq_client import client

from utils.web_search import search_web
from utils.groq_client import client

def research_technical(topic):

    web_results = search_web(topic)

    prompt = f"""
You are a senior technical research analyst.

Topic:
{topic}

Latest Web Research:
{web_results}

Create detailed technical research covering:

1. Technical Overview
2. Architecture
3. Technologies Involved
4. Technical Challenges
5. Technical Advantages
6. Future Technical Developments

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
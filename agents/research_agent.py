from utils.groq_client import client


def research_topic(topic, plan):

    prompt = f"""
You are an expert research analyst.

Research Topic:
{topic}

Research Plan:
{plan}

Follow the research plan carefully.

Create detailed research notes covering:

1. Overview
2. Key Concepts
3. Applications
4. Advantages
5. Challenges
6. Future Trends

Use the research plan to guide your analysis.

Provide detailed and structured findings.

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
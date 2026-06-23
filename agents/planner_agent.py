from utils.groq_client import client


def create_research_plan(topic):

    prompt = f"""
You are an expert research strategist.

Research Topic:
{topic}

Create a research plan.

Include:

1. Main Areas to Investigate
2. Important Subtopics
3. Key Questions
4. Recommended Research Focus

Return a structured plan.
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
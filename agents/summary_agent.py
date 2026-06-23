from utils.groq_client import client


def summarize_research(research_notes):

    prompt = f"""
You are an expert executive summary writer.

Create a concise and professional summary from the research below.

Research:

{research_notes}

Requirements:

- Keep it concise
- Highlight the most important points
- Use bullet points when appropriate
- Make it easy for executives to understand

Return only the summary.
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
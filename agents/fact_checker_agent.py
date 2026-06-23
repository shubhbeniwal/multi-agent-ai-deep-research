from utils.groq_client import client


def fact_check_research(research_notes):

    prompt = f"""
You are a senior fact-checking analyst.

Review the following research.

Research:

{research_notes}

Tasks:

1. Identify any questionable claims.
2. Identify assumptions.
3. Point out areas requiring verification.
4. Highlight possible inaccuracies.
5. Assess overall reliability.

Return a professional fact-checking report.
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
from utils.groq_client import client


def merge_research(
    technical,
    business,
    future
):

    prompt = f"""
You are a senior research editor.

Merge the following research streams into one unified research document.

TECHNICAL RESEARCH:
{technical}

BUSINESS RESEARCH:
{business}

FUTURE RESEARCH:
{future}

Create one coherent report.

Return only the merged research.
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
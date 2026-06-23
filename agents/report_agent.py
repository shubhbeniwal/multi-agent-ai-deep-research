from utils.groq_client import client


def generate_report(topic, research_notes, summary):

    prompt = f"""
You are a professional research consultant.

Create a detailed research report.

Topic:
{topic}

Executive Summary:
{summary}

Research Notes:
{research_notes}

Structure:

# Title

# Executive Summary

# Detailed Analysis

# Key Findings

# Recommendations

# Conclusion

Return only the report.
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
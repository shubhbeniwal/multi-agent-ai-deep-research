from duckduckgo_search import DDGS


def search_web(topic):

    results_text = ""

    with DDGS() as ddgs:

        results = ddgs.text(
            topic,
            max_results=5
        )

        for item in results:

            results_text += f"""

Title:
{item['title']}

Source:
{item['href']}

Summary:
{item['body']}

=================================
"""

    return results_text
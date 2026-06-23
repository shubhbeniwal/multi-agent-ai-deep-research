from agents.research_agent import research_topic
from agents.summary_agent import summarize_research
from agents.report_agent import generate_report
from agents.fact_checker_agent import fact_check_research
from utils.memory_manager import (
    save_topic,
    load_topics
)
from agents.planner_agent import create_research_plan



import concurrent.futures

from agents.technical_researcher import (
    research_technical
)

from agents.business_researcher import (
    research_business
)

from agents.future_researcher import (
    research_future
)

from agents.merge_agent import (
    merge_research
)


def run_research_assistant(topic):
    
    previous_topics = load_topics()

    print("\n📚 Previous Topics:\n")

    for item in previous_topics[-5:]:
        print("-", item)

    print("\n🧠 Planning Research...\n")

    plan = create_research_plan(topic)

    print(plan)

    print("\n✅ Research Plan Complete")

    
    
    
    print("\n🔍 Running Parallel Research Agents...\n")

    with concurrent.futures.ThreadPoolExecutor() as executor:

        technical_future = executor.submit(
            research_technical,
            topic
        )

        business_future = executor.submit(
            research_business,
            topic
        )

        future_future = executor.submit(
            research_future,
            topic
        )

        technical_research = technical_future.result()

        business_research = business_future.result()

        future_research = future_future.result()

    print("✅ All Research Agents Complete")

    print("\n🔗 Merging Research...\n")

    research = merge_research(
        technical_research,
        business_research,
        future_research
    )

    print("✅ Research Merge Complete")
    
    
    

    print("\n📝 Summarizing...\n")

    summary = summarize_research(
        research
    )

    print("✅ Summary Complete")

    print("\n🔎 Fact Checking...\n")

    fact_check = fact_check_research(
        research
    )

    print("✅ Fact Check Complete")

    print("\n📊 Building Report...\n")

    report = generate_report(
        topic,
        research,
        summary
    )

    print("✅ Report Complete")

    save_topic(topic)

    return report


if __name__ == "__main__":

    topic = input(
        "Enter a research topic: "
    )

    final_report = run_research_assistant(
        topic
    )

    print("\n")
    print("=" * 80)
    print(final_report)
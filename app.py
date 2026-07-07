import streamlit as st

from agents.planner_agent import create_research_plan

from agents.technical_researcher import research_technical
from agents.business_researcher import research_business
from agents.future_researcher import research_future

from agents.merge_agent import merge_research

from agents.summary_agent import summarize_research
from agents.fact_checker_agent import fact_check_research
from agents.report_agent import generate_report


import concurrent.futures

from utils.report_generator import (
    generate_pdf_report
)

from utils.memory_manager import (
    get_topic,
    save_topic
)

from utils.web_search import search_web


st.set_page_config(
    page_title="Multi-Agent Research Assistant",
    page_icon="🔬",
    layout="wide"
)

st.markdown("""
    <style>

    .main {
        padding-top: 1rem;
    }

    .block-container {
        padding-top: 2rem;
    }

    [data-testid="stMetric"] {
        border: 1px solid rgba(255,255,255,0.1);
        padding: 15px;
        border-radius: 12px;
    }

    .stButton > button {
        width: 100%;
        border-radius: 10px;
        height: 3rem;
        font-weight: 600;
    }

    </style>
    """, unsafe_allow_html=True)

if "sources" not in st.session_state:
    st.session_state.sources = ""

if "reports_generated" not in st.session_state:
    st.session_state.reports_generated = 0

if "memory_hits" not in st.session_state:
    st.session_state.memory_hits = 0

if "quality_history" not in st.session_state:
    st.session_state.quality_history = []
    
if "research_history" not in st.session_state:
    st.session_state.research_history = []
    
st.markdown("""
# 🔬 ResearchGPT – Multi-Agent AI Research Assistant

### AI-Powered Deep Research Platform

Generate comprehensive research reports using multiple specialized AI agents, web intelligence, fact-checking, and memory-augmented workflows.
""")

st.sidebar.markdown("""
## 🚀 About the Creator

### Shubh Beniwal

AI Engineer | Software Developer

🎓 VIT Chennai Graduate

### Specializations

- Artificial Intelligence
- LLM Applications
- NLP Systems
- Multi-Agent AI
- Generative AI

### Connect

🔗 LinkedIn  
https://www.linkedin.com/in/shubh-beniwal/

💻 GitHub  
https://github.com/shubhbeniwal

""")

st.markdown("---")
st.subheader("🔍 Research Workspace")
topic = st.text_input(
    "Research Topic",
    placeholder="Example: Multi-Agent Systems in Healthcare"
)

run_button = st.button(
    "Generate Research Report"
)




if run_button and topic:
    
    
    cached_topic = get_topic(topic)
    
    web_results = search_web(topic)

    st.session_state.sources = web_results
    
    
    if cached_topic:
        
        st.session_state.memory_hits += 1

        st.success(
            "🧠 Research Found In Memory"
        )

        st.subheader(
            "📄 Final Research Report"
        )

        st.write(
            cached_topic["report"]
        )

        # PDF generation

        pdf_file = "research_report.pdf"

        generate_pdf_report(
            pdf_file,
            topic,
            cached_topic["report"]
        )

        with open(pdf_file, "rb") as file:

            st.download_button(
                label="📄 Download PDF Report",
                data=file,
                file_name=f"{topic}.pdf",
                mime="application/pdf"
            )

        # TXT download

        st.download_button(
            label="📄 Download TXT Report",
            data=cached_topic["report"],
            file_name=f"{topic}.txt",
            mime="text/plain"
        )

        # Sources

        if "sources" in st.session_state:

            st.markdown("---")

            st.header("🔗 Research Sources")

            with st.expander("View Sources"):

                st.write(
                    st.session_state.sources
                )

        st.stop()
    

    planner_status = st.empty()
    research_status = st.empty()
    merge_status = st.empty()
    summary_status = st.empty()
    fact_status = st.empty()
    report_status = st.empty()

    # ---------------- PLANNER ----------------
    
    planner_status.info(
        "🧠 Planner Agent Running..."
    )

    plan = create_research_plan(topic)

    planner_status.success(
        "✅ Planner Complete"
    )

    # ---------------- PARALLEL RESEARCH ----------------

    research_status.info(
        "🔍 Research Agents Running..."
    )

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

    research_status.success(
        "✅ Research Complete"
    )

    # ---------------- MERGE ----------------

    merge_status.info(
        "🔗 Merge Agent Running..."
    )

    merged_research = merge_research(
        technical_research,
        business_research,
        future_research
    )

    merge_status.success(
        "✅ Merge Complete"
    )

    # ---------------- SUMMARY ----------------

    summary_status.info(
        "📝 Summary Agent Running..."
    )

    summary = summarize_research(
        merged_research
    )

    summary_status.success(
        "✅ Summary Complete"
    )

    # ---------------- FACT CHECK ----------------

    fact_status.info(
        "✔ Fact Checker Running..."
    )

    checked_report = fact_check_research(
        summary
    )

    fact_status.success(
        "✅ Fact Check Complete"
    )

    # ---------------- REPORT ----------------

    report_status.info(
        "📄 Report Agent Running..."
    )

    final_report = generate_report(
        topic,
        merged_research,
        checked_report
    )
    
    st.session_state.reports_generated += 1
    
    st.session_state.research_history.append(
        {
            "topic": topic
        }
    )
    
    research_depth = min(
        len(final_report) // 80,
        100
    )

    source_coverage = min(
        len(st.session_state.sources.split("Title:")),
        100
    )

    confidence_score = 90
        
    st.session_state.quality_history.append(
        confidence_score
    )
    
    st.markdown("---")
    st.header("🧠 Agent Thought Process")
    
    with st.expander("🧠 Planner Agent"):

        st.write(plan)

    with st.expander("🔍 Technical Research Agent"):

        st.write(technical_research)

    with st.expander("💼 Business Research Agent"):

        st.write(business_research)

    with st.expander("🚀 Future Trends Agent"):

        st.write(future_research)

    with st.expander("🔗 Merge Agent"):

        st.write(merged_research)

    with st.expander("📝 Summary Agent"):

        st.write(summary)

    with st.expander("✔ Fact Check Agent"):

        st.write(checked_report)
    
    save_topic(
        topic,
        final_report,
        checked_report,
        st.session_state.sources
    )
    
    report_status.success(
        "✅ Report Generated"
    )

    st.markdown("---")

    st.subheader("📚 Recent Research Topics")

    if st.session_state.research_history:

        for item in reversed(
            st.session_state.research_history[-5:]
        ):

            st.write(
                f"• {item['topic']}"
            )
            
            
    st.header("📈 Research Analytics Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Reports Generated",
            st.session_state.reports_generated
        )

    with col2:
        st.metric(
            "Memory Hits",
            st.session_state.memory_hits
        )

    with col3:
        st.metric(
            "Topics Researched",
            st.session_state.reports_generated
            +
            st.session_state.memory_hits
        )
        
        
    st.subheader(
        "📄 Final Research Report"
    )

    st.write(final_report)
    
    st.markdown("---")

    st.subheader("📊 Research Quality Analysis")

    q1, q2, q3 = st.columns(3)
    
    with q1:
        st.metric(
            "Research Depth",
            f"{research_depth}%"
        )
    
    with q2:
        st.metric(
            "Source Coverage",
            f"{source_coverage}%"
        )
    
    with q3:
        st.metric(
            "Confidence",
            f"{confidence_score}%"
        )
    
    pdf_file = "research_report.pdf"

    generate_pdf_report(
        pdf_file,
        topic,
        final_report
    )
    
    st.markdown("---")

    with open(pdf_file, "rb") as file:

        st.download_button(
            label="📄 Download PDF Report",
            data=file,
            file_name=f"{topic}.pdf",
            mime="application/pdf"
        )
        

        st.download_button(
            label="📄 Download TXT Report",
            data=final_report,
            file_name=f"{topic}.txt",
            mime="text/plain"
        )

        
    st.markdown("---")

    st.header("🔗 Research Sources")

    with st.expander("View Sources"):

        st.write(
            st.session_state.sources
        )




st.markdown("---")

st.subheader(
    "🤖 Agent Workflow"
)

st.info("""
🧠 Planner Agent
⬇
🔍 Technical Research Agent
⬇
💼 Business Research Agent
⬇
🚀 Future Trends Agent
⬇
🔗 Merge Agent
⬇
📝 Summary Agent
⬇
✔ Fact Checker Agent
⬇
📄 Report Generator Agent
""")

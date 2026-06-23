# 🔬 AI Deep Research Platform

## Multi-Agent AI Research, Web Intelligence & Memory-Augmented Report Generation

A fully deployed Multi-Agent AI Deep Research Platform that autonomously plans, researches, validates, and generates professional research reports using collaborative AI agents, web intelligence, memory caching, and analytics.

---

## 🚀 Live Demo

https://multi-agent-ai-deep-research-5elammefdpxnujsrjzjw9s.streamlit.app/

---

## 📌 Overview

Traditional research assistants rely on a single AI model.

This project implements a Multi-Agent Architecture where specialized AI agents collaborate to perform:

* Research Planning
* Technical Analysis
* Business Analysis
* Future Trend Forecasting
* Research Merging
* Fact Validation
* Professional Report Generation

The platform also integrates:

* Web Intelligence
* Research Memory Cache
* PDF/TXT Report Export
* Analytics Dashboard
* Source Transparency

---

## 🏗 Architecture

```text
User Query
    ↓
Planner Agent
    ↓

━━━━━━━━━━━━━━━━━━━━━━━
Technical Agent
Business Agent
Future Trends Agent
━━━━━━━━━━━━━━━━━━━━━━━

    ↓
Merge Agent
    ↓
Summary & Validation Agent
    ↓
Report Generation Agent
    ↓
Memory Layer
    ↓
PDF / TXT Export
```

---

## 🧠 Agent Responsibilities

### Planner Agent

Creates the research strategy and determines how the topic should be explored.

---

### Technical Research Agent

Analyzes:

* Technologies
* Methodologies
* Technical Concepts
* Industry Implementations

---

### Business Research Agent

Analyzes:

* Market Trends
* Business Value
* Industry Adoption
* Commercial Impact

---

### Future Trends Agent

Analyzes:

* Emerging Innovations
* Future Predictions
* Industry Direction
* Long-Term Opportunities

---

### Merge Agent

Combines outputs from all research agents into a unified research document.

---

### Summary & Validation Agent

Produces:

* Executive Summary
* Key Findings
* Validation Notes

---

### Report Generation Agent

Creates the final professional report.

---

## 🌐 Web Intelligence Layer

The platform uses DuckDuckGo Search to retrieve:

* Current information
* Supporting sources
* Research references

Sources are displayed transparently within the application.

---

## ⚡ Memory-Augmented Research

The application includes a local memory system.

Features:

* Cached research reports
* Faster repeated queries
* Reduced API costs
* Memory hit analytics

Research is stored inside:

```text
memory/research_memory.json
```

---

## 📊 Analytics Dashboard

Tracks:

* Reports Generated
* Topics Researched
* Memory Hits
* Research Quality Metrics

---

## 📄 Export Features

Generate:

### PDF Reports

Professional research reports generated automatically.

### TXT Reports

Lightweight downloadable text reports.

---

## 🛠 Technology Stack

### Frontend

* Streamlit

### LLM Provider

* Groq

### Model

* Llama 3.3 70B Versatile

### Programming Language

* Python

### Search Engine

* DuckDuckGo Search

### Report Generation

* ReportLab

### Storage

* JSON Memory Store

### Concurrency

* concurrent.futures

---

## 📂 Project Structure

```text
AI-Deep-Research-Platform
│
├── agents
│   ├── planner_agent.py
│   ├── technical_researcher.py
│   ├── business_researcher.py
│   ├── future_researcher.py
│   ├── merge_agent.py
│   ├── summary_agent.py
│   ├── fact_checker_agent.py
│   └── report_agent.py
│
├── utils
│   ├── groq_client.py
│   ├── web_search.py
│   ├── report_generator.py
│   ├── memory_manager.py
│
├── memory
│   └── research_memory.json
│
├── app.py
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙ Installation

### Clone Repository

```bash
git clone https://github.com/shubhbeniwal/multi-agent-ai-deep-research.git

cd multi-agent-ai-deep-research
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a .env file:

```env
GROQ_API_KEY=your_api_key_here
```

Get your API key from:

https://console.groq.com

---

## ▶ Run Application

```bash
streamlit run app.py
```

---

## 🎯 Use Cases

* Academic Research
* Market Research
* Technology Analysis
* Industry Reports
* Competitive Intelligence
* AI Trend Analysis
* Business Research

---

## 🚀 Future Improvements

* Vector Database Integration
* RAG Pipeline
* Multi-Model Support
* Agent Evaluation Framework
* Research Collaboration
* Cloud Database Storage
* Research History Dashboard
* Advanced Analytics

---

## 👨‍💻 About the Creator

Shubh Beniwal

AI Engineer | Software Developer

VIT Chennai Graduate

Passionate about:

* Artificial Intelligence
* LLM Applications
* NLP
* Multi-Agent Systems
* Generative AI

LinkedIn:
https://www.linkedin.com/in/shubh-beniwal/

GitHub:
https://github.com/shubhbeniwal

---

## ⭐ If you found this project useful, consider starring the repository.

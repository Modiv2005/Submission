# 🤖 Agentic AI Marketing Intelligence System

> An autonomous multi-agent AI platform that generates a complete 7-day marketing campaign from a synthetic business context using Large Language Models, AI-generated media, and an agentic orchestration pipeline.

---

## 📌 Project Overview

This project was developed as part of an AI Engineering technical assessment.

The system autonomously creates a complete first-week social media marketing campaign for a synthetic business by coordinating multiple specialized AI agents.

Starting with a business profile, the platform:

- Generates a synthetic business context
- Performs business and market analysis
- Creates a marketing strategy
- Plans a 7-day content calendar
- Generates engaging captions and marketing copy
- Produces AI-generated Instagram posts
- Creates promotional reels
- Reviews generated content for consistency
- Packages all outputs with execution logs

The complete workflow executes automatically while maintaining a **strict budget limit of ₹100**, with an actual execution cost of **₹0.00**.

---

# ✨ Features

- ✅ Multi-Agent AI Architecture
- ✅ Autonomous Workflow Execution
- ✅ Business Context Generation
- ✅ Marketing Strategy Generation
- ✅ Weekly Content Planning
- ✅ AI Caption Generation
- ✅ AI Image Generation
- ✅ Automated Reel Creation
- ✅ Structured Agent Memory
- ✅ Budget Tracking
- ✅ Execution Logging
- ✅ Modular & Scalable Architecture

---

# 🏗️ System Architecture

```text
                         Orchestrator
                              │
                              ▼
                SyntheticContextAgent
                              │
                              ▼
               BusinessAnalysisAgent
                              │
                              ▼
              MarketingStrategyAgent
                              │
                              ▼
                 WeeklyPlannerAgent
                              │
                              ▼
              ContentGenerationAgent
                              │
                              ▼
               MediaGenerationAgent
                    │                │
                    ▼                ▼
             Image Generator    Video Generator
                    │                │
                    └──────┬─────────┘
                           ▼
                   ReviewerAgent
                           │
                           ▼
                  PackagingAgent
                           │
                           ▼
                  Final Deliverables
```

---

# 🧠 AI Agents

| Agent | Responsibility |
|-------|----------------|
| SyntheticContextAgent | Generates a realistic business profile |
| BusinessAnalysisAgent | Identifies opportunities and challenges |
| MarketingStrategyAgent | Creates marketing objectives |
| WeeklyPlannerAgent | Plans the weekly campaign |
| ContentGenerationAgent | Generates captions and prompts |
| MediaGenerationAgent | Produces AI images and promotional videos |
| ReviewerAgent | Validates brand tone and content quality |
| PackagingAgent | Compiles final outputs and logs |

---

# 📁 Project Structure

```text
VaishaliModi_TrapeziumAI/
│
├── agents/
│   ├── base_agent.py
│   ├── context_agent.py
│   ├── analysis_agent.py
│   ├── strategy_agent.py
│   ├── content_agent.py
│   ├── media_agent.py
│   ├── review_agent.py
│   └── packaging_agent.py
│
├── core/
│   ├── logger.py
│   ├── memory.py
│   └── spend_tracker.py
│
├── models/
│   └── schemas.py
│
├── tests/
│   └── test_agents.py
│
├── outputs/
│   ├── day_1_post.jpg
│   ├── day_2_post.jpg
│   ├── day_3_post.jpg
│   ├── day_4_post.jpg
│   ├── day_5_post.jpg
│   ├── day_6_reel.mp4
│   ├── day_7_reel.mp4
│   ├── execution_trace.log
│   ├── spend_log.json
│   └── memory.json
│
├── main.py
├── README.md
└── .env
```

---

# 🚀 Technology Stack

- Python 3.11
- Google Gemini API
- Pydantic
- MoviePy
- Pollinations AI
- Requests
- Pillow
- OpenCV
- Pytest
- Python-dotenv

---

# ⚙️ Environment Variables

Create a `.env` file inside the project directory.

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

If no API key is provided, the application automatically falls back to mock inference, allowing the workflow to execute without failure.

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/Modiv2005/Submission.git
```

Navigate to the project

```bash
cd Submission
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install google-genai pydantic moviepy pytest requests pillow opencv-python pydantic-settings python-dotenv
```

---

# ▶️ Run the Project

```bash
PYTHONPATH=. python main.py
```

Execution takes approximately **2–3 minutes** while the system generates images and promotional reels.

---

# 🧪 Run Tests

```bash
PYTHONPATH=. pytest tests/
```

---

# 📦 Generated Deliverables

The system automatically generates:

- 📸 5 Instagram Post Images
- 🎬 2 Promotional Reels
- 📝 Marketing Captions
- 📄 Execution Logs
- 💾 Shared Agent Memory
- 💰 Budget Tracking Logs

---

# 💰 Budget Report

| Resource | Cost |
|-----------|------|
| Google Gemini (Free Tier) | ₹0 |
| Pollinations AI | ₹0 |
| MoviePy | ₹0 |
| Python Libraries | ₹0 |
| **Total Cost** | **₹0.00** |

---

# 📊 APIs & Libraries Used

### Google Gemini

Used for:

- Business reasoning
- Marketing strategy
- Content generation
- Structured JSON outputs

### Pollinations AI

Used for:

- AI Image Generation
- Marketing creatives

### MoviePy

Used for:

- Promotional Reel Generation
- Video Rendering

---

# 🛡️ Known Limitations

- Video generation uses programmatically rendered text animations to maintain zero operational cost.
- ReviewerAgent currently logs warnings instead of blocking execution.
- Image generation depends on the availability of the Pollinations service.

---

# 🔮 Future Improvements

- LangGraph-based Agent Orchestration
- Human-in-the-loop Review System
- Instagram Graph API Integration
- Vision-based AI Quality Review
- Multi-platform Publishing (Instagram, LinkedIn, X)
- Analytics Dashboard
- Campaign Performance Tracking
- Retrieval-Augmented Generation (RAG) Support

---



## ⭐ Assignment Highlights

- Multi-Agent AI System
- Autonomous Decision Making
- LLM Integration
- AI Image Generation
- Automated Video Creation
- Modular Python Architecture
- Budget-Constrained Execution
- Production-Oriented Code Structure
- Comprehensive Logging
- End-to-End Marketing Content Automation

---

**Thank you for reviewing this project!**

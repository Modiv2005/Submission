# Agentic AI Marketing Intelligence System

An autonomous, multi-agent AI software system that creates a privacy-safe synthetic business context, analyzes it, formulates a 7-day content strategy, and autonomously generates the complete first-week content set (5 Instagram posts and 2 reels).

## 🚀 Overview

This platform uses a modular, agentic architecture powered by LLMs (Google Gemini), Pollinations API (for zero-cost image generation), and MoviePy (for programmatic video generation). The entire workflow executes autonomously while strictly adhering to a **₹100 budget cap**.

**Final Project Spend:** ₹0.00 

## 🧠 Architecture Diagram

The system operates as a sequential pipeline of specialized agents. Each agent handles a distinct part of the reasoning and generation process, passing structured Pydantic models to the next via a centralized `Memory` store.

    +-----------------------+
    |  Orchestrator (Main)  |
    +-----------+-----------+
                |
    +-----------v-----------+
    | 1. SyntheticContextAgent: Defines the business
    | 2. BusinessAnalysisAgent: Finds gaps/opportunities
    | 3. MarketingStrategyAgent: Defines week objective
    | 4. WeeklyPlannerAgent: Plans 5 posts & 2 videos
    +-----------+-----------+
                |
    +-----------v-----------+
    | 5. ContentGenerationAgent: Writes captions & hooks
    | 6. ImageGenerationAgent: Renders static posts
    | 7. VideoGenerationAgent: Renders MP4 reels
    +-----------+-----------+
                |
    +-----------v-----------+
    | 8. ReviewerAgent: Validates brand consistency
    | 9. PackagingAgent: Compiles outputs & logs
    +-----------------------+

## 📁 Folder Structure

VaishaliModi_TrapeziumAI/
│
├── core/                       # Core engine mechanics
│   ├── logger.py               # Centralized observability
│   ├── memory.py               # Shared agent state management
│   └── spend_tracker.py        # Strict budget enforcement
│
├── models/
│   └── schemas.py              # Pydantic JSON schemas for agents
│
├── agents/                     # The multi-agent brain trust
│   ├── base_agent.py           # Base class with retry & LLM setup
│   ├── context_agent.py        # Generates business context
│   ├── analysis_agent.py       # Context analysis
│   ├── strategy_agent.py       # Strategy & weekly planning
│   ├── content_agent.py        # Copywriting and prompts
│   ├── media_agent.py          # Images (Pollinations) & Videos (MoviePy)
│   ├── review_agent.py         # Tone and brand validation
│   └── packaging_agent.py      # Final output compilation
│
├── tests/
│   └── test_agents.py          # Pytest suite for framework validation
│
├── outputs/                    # Generated Deliverables
│   ├── day_X_post.jpg          # Generated images
│   ├── day_X_reel.mp4          # Generated videos
│   ├── execution_trace.log     # Observability and agent decisions
│   ├── memory.json             # Structured outputs & state dump
│   └── spend_log.json          # Cost tracking
│
├── main.py                     # Entry point orchestrator
└── README.md                   # This file

## ⚙️ Environment Variables

To run this project, you need to provide a Gemini API key. If the key is absent, the system gracefully falls back to mock inference to prevent hard crashes and demonstrate the pipeline logic.

Create a `.env` file in the root directory (or export it to your shell):
GEMINI_API_KEY=your_gemini_api_key_here

## 🛠️ Installation Guide

1. **Clone or download the project** and navigate into the directory.
2. **Set up a Python virtual environment:**
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. **Install dependencies:**
   pip install google-genai pydantic moviepy pytest requests pillow opencv-python pydantic-settings python-dotenv

## 💻 Usage Guide

**Run the autonomous workflow:**
PYTHONPATH=. python main.py

*Note: The script takes about 2-3 minutes to run as it sequentially generates 5 images via the API and renders 2 videos programmatically.*

**Run the tests:**
PYTHONPATH=. pytest tests/

## 📚 Prompt Library & APIs

- **LLM Reasoning**: Handled via `google-genai` (Gemini 2.5 Pro). Prompts are heavily structured to enforce JSON outputs via Pydantic schemas.
- **Image Generation**: Handled via `image.pollinations.ai`. The `ContentGenerationAgent` creates specific visual descriptions which are URL-encoded and fetched securely.
- **Video Generation**: Uses `MoviePy`. The `ContentGenerationAgent` scripts short 5-second dynamic text reels, which are natively rendered using Python.

## 🛑 Known Limitations

- **Video Complexity**: To keep costs strictly at ₹0.00 without relying on heavily watermarked or gated APIs, video generation relies on programmatic text-on-background rendering via MoviePy.
- **Human-in-the-Loop Mocking**: Currently, if the `ReviewerAgent` flags a piece of content as inappropriate, it logs a warning but proceeds with packaging. In a full production environment, this would halt execution and trigger a manual CLI/UI prompt.

## 🔮 Future Improvements

1. **Agentic Framework Integration**: Migrate the custom `BaseAgent` class to LangGraph for advanced cyclic routing (e.g., automatically looping a failed image generation back to the Prompt Agent for adjustments).
2. **Social Media API Integration**: Add an `ExportAgent` that connects to Meta's Graph API to push approved assets directly to Instagram Drafts.
3. **Multimodal Review**: Pass the generated image bytes back into a Vision-capable LLM for the `ReviewerAgent` to verify that the image matches the prompt contextually.

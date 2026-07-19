import json
import os
from agents.base_agent import BaseAgent
from core.memory import memory

class PackagingAgent(BaseAgent):
    def __init__(self):
        super().__init__("PackagingAgent", "Packages the workflow outputs and generates README and documentation.")

    def package(self):
        self.logger.info("Packaging final outputs...")
        
        # Save complete memory state to output
        memory._save()
        
        context = memory.get("business_context")
        strategy = memory.get("marketing_strategy")
        
        # Generate README
        readme_content = f"""# Agentic AI Marketing Platform

## Overview
This platform autonomously generated a 7-day marketing strategy and content for:
**{context.get('name', 'Unknown')}** - {context.get('category', 'Unknown')}

## Workflow
1. Synthetic Context Generator Agent created the business profile.
2. Business Analysis Agent found gaps and opportunities.
3. Marketing Strategy Agent created the weekly objective and pillars.
4. Weekly Planner Agent planned exactly 5 static posts and 2 videos.
5. Content Generation Agent wrote the captions, hashtags, and media prompts.
6. Image & Video Generation Agents created the actual media files using Pollinations API and MoviePy.
7. Reviewer Agent validated the tone and brand consistency.

## Outputs
All generated assets (images, videos, logs, and this memory dump) are located in the `outputs/` folder.
- `outputs/execution_trace.log`: Complete execution trace of the agents.
- `outputs/spend_log.json`: Financial tracking proving the cost is under ₹100.
- `outputs/memory.json`: Full state and generated JSON structured outputs.
- `outputs/day_*`: The generated images and videos.

## Setup Instructions
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export GEMINI_API_KEY="your-api-key"
python main.py
```
"""
        with open("outputs/README.md", "w") as f:
            f.write(readme_content)
            
        self.logger.info("Packaging complete. README generated.")

import os
import json
import time
from typing import Any, Type, Optional
from pydantic import BaseModel
from google import genai
from google.genai import types

from core.logger import get_logger
from core.spend_tracker import spend_tracker
from core.memory import memory

class BaseAgent:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        self.logger = get_logger(name)
        
        # Check if API key is present
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            self.logger.warning("GEMINI_API_KEY not found. Attempting to use default auth or mock.")
            try:
                self.client = genai.Client()
            except Exception as e:
                self.logger.error(f"Failed to initialize GenAI client: {e}")
                self.client = None
        else:
            self.client = genai.Client(api_key=api_key)

    def execute_with_retry(self, prompt: str, schema: Optional[Type[BaseModel]] = None, max_retries: int = 3) -> Any:
        self.logger.info(f"Executing task with {max_retries} retries...")
        
        # Log input
        self.logger.debug(f"Prompt: {prompt}")

        for attempt in range(1, max_retries + 1):
            try:
                # Approximate cost calculation (Gemini Flash is very cheap, let's say ₹0.001 per call)
                spend_tracker.log_expense("Gemini API", 0.001, f"{self.name} inference attempt {attempt}")
                
                start_time = time.time()
                
                if not self.client:
                    # Mock behavior for testing when no key
                    self.logger.warning("No client available, returning mock response.")
                    time.sleep(1)
                    if schema:
                        # Return valid mock data based on schema name to prevent crashes
                        if schema.__name__ == "BusinessContext":
                            return schema(name="Cozy Cafe", category="Cafe", location="Downtown", main_products=["Coffee", "Pastries"], target_customers="Locals", tone="Friendly", commercial_goal="Increase footfall")
                        elif schema.__name__ == "AnalysisResult":
                            return schema(summary="Local cafe selling coffee.", strongest_offers=["Morning combo"], trust_signals=["Freshly baked"], customer_needs=["Quick coffee"], opportunities=["Winter specials"], assumptions=["None"])
                        elif schema.__name__ == "MarketingStrategy":
                            return schema(objective="Brand awareness", target_audience="Office workers", content_pillars=["Coffee", "Community", "Quality"], key_messages=["Best coffee in town"], tone="Warm", calls_to_action=["Visit us"], format_mix="5 posts, 2 videos", reasoning="Simple and effective")
                        elif schema.__name__ == "WeeklyContentPlan":
                            items = []
                            for i in range(1, 6):
                                items.append({"day": i, "format": "static", "topic": f"Topic {i}", "hook": "Hook", "content_idea": "Idea", "caption_direction": "Caption", "call_to_action": "Visit", "business_insight": "Insight"})
                            for i in range(6, 8):
                                items.append({"day": i, "format": "video", "topic": f"Topic {i}", "hook": "Hook", "content_idea": "Idea", "caption_direction": "Caption", "call_to_action": "Visit", "business_insight": "Insight"})
                            return schema(items=items)
                        elif schema.__name__ == "GeneratedAsset":
                            return schema(day=1, format="static", title="Title", hook="Hook", caption="Caption", cta="CTA", hashtags="#cafe", design_prompt="A cozy cafe", video_prompt="A cozy cafe", reasoning="Reason")
                        elif schema.__name__ == "ReviewResult":
                            return schema(is_approved=True, feedback="Looks good")
                        return schema.model_construct()
                    return "Mock response"
                
                # Setup generation config with structured output if schema is provided
                config = types.GenerateContentConfig(
                    temperature=0.7,
                )
                if schema:
                    config.response_mime_type = "application/json"
                    config.response_schema = schema

                response = self.client.models.generate_content(
                    model='gemini-2.5-pro',
                    contents=prompt,
                    config=config
                )
                
                execution_time = time.time() - start_time
                self.logger.info(f"Execution successful in {execution_time:.2f}s")
                
                if schema:
                    try:
                        # Clean up response text in case it's wrapped in markdown
                        text = response.text
                        if text.startswith("```json"):
                            text = text[7:-3]
                        result = schema.parse_raw(text)
                        self.logger.debug(f"Structured output generated: {result.json()}")
                        return result
                    except Exception as e:
                        self.logger.error(f"Failed to parse structured output: {e}. Raw response: {response.text}")
                        raise e
                else:
                    self.logger.debug(f"Output: {response.text}")
                    return response.text

            except Exception as e:
                self.logger.error(f"Attempt {attempt} failed: {e}")
                if attempt == max_retries:
                    self.logger.error("Max retries reached. Failing task.")
                    raise e
                time.sleep(2) # Backoff before retry

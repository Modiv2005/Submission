from agents.base_agent import BaseAgent
from models.schemas import GeneratedAsset
from core.memory import memory
import json

class ContentGenerationAgent(BaseAgent):
    def __init__(self):
        super().__init__("ContentGenerationAgent", "Generates captions, hashtags, and media prompts for each planned item.")

    def generate_content(self, day_plan: dict) -> GeneratedAsset:
        self.logger.info(f"Generating content for Day {day_plan['day']}...")
        
        context = memory.get("business_context")
        
        prompt = f"""
        You are a Content Generation Agent.
        Based on this business context: {json.dumps(context)}
        And this specific plan for the day: {json.dumps(day_plan)}
        
        Generate the final content asset including:
        - title
        - hook (the actual words to use)
        - caption (full text ready for Instagram)
        - cta (Call to action)
        - hashtags (string of hashtags)
        - design_prompt (Detailed prompt for an image generator API to create a visually appealing, brand-consistent image)
        - video_prompt (Detailed prompt/script for a short video, if the format is video. If static, leave empty or null)
        - reasoning (Why this content works)
        
        Format MUST match the provided schema.
        """
        
        asset = self.execute_with_retry(prompt, schema=GeneratedAsset)
        
        if day_plan['format'] == 'video' and not asset.video_prompt:
            asset.video_prompt = "A visually appealing short video summarizing the topic."
            
        return asset

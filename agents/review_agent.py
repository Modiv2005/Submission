from agents.base_agent import BaseAgent
from models.schemas import GeneratedAsset
from pydantic import BaseModel
import json

class ReviewResult(BaseModel):
    is_approved: bool
    feedback: str

class ReviewerAgent(BaseAgent):
    def __init__(self):
        super().__init__("ReviewerAgent", "Validates that every asset matches its planned message, uses the intended tone, and contains no unsupported claims.")

    def review_asset(self, asset: GeneratedAsset, strategy: dict) -> ReviewResult:
        self.logger.info(f"Reviewing asset for Day {asset.day}...")
        
        prompt = f"""
        You are a Reviewer Agent.
        Review the following generated asset against the marketing strategy.
        
        Strategy Tone: {strategy.get('tone')}
        Key Messages: {strategy.get('key_messages')}
        
        Asset:
        Title: {asset.title}
        Caption: {asset.caption}
        CTA: {asset.cta}
        
        Does this asset match the planned message, use the intended tone, and contain NO unsupported claims?
        Output MUST be structured JSON with 'is_approved' (boolean) and 'feedback' (string).
        """
        
        result = self.execute_with_retry(prompt, schema=ReviewResult)
        
        if result.is_approved:
            self.logger.info(f"Asset for Day {asset.day} approved.")
        else:
            self.logger.warning(f"Asset for Day {asset.day} rejected. Feedback: {result.feedback}")
            
        return result

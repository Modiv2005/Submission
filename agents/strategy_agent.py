from agents.base_agent import BaseAgent
from models.schemas import MarketingStrategy, WeeklyContentPlan
from core.memory import memory
import json

class MarketingStrategyAgent(BaseAgent):
    def __init__(self):
        super().__init__("MarketingStrategyAgent", "Creates the first-week strategy.")

    def strategize(self) -> MarketingStrategy:
        self.logger.info("Generating marketing strategy...")
        
        context = memory.get("business_context")
        analysis = memory.get("business_analysis")
        
        prompt = f"""
        You are a Marketing Strategy Agent.
        Based on this context: {json.dumps(context)}
        And this analysis: {json.dumps(analysis)}
        
        Create a 7-day marketing strategy. Define:
        1. The week's objective.
        2. Specific target audience.
        3. 3-5 Content pillars.
        4. Key messages.
        5. Tone.
        6. Calls to action.
        7. Format mix (MUST be 5 static posts, 2 videos).
        8. Reasoning behind the strategy.
        
        Output MUST be in structured JSON format according to the schema.
        """
        
        strategy = self.execute_with_retry(prompt, schema=MarketingStrategy)
        memory.set("marketing_strategy", strategy.model_dump())
        return strategy


class WeeklyPlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__("WeeklyPlannerAgent", "Creates the 7-day content plan (5 posts, 2 videos).")

    def plan_week(self) -> WeeklyContentPlan:
        self.logger.info("Generating weekly content plan...")
        
        context = memory.get("business_context")
        strategy = memory.get("marketing_strategy")
        
        prompt = f"""
        You are a Weekly Planner Agent.
        Based on this context: {json.dumps(context)}
        And this strategy: {json.dumps(strategy)}
        
        Create a 7-day content plan containing EXACTLY 5 static posts and 2 videos.
        For each day (1-7), provide:
        - format (static or video)
        - topic
        - hook
        - content idea
        - caption direction
        - call to action
        - business insight supporting it
        
        Ensure exactly 2 items have format='video' and 5 items have format='static'.
        Output MUST be in structured JSON format according to the schema.
        """
        
        plan = self.execute_with_retry(prompt, schema=WeeklyContentPlan)
        memory.set("weekly_plan", plan.model_dump())
        return plan

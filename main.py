import os
import json
from dotenv import load_dotenv

from core.logger import get_logger
from core.memory import memory
from core.spend_tracker import spend_tracker
from agents.context_agent import SyntheticContextAgent
from agents.analysis_agent import BusinessAnalysisAgent
from agents.strategy_agent import MarketingStrategyAgent, WeeklyPlannerAgent
from agents.content_agent import ContentGenerationAgent
from agents.media_agent import ImageGenerationAgent, VideoGenerationAgent
from agents.review_agent import ReviewerAgent
from agents.packaging_agent import PackagingAgent

load_dotenv()

def main():
    logger = get_logger("Workflow")
    logger.info("Starting autonomous agentic workflow...")
    
    # Check budget
    if spend_tracker.current_spend >= spend_tracker.budget_limit:
        logger.error("Budget limit reached before starting. Aborting.")
        return
        
    try:
        # 1. Context Generation
        context_agent = SyntheticContextAgent()
        context_agent.generate_context()
        
        # 2. Business Analysis
        analysis_agent = BusinessAnalysisAgent()
        analysis_agent.analyze()
        
        # 3. Strategy
        strategy_agent = MarketingStrategyAgent()
        strategy_agent.strategize()
        
        # 4. Planning
        planner_agent = WeeklyPlannerAgent()
        plan = planner_agent.plan_week()
        
        # 5. Content & Media Generation
        content_agent = ContentGenerationAgent()
        image_agent = ImageGenerationAgent()
        video_agent = VideoGenerationAgent()
        reviewer_agent = ReviewerAgent()
        
        strategy_data = memory.get("marketing_strategy")
        
        # Ensure we don't process more than 7 items
        items = plan.items[:7]
        
        for item in items:
            day_plan = item.model_dump()
            day = day_plan['day']
            format_type = day_plan['format']
            
            # Generate content
            asset = content_agent.generate_content(day_plan)
            
            # Media generation
            if format_type == 'video':
                asset.file_path = video_agent.generate_video(asset.video_prompt or asset.title, day)
            else:
                asset.file_path = image_agent.generate_image(asset.design_prompt, day)
                
            # Review
            review_result = reviewer_agent.review_asset(asset, strategy_data)
            
            # Even if rejected, we keep it for this version but log it. A more complex workflow would retry.
            if not review_result.is_approved:
                logger.warning(f"Human intervention might be needed for Day {day} due to reviewer feedback.")
            
            # Save asset to memory
            memory.add_asset(f"{format_type}s", asset.model_dump())
            
        # 6. Packaging
        packaging_agent = PackagingAgent()
        packaging_agent.package()
        
        logger.info("Workflow completed successfully!")
        
    except Exception as e:
        logger.error(f"Workflow failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()

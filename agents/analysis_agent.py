from agents.base_agent import BaseAgent
from models.schemas import AnalysisResult
from core.memory import memory

class BusinessAnalysisAgent(BaseAgent):
    def __init__(self):
        super().__init__("BusinessAnalysisAgent", "Analyzes the business context to identify offers, gaps, and opportunities.")

    def analyze(self) -> AnalysisResult:
        self.logger.info("Analyzing business context...")
        
        context = memory.get("business_context")
        source_pack = memory.get("synthetic_source_pack")
        
        if not context or not source_pack:
            raise ValueError("Context or source pack is missing from memory.")
            
        prompt = f"""
        You are a Business Analysis Agent.
        Analyze the following business context and source pack:
        Context: {context}
        Source Pack: {source_pack}
        
        Identify:
        1. A summary of what they sell and who they reach.
        2. Their strongest offers.
        3. Trust signals (why should customers trust them?).
        4. Core customer needs.
        5. Local or seasonal opportunities.
        6. Assumptions or missing information you have made.
        
        Output MUST be in structured JSON format according to the schema.
        """
        
        analysis = self.execute_with_retry(prompt, schema=AnalysisResult)
        
        # Save to memory
        memory.set("business_analysis", analysis.model_dump())
        return analysis

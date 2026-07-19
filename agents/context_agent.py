from agents.base_agent import BaseAgent
from models.schemas import BusinessContext
from core.memory import memory

class SyntheticContextAgent(BaseAgent):
    def __init__(self):
        super().__init__("SyntheticContextAgent", "Generates a synthetic business source pack and business context.")

    def generate_context(self) -> BusinessContext:
        self.logger.info("Generating synthetic business context...")
        
        prompt = """
        You are an AI tasked with creating a synthetic business source pack.
        Assume a small business (e.g., a bakery, salon, fitness studio, or local retailer).
        Invent its name, category, location, main products/services, target customers, brand tone, and a primary commercial goal.
        Ensure it represents a realistic local small business.
        Output MUST be in structured JSON format according to the provided schema.
        """
        
        context = self.execute_with_retry(prompt, schema=BusinessContext)
        
        # Save to memory
        memory.set("business_context", context.model_dump())
        
        # Create a synthetic source pack string
        source_pack = f"""
        SYNTHETIC SOURCE PACK:
        Business Name: {context.name}
        Category: {context.category}
        Location: {context.location}
        Products: {', '.join(context.main_products)}
        Customers: {context.target_customers}
        Tone: {context.tone}
        Goal: {context.commercial_goal}
        
        Sample Website Text:
        Welcome to {context.name}! We specialize in providing the best {', '.join(context.main_products)} in {context.location}. 
        Our goal is to serve {context.target_customers} with a {context.tone} touch.
        """
        memory.set("synthetic_source_pack", source_pack)
        
        return context

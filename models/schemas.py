from pydantic import BaseModel, Field
from typing import List, Optional

class BusinessContext(BaseModel):
    name: str = Field(description="Name of the assumed business")
    category: str = Field(description="Category of the business (e.g. bakery, salon)")
    location: str = Field(description="Location of the business")
    main_products: List[str] = Field(description="Main products or services offered")
    target_customers: str = Field(description="Target customers")
    tone: str = Field(description="Brand voice and tone")
    commercial_goal: str = Field(description="Commercial goal of the content")
    
class AnalysisResult(BaseModel):
    summary: str = Field(description="Summary of what the business sells and who it should reach")
    strongest_offers: List[str] = Field(description="The strongest offers")
    trust_signals: List[str] = Field(description="Trust signals")
    customer_needs: List[str] = Field(description="Customer needs")
    opportunities: List[str] = Field(description="Local or seasonal opportunities")
    assumptions: List[str] = Field(description="Assumptions or missing information")

class MarketingStrategy(BaseModel):
    objective: str = Field(description="The week's objective")
    target_audience: str = Field(description="Specific target audience for this week")
    content_pillars: List[str] = Field(description="Three to five content pillars")
    key_messages: List[str] = Field(description="Key messages to convey")
    tone: str = Field(description="Tone of the week")
    calls_to_action: List[str] = Field(description="Allowed calls to action")
    format_mix: str = Field(description="Format mix (e.g., 5 posts, 2 videos)")
    reasoning: str = Field(description="Reasoning behind the strategy")

class ContentPlanItem(BaseModel):
    day: int = Field(description="Day number (1 to 7)")
    format: str = Field(description="Format: 'static' or 'video'")
    topic: str = Field(description="Topic for the day")
    hook: str = Field(description="Hook to grab attention")
    content_idea: str = Field(description="Content idea")
    caption_direction: str = Field(description="Caption direction")
    call_to_action: str = Field(description="Specific call to action")
    business_insight: str = Field(description="Business insight that supports this item")

class WeeklyContentPlan(BaseModel):
    items: List[ContentPlanItem] = Field(description="List of 7 items (5 static, 2 video)")

class GeneratedAsset(BaseModel):
    day: int
    format: str
    title: str
    hook: str
    caption: str
    cta: str
    hashtags: str
    design_prompt: str
    video_prompt: Optional[str] = None
    reasoning: str
    file_path: Optional[str] = None

class AllAssets(BaseModel):
    assets: List[GeneratedAsset]

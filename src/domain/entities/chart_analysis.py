from pydantic import BaseModel
from datetime import datetime, timezone
class ChartAnalysis(BaseModel):
    id: str
    chart_image_id: str  # Links to ChartImage
    question: str
    answer: str
    created_at: datetime = datetime.now(timezone.utc)
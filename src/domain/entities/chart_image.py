from pydantic import BaseModel
from datetime import datetime, timezone

class ChartImage(BaseModel):
    id: str  # UUID
    user_id: str  # Owner of the chart
    image_data: bytes  # Or file path if storing externally
    uploaded_at: datetime = datetime.now(timezone.utc)
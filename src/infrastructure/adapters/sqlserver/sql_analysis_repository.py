from sqlalchemy import create_engine
from src.domain.ports import AnalysisRepositoryPort
from src.domain.entities import ChartAnalysis, ChartImage
class SqlAnalysisRepository(AnalysisRepositoryPort):
    def __init__(self, connection_string: str):
        self._engine = create_engine(connection_string)

    def save(self, image: ChartImage) -> str:
        with self._engine.connect() as conn:
            conn.execute(
                "INSERT INTO Charts (Id, UserId, ImageData, UploadedAt) "
                "VALUES (?, ?, ?, ?)",
                (image.id, image.user_id, image.image_data, image.uploaded_at)
            )
            conn.commit()
        return image.id  # Return the ID instead of a file path
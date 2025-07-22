from domain.entities import ChartImage
from domain.ports import ChartsRepositoryPort
import uuid

class UploadChartUseCase:
    def __init__(self, image_repo: ChartsRepositoryPort):
        self._image_repo = image_repo

    def execute(self, image_bytes: bytes, user_id: str) -> str:
        chart_image = ChartImage(
            id=str(uuid.uuid4()),
            user_id=user_id,
            image_data=image_bytes
        )
        return self._image_repo.save(chart_image)  # Returns image ID
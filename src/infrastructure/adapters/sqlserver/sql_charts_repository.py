from sqlalchemy import create_engine
from src.domain.ports.repositories.charts_repository import ChartsRepositoryPort
from src.domain.entities.chart_image import ChartImage
from sqlalchemy.orm import Session

class SqlChartsRepository(ChartsRepositoryPort):
    def __init__(self, session: Session):
        self._session = session

    def save(self, image: ChartImage) -> str:
        self._session.add(image)
        self._session.commit()
        return image.id
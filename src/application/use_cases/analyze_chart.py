from domain.entities import ChartAnalysis
from domain.ports import AnalysisRepositoryPort, ChartsRepositoryPort

class AnalyzeChartUseCase:
    def __init__(
        self, 
        charts_repo: ChartsRepositoryPort,
        analysis_repo: AnalysisRepositoryPort
    ):
        self._image_storage = charts_repo
        self._analysis_repo = analysis_repo

    def execute(self, image_bytes: bytes, question: str) -> ChartAnalysis:
        # 1. Store image
        image_id = self._image_storage.save(image_bytes)
        
        # 2. Call your multimodal model (mock or real)
        answer = "Mocked analysis result"  # Replace with model call
        
        # 3. Save analysis
        analysis = ChartAnalysis(
            id="generated_uuid",
            chart_image_id=image_id,
            question=question,
            answer=answer
        )
        self._analysis_repo.save_analysis(analysis)
        return analysis
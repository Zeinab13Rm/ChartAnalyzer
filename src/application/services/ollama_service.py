from ollama import Client
from src.application.ports.llm_service_port import LLMServicePort  # Your existing interface
from src.application.dtos.LLM import LLMRequestDTO, LLMResponseDTO
import json
class OllamaService(LLMServicePort):
    def __init__(self, host: str ):
        self.client = Client(host=host)
    
    async def analyze(self, request: LLMRequestDTO) -> LLMResponseDTO:
        data = {
            "Telecom": "Telecom",
            "title": "Barclength = value amount",
            "source": "chat.com",
            "x_title": "Scale",
            "y_title": "None",
            "values": {
                "Data Set 1": {
                    "Category B": "3.4",
                    "Category A": "4.7",
                    "Category A Telecom": "4.9",
                    "Category A Telecom Duplicate": "4.2"  # Fixed duplicate key
                },
                "Data Set 2": {
                    "Category B": "2.6",
                    "Category A": "5.8",
                    "Category A Duplicate": "4.5",  # Fixed duplicate key
                    "Category A Duplicate 2": "4.0"  # Fixed duplicate key
                },
                "Data Set 3": {
                    "Category B": "2.9",
                    "Category A": "3.8",
                    "Category A Duplicate": "3.7",  # Fixed duplicate key
                    "Category A Duplicate 2": "3.9"  # Fixed duplicate key
                }
            }
        }

        # To convert to string:

        data_string = json.dumps(data, indent=4)

        response = self.client.chat(
            model="llava:34b",  # or "chartgemma" if available
            messages=[{
                "role": "user",
                "content": f"having this python dictionary : {data_string} ,Analyze this chart (do not mention any python dictionary in your answer) : {request.question}\n"
            }]
        )
        return LLMResponseDTO(
            answer=response['message']['content'],
            model_used="llava:34b",
            processing_time=response.get('total_duration')
        )
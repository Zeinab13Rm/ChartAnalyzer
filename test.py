# 1. Install required package
# pip install huggingface-hub

# 2. Import and initialize
from huggingface_hub import InferenceClient
import base64
import requests

# 1. Convert image to base64
with open("/home/zeinabrm/Pictures/Screenshots/Screenshot from 2025-02-17 22-46-46.png", "rb") as image_file:
    base64_image = base64.b64encode(image_file.read()).decode('utf-8')

# 2. Prepare payload
headers = {
    "Authorization": f"Bearer REPLACED",
    "Content-Type": "application2/json"
}

payload = {
    "inputs": f"<image>{base64_image}</image>\nQuestion: What does this chart show?\nAnswer:",
    "parameters": {"max_new_tokens": 200}
}

# 3. Manually call the API
response = requests.post(
    "https://api-inference.huggingface.co/yuan-tian/chartgpt-llama3",
    headers=headers,
    json=payload
)
print(f"Status Code: {response.status_code}")
print(f"Raw Response: {response.text}")
print(response.json())
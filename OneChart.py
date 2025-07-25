from transformers import AutoTokenizer
from PIL import Image
import onnxruntime as ort
import numpy as np
import requests

# Download tokenizer only (very small)
tokenizer = AutoTokenizer.from_pretrained('kppkkp/OneChart', trust_remote_code=True)

# Load pre-converted ONNX model (you'll need to get/make this first)
onnx_session = ort.InferenceSession("onechart_model.onnx")

# Prepare inputs
image = Image.open("/home/zeinabrm/Documents/ChartToText/Project/ChartAnalyzer/multiset_barchart.png")
inputs = tokenizer("analyze this chart", return_tensors="np")
pixel_values = np.array(image.convert("RGB"))  # Simple image processing

# Run inference
outputs = onnx_session.run(
    None,
    {
        "input_ids": inputs["input_ids"],
        "attention_mask": inputs["attention_mask"],
        "pixel_values": np.expand_dims(pixel_values, 0)
    }
)

print(tokenizer.decode(outputs[0]))
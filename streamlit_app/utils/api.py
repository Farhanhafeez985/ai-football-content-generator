import os
from pathlib import Path
import requests
import json
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[2] / ".env")

API_TOKEN = os.getenv("API_TOKEN")

def stream_response(topic):
    headers = {
        'Authorization': f'Bearer {API_TOKEN}',
        'Content-Type': 'application/json'
    }
    response = requests.post(
        "http://127.0.0.1:8000/generate",
        json={
            "topic": topic
        },
        headers=headers,
        stream=True,
    )
    for line in response.iter_lines():

        if not line:
            continue

        if line.startswith(b"data: "):
            yield json.loads(line[6:])
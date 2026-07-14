import requests
import json
from app.config import settings

def stream_response(topic):
    headers = {
        'Authorization': f'Bearer {settings.API_TOKEN}',
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
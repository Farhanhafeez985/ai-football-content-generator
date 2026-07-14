import requests
import json
def stream_response(topic):
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c',
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
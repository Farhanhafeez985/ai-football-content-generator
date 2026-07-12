```markdown
# ⚽ AI Football Content Generator

An AI-powered content automation system that creates engaging football content for **TikTok, Instagram Reels, and YouTube Shorts**.

The system uses a **LangGraph multi-agent architecture** where a supervisor workflow coordinates specialized AI agents to automate:

- Football research
- Viral topic generation
- Short-form video script writing

---

## 🚀 Features

✅ AI-powered football research  
✅ Latest football news and trends using Tavily Search  
✅ Automated content idea generation  
✅ 60-second video script creation  
✅ LangGraph agent orchestration  
✅ Open-source LLM support using Ollama  
✅ Configurable LLM provider architecture  
✅ Ready for future RAG integration  

---

# 🏗️ Architecture

```

```
                User
                  |
                  ▼
          LangGraph Workflow
          (Supervisor)
                  |
    ┌─────────────┼─────────────┐
    ▼             ▼             ▼
    Research      Topic         Script
    Agent         Agent         Agent
    └─────────────┼─────────────┘
                  |
                  |
                  |
                  ▼
              Final Result

```

---

# 🤖 Agents

## 1. Research Agent

Responsible for collecting football information.

### Input

```

Football topic

```

### Uses

- Tavily Search API
- LLM summarization

### Output

- Latest news
- Statistics
- Historical facts
- Trending stories

---

## 2. Topic Agent

Transforms research into engaging short-form content ideas.

### Input

```

Research summary

```

### Output

3-5 viral content ideas optimized for:

- TikTok
- Instagram Reels
- YouTube Shorts

---

## 3. Script Agent

Creates a complete short-form video script.

### Input

```

Selected content idea

````

### Output

```json
{
  "hook": "",
  "body": "",
  "ending": "",
  "cta": ""
}
````

---

# 🔄 Workflow

```
START
 |
 ▼
Research Agent
 |
 ▼
Topic Agent
 |
 ▼
Script Agent
 |
 ▼
END
```

LangGraph controls the workflow execution and agent communication.

---

# 🛠️ Tech Stack

## Backend

* Python
* FastAPI

## AI Framework

* LangChain
* LangGraph

## LLM

Current:

* Ollama
* Open-source models

Supported architecture for:

* OpenAI GPT
* Google Gemini
* Anthropic Claude

Switching models only requires configuration changes.

---

## Tools

### Web Search

* Tavily API

Used by the Research Agent for real-time football information.

---

# 📂 Project Structure

```
app/
│
├── agents/
│   ├── base.py
│   ├── research.py
│   ├── topic.py
│   └── script.py
│
├── api/
│   └── auth.py
│
├── config/
│   └── settings.py
│
├── graph/
│   ├── state.py
│   ├── nodes.py
│   └── workflow.py
│
├── prompts/
│   ├── research.txt
│   ├── topic.txt
│   └── script.txt
│
├── tools/
│   └── tavily_search.py
│
├── llm.py
└── main.py
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone <repository-url>

cd ai-football-content-generator
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

### Mac/Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create `.env`

```env
LLM_PROVIDER=ollama

OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=qwen3:8b

TAVILY_API_KEY=your_api_key

API_TOKEN=your_secret_token
```

---

# 🧠 Running Locally

Start Ollama:

```bash
ollama serve
```

Pull model:

```bash
ollama pull qwen3:8b
```

Start API:

```bash
uvicorn app.main:app --reload
```

API:

```
http://localhost:8000
```

Swagger:

```
http://localhost:8000/docs
```

---

# 🔌 API Example

## Generate Content

### Request

```
POST /generate
```

Headers:

```
Authorization: Bearer your_secret_token
```

Body:

```json
{
  "topic": "Cristiano Ronaldo career story"
}
```

Response:

```json
{
  "success": true,
  "data": {
    "research": "...",
    "ideas": "...",
    "script": {
      "hook": "...",
      "body": "...",
      "ending": "...",
      "cta": "..."
    }
  }
}
```

---

# 🔮 Future Improvements

## Database & RAG

Currently:

* No database

Future:

* Neo4j Vector Database
* Football knowledge graph
* RAG pipeline
* Semantic search

---

## Content Automation

Future plans:

* AI voice generation
* Video generation
* Automatic captions
* Social media publishing automation

---

# 🎯 Project Goals

This project demonstrates:

* AI agent development
* LLM integration
* Prompt engineering
* LangGraph orchestration
* Tool calling
* Production-ready AI architecture

---

## 📄 License

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for details.
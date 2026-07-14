# ⚽ AI Football Studio

An AI-powered multi-agent content automation platform that researches football topics, generates viral content ideas, writes engaging short-form scripts, evaluates script quality, and streams the entire workflow in real time.

Built with **LangGraph**, **FastAPI**, **Streamlit**, and **Open-Source LLMs**.

---

## ✨ Features

- 🤖 Multi-Agent AI workflow using LangGraph
- 🔍 Football research with real-time web search
- 💡 AI-powered viral topic generation
- ✍️ Short-form video script generation
- 🧐 Automated script quality evaluation
- 🔄 Intelligent retry loop for script improvement
- ⚡ Real-time workflow streaming (Server-Sent Events)
- 🎨 Modern Streamlit AI Studio interface
- 🔐 Token-protected REST API
- 🦙 Open-source LLM support via Ollama
- 🔧 Easily switch between different LLM providers

---

# 🏗 Architecture

```text
                      User
                        │
                        ▼
              FastAPI Streaming API
                        │
                        ▼
             LangGraph Supervisor Agent
                        │
      ┌─────────────────┼─────────────────┐
      ▼                 ▼                 ▼
 Research Agent   Topic Generator   Script Writer
                                           │
                                           ▼
                                   Script Evaluator
                                           │
                        ┌──────────────────┴─────────────────┐
                        │                                    │
                  Quality Good                        Quality Poor
                        │                                    │
                        ▼                                    │
                 Stream Final Result                Retry Script Generation
                                                     (Max Retry Limit)
```

---

# 🤖 AI Agents

## 🔍 Research Agent

Collects accurate football information using external search tools.

### Responsibilities

- Latest football news
- Historical facts
- Statistics
- Trending stories
- Source collection

---

## 💡 Topic Generator

Converts research into engaging short-form content ideas optimized for social media.

Output:

- Viral hooks
- Story ideas
- Educational topics
- Comparison videos

---

## ✍️ Script Writer

Generates a structured short-form script.

```json
{
  "hook": "",
  "body": "",
  "ending": "",
  "cta": ""
}
```

---

## 🧐 Script Evaluator

Reviews every generated script.

Checks:

- Quality
- Clarity
- Engagement
- Flow
- Completeness

If the script quality is poor, feedback is automatically sent back to the Script Writer for regeneration.

---

# 🔄 Workflow

```text
START
   │
   ▼
Research Agent
   │
   ▼
Topic Generator
   │
   ▼
Script Writer
   │
   ▼
Script Evaluator
   │
   ├────────────── Good ─────────────► Finish
   │
   └────────────── Poor ─────────────► Retry Script
                                          │
                                          ▼
                                   Script Writer
```

The Supervisor Agent automatically decides which agent should execute next based on the current workflow state.

---

# ⚡ Live Streaming

The backend streams every workflow event to the frontend using **Server-Sent Events (SSE)**.

Example:

```
Research Complete
↓

Topic Ideas Generated
↓

Writing Script...
↓

Evaluating Script...

↓

Retrying Script...
↓

Script Approved
```

The Streamlit frontend updates each agent card in real time.

---

# 🎨 AI Studio Interface

The project includes a modern Streamlit interface inspired by ChatGPT.

Features include:

- Sidebar chat history
- Live agent status updates
- Streaming workflow progress
- Expandable agent cards
- Real-time script generation
- Evaluation feedback
- Dark theme UI

---

# 🛠 Tech Stack

## Backend

- Python
- FastAPI

## AI

- LangChain
- LangGraph

## Frontend

- Streamlit

## LLM

Current

- Ollama

Supported

- OpenAI
- Anthropic Claude
- Google Gemini
- Local OpenAI-compatible APIs

---

# 🔧 AI Tools

### Custom Tavily Search Tool

Used by the Research Agent for real-time football information.

Capabilities:

- Latest news
- Statistics
- Football events
- Reliable sources

---

# 📁 Project Structure

```text
app/
│
├── agents/
│
├── graph/
│   ├── workflow.py
│   ├── nodes.py
│   ├── state.py
│   └── supervisor.py
│
├── prompts/
│
├── tools/
│
├── llm.py
└── main.py

streamlit_app/
│
├── app.py
├── assets/
├── components/
├── utils/
```

---

# ⚙ Installation

```bash
git clone https://github.com/yourusername/ai-football-studio.git

cd ai-football-studio
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate

Mac/Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env`

```env
LLM_PROVIDER=ollama

OLLAMA_BASE_URL=http://localhost:11434

OLLAMA_MODEL=qwen3:8b

TAVILY_API_KEY=xxxxxxxx

API_TOKEN=xxxxxxxx
```

---

# 🚀 Running the Project

Start Ollama

```bash
ollama serve
```

Pull a model

```bash
ollama pull qwen3:8b
```

Run the FastAPI backend

```bash
uvicorn app.main:app --reload
```

Run the Streamlit frontend

```bash
streamlit run streamlit_app/app.py
```

---

# 📡 REST API

### Generate Content

```
POST /generate
```

Authorization

```
Bearer <API_TOKEN>
```

Example

```json
{
  "topic": "Lionel Messi Career Story"
}
```

The endpoint streams progress updates until the workflow finishes.

---

# 🚧 Roadmap

Upcoming features

- 🎙 AI voice generation
- 🎥 AI video generation
- 🖼 Automatic thumbnail generation
- 📱 Social media publishing
- 📊 Analytics dashboard
- 🧠 Football RAG knowledge base
- 🕸 Neo4j knowledge graph
- 📰 Multi-source research
- 🎬 Multi-language content generation

---

# 🎯 What This Project Demonstrates

- Multi-Agent AI Systems
- LangGraph Workflows
- Supervisor-Based Agent Orchestration
- Streaming AI Applications
- Prompt Engineering
- Tool Calling
- Structured Outputs
- Retry Mechanisms
- FastAPI Backend Development
- Modern Streamlit UI
- Production-Oriented AI Architecture

---

## 📄 License

Licensed under the MIT License.
See the [LICENSE](LICENSE) file for details.
# ⚽ AI Football Studio

An AI-powered multi-agent content automation platform that researches football topics, generates viral content ideas, writes engaging short-form scripts, evaluates script quality, generates AI voiceovers, and streams the entire workflow in real time.

Built with **LangGraph**, **FastAPI**, **Streamlit**, **Deepgram**, and **Open-Source LLMs**.

---

# ✨ Features

- 🤖 Multi-Agent AI workflow powered by LangGraph
- 🧠 Intelligent Supervisor Agent orchestration
- 🔍 Football research with real-time web search
- 💡 AI-powered viral content idea generation
- ✍️ Structured short-form video script generation
- 🧐 Automated script quality evaluation
- 🔄 Intelligent retry loop for script improvement
- 🎙️ AI voice generation using Deepgram Aura TTS
- ⚡ Real-time workflow streaming with Server-Sent Events (SSE)
- 🎨 Modern  Streamlit interface
- 🔐 Token-protected REST API
- 🦙 Configurable LLM provider architecture
- 🔧 Easy switching between Ollama, Groq, OpenAI, and Gemini

---

# 🏗️ Architecture

```text
                        User
                          │
                          ▼
                FastAPI Streaming API
                          │
                          ▼
               LangGraph Supervisor Agent
                          │
      ┌───────────────────┼───────────────────┐
      ▼                   ▼                   ▼
 Research Agent    Topic Generator     Script Writer
                                             │
                                             ▼
                                     Script Evaluator
                                             │
                    ┌────────────────────────┴────────────────────────┐
                    │                                                 │
              Quality Poor                                     Quality Good
                    │                                                 │
                    ▼                                                 ▼
           Retry Script Generation                           Voice Generator
             (Max Retry Limit)                                    │
                    ▲                                              ▼
                    └──────────────────────────────►      Deepgram Aura TTS
                                                         │
                                                         ▼
                                                    MP3 Audio Output
```

---

# 🤖 AI Agents

## 🔍 Research Agent

Collects accurate football information using real-time search tools.

### Responsibilities

- Latest football news
- Historical facts
- Match statistics
- Trending stories
- Source collection

---

## 💡 Topic Generator

Transforms research into engaging short-form content ideas optimized for:

- TikTok
- Instagram Reels
- YouTube Shorts

Output includes:

- Viral hooks
- Story ideas
- Educational content
- Comparison videos

---

## ✍️ Script Writer

Generates a structured short-form video script.

```json
{
  "hook": "",
  "body": "",
  "ending": "",
  "cta": "",
  "narration": ""
}
```

The `narration` field is a natural voice-over version of the structured script and is consumed directly by the Voice Generator.

---

## 🧐 Script Evaluator

Reviews every generated script.

### Checks

- Content quality
- Clarity
- Engagement
- Flow
- Completeness

If the quality is poor, feedback is automatically sent back to the Script Writer for regeneration until the maximum retry limit is reached.

---

## 🎙️ Voice Generator

Converts the approved narration into natural speech.

### Responsibilities

- Generate AI voice using Deepgram Aura TTS
- Convert narration into MP3
- Return audio path for downstream processing

### Output

```text
outputs/audio/script.mp3
```

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
   ├────────────── Poor ─────────────► Retry Script
   │                                      │
   │                                      ▼
   │                               Script Writer
   │
   └────────────── Good ─────────────► Voice Generator
                                             │
                                             ▼
                                      Deepgram Aura TTS
                                             │
                                             ▼
                                           Finish
```

The Supervisor Agent dynamically determines which agent should execute next based on the current workflow state.

---

# ⚡ Live Streaming

The backend streams every workflow event to the frontend using **Server-Sent Events (SSE)**.

Example workflow:

```text
🔍 Research Complete

↓

💡 Topic Ideas Generated

↓

✍️ Writing Script...

↓

🧐 Evaluating Script...

↓

🔄 Retrying Script...

↓

✅ Script Approved

↓

🎙️ Generating Voice...

↓

🎧 Voice Ready
```

The Streamlit frontend updates each agent card in real time as the workflow progresses.

---

# 🎨 AI Studio Interface

The project includes a modern ChatGPT-inspired interface built with Streamlit.

### Features

- 💬 Chat-style conversation interface
- 📂 Sidebar conversation history
- ⚡ Live workflow streaming
- 🤖 Expandable AI agent cards
- 📊 Real-time workflow status
- 🔄 Retry progress visualization
- 🎙️ Voice generation status
- 🌙 Modern dark theme UI

---

# 🛠️ Tech Stack

## Backend

- Python
- FastAPI

## AI Framework

- LangChain
- LangGraph

## Frontend

- Streamlit

## LLM Providers

Current

- Ollama

Supported

- OpenAI
- Anthropic Claude
- Google Gemini
- Groq
- Local OpenAI-Compatible APIs

---

# 🔧 AI Tools

## Tavily Search

Used by the Research Agent.

Capabilities

- Latest football news
- Match statistics
- Historical facts
- Trending stories
- Reliable sources

---

## Deepgram Aura TTS

Used by the Voice Generator.

Capabilities

- Natural AI voice generation
- MP3 audio output
- Multiple voice models
- Production-quality narration

---

# 📁 Project Structure

```text
app/
│
├── agents/
│   ├── base.py
│   ├── research.py
│   ├── topic.py
│   ├── script.py
│   ├── evaluator.py
│   ├── supervisor.py
│   └── voice.py
│
├── api/
│
├── config/
│
├── graph/
│   ├── workflow.py
│   ├── nodes.py
│   ├── state.py
│   └── supervisor.py
│
├── prompts/
│   ├── research.txt
│   ├── topic.txt
│   ├── script.txt
│   ├── evaluator.txt
│   └── supervisor.txt
│
├── schemas/
│
├── tools/
│   ├── tavily_search.py
│   └── deepgram_tts.py
│
├── llm.py
└── main.py

streamlit_app/
│
├── app.py
├── assets/
├── components/
└── utils/
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/ai-football-studio.git

cd ai-football-studio
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file.

```env
LLM_PROVIDER=ollama

OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=qwen3:8b

GROQ_API_KEY=xxxxxxxx

OPENAI_API_KEY=xxxxxxxx

GEMINI_API_KEY=xxxxxxxx

TAVILY_API_KEY=xxxxxxxx

DEEPGRAM_API_KEY=xxxxxxxx

API_TOKEN=xxxxxxxx
```

---

# 🚀 Running the Project

Start Ollama

```bash
ollama serve
```

Pull your model

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

## Generate Content

```
POST /generate
```

Authorization

```
Bearer <API_TOKEN>
```

Example Request

```json
{
  "topic": "Lionel Messi Career Story"
}
```

The endpoint streams workflow progress until completion using **Server-Sent Events (SSE)**.

Example streamed event

```json
{
    "node": "research",
    "status": "🔍 Research Complete",
    "data": {}
}
```

```json
{
    "node": "voice",
    "status": "🎙️ Voice Generated",
    "data": {
        "audio_path": "outputs/audio/script.mp3"
    }
}
```

# 🎯 What This Project Demonstrates

- Multi-Agent AI Systems
- LangGraph Workflows
- Supervisor-Based Agent Orchestration
- Streaming AI Applications (SSE)
- Prompt Engineering
- Tool Calling
- Structured LLM Outputs
- Intelligent Retry Mechanisms
- AI Voice Generation
- FastAPI Backend Development
- Modern Streamlit UI
- Production-Oriented AI Architecture

---

## 📄 License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE) file for details.
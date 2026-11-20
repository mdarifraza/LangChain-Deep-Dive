# 🦜 LangChain Learning Journey

### 🚀 Generative AI using LangChain — From Fundamentals to AI Agents

A **hands-on learning repository** documenting my journey of learning and implementing **LangChain** for building modern **Generative AI applications**.

This repository contains my **notes, Python implementations, experiments, practical examples, and projects** based on the **Generative AI using LangChain** playlist by **CampusX**.

> **Learn → Implement → Experiment → Build**

---

## 📌 About This Repository

The goal of this repository is not just to collect theoretical notes, but to **understand how LangChain works internally and implement its core components using Python**.

Throughout this journey, I am exploring how LLMs can be connected with:

- 🧠 Language Models
- 📝 Prompts
- 🔄 Chains & Runnables
- 📄 Documents
- 🔍 Retrievers
- 🗄️ Vector Stores
- 📚 RAG Pipelines
- 🛠️ Tools
- 🤖 AI Agents
- 📞 Tool Calling
- 🦙 Local LLMs with Ollama

The repository will continuously evolve as I learn and build more advanced Generative AI applications.

---

## 🎯 Learning Objectives

By completing this learning journey, my objectives are to:

- Understand the architecture and ecosystem of LangChain
- Work with different LLM and chat model integrations
- Design reusable prompt templates
- Generate structured outputs from LLMs
- Understand LangChain's Runnable architecture and LCEL
- Build chains and composable workflows
- Load and process different types of documents
- Implement text splitting strategies
- Work with embeddings and vector stores
- Build Retrieval-Augmented Generation (RAG) applications
- Implement tools and tool calling
- Understand and build AI agents
- Work with local LLMs using Ollama
- Apply these concepts to real-world GenAI applications

---

# 🗺️ Learning Roadmap

## 01. 🧭 GenAI & LangChain Introduction

- Generative AI roadmap
- Introduction to LangChain
- Why LangChain?
- LangChain ecosystem
- Basic architecture
- LLM application development

---

## 02. 🧩 LangChain Components

Understanding the major building blocks of LangChain:

- Models
- Prompts
- Output Parsers
- Chains
- Runnables
- Retrievers
- Tools
- Agents

---

## 03. 🧠 LangChain Models

Working with different types of models:

- Language Models
- Chat Models
- Open-source models
- Model APIs
- Model configuration
- Embedding Models
- Practical model integration

---

## 04. ✍️ Prompts

Understanding prompt engineering inside LangChain:

- Prompt Templates
- Dynamic prompts
- Chat Prompt Templates
- System / Human / AI messages
- Prompt variables
- Reusable prompts
- Prompt composition

---

## 05. 📦 Structured Output

Working with reliable and structured LLM responses:

- Structured responses
- Output schemas
- Pydantic models
- JSON outputs
- Structured generation
- Type-safe LLM responses

---

## 06. 🔎 Output Parsers

Understanding how to process LLM outputs:

- Output parsing
- String output parsing
- Structured output parsing
- JSON parsing
- Pydantic parsing
- Converting LLM responses into usable application data

---

## 07. 🔗 Chains

Building multi-step LLM workflows:

- What are chains?
- Sequential workflows
- Combining components
- Chain composition
- Reusable workflows
- Practical chain implementations

---

## 08. ⚡ Runnables & LCEL

Understanding LangChain's Runnable architecture:

- Runnable
- RunnableSequence
- RunnableParallel
- RunnablePassthrough
- RunnableLambda
- RunnableMap
- LCEL
- Composable pipelines

---

## 09. 📄 Document Loaders

Working with external data:

- Document loading
- Text files
- PDFs
- Web pages
- CSV files
- Different document sources
- Document objects

---

## 10. ✂️ Text Splitters

Preparing documents for retrieval:

- Why chunking is required
- Character-based splitting
- Recursive character splitting
- Chunk size
- Chunk overlap
- Metadata handling
- Chunking strategies

---

## 11. 🗄️ Vector Stores

Understanding semantic search infrastructure:

- Embeddings
- Vector representations
- Vector databases
- Similarity search
- Document indexing
- Storing embeddings
- Retrieving relevant documents

---

## 12. 🔍 Retrievers

Understanding retrieval systems:

- Retriever concept
- Vector store retrievers
- Similarity search
- Top-K retrieval
- Retrieval pipelines
- Retriever configuration

---

# 13. 📚 Retrieval-Augmented Generation (RAG)

Building applications that combine external knowledge with LLMs.

### RAG Pipeline

```text
Documents
    ↓
Document Loader
    ↓
Text Splitting
    ↓
Embeddings
    ↓
Vector Store
    ↓
Retriever
    ↓
Relevant Context
    ↓
LLM
    ↓
Final Answer
```

Topics covered:

- What is RAG?
- Why RAG?
- RAG architecture
- Retrieval process
- Context injection
- Question answering
- Building RAG applications

---

# 14. ▶️ YouTube Chatbot

Building a practical RAG application that can interact with YouTube content.

### Conceptual Architecture

```text
YouTube Video
      ↓
Transcript
      ↓
Document Processing
      ↓
Text Splitting
      ↓
Embeddings
      ↓
Vector Store
      ↓
Retriever
      ↓
LLM
      ↓
User Question
      ↓
Answer
```

This project demonstrates how LangChain can be used to build a **knowledge-grounded conversational application**.

---

# 15. 🛠️ Tools

Understanding how LLM applications interact with external capabilities.

Topics include:

- What are tools?
- Custom tools
- Tool schemas
- Tool integration
- Tool execution
- Using tools with LLMs

---

# 16. 📞 Tool Calling

Understanding how modern LLMs decide when and how to use external tools.

### Basic Flow

```text
User Query
     ↓
LLM
     ↓
Tool Selection
     ↓
Tool Execution
     ↓
Tool Result
     ↓
LLM
     ↓
Final Response
```

Topics include:

- Tool calling
- Function calling
- Tool schemas
- Arguments
- Tool execution
- LLM + external capabilities

---

# 17. 🤖 AI Agents

Building autonomous LLM-powered systems.

Topics include:

- What is an AI Agent?
- Agent architecture
- Reasoning + Action
- Tools + LLMs
- Agent execution
- Multi-step task solving
- Building an end-to-end AI Agent

### Agent Workflow

```text
User
  ↓
Agent
  ↓
Reason
  ↓
Select Tool
  ↓
Execute Tool
  ↓
Observe Result
  ↓
Reason Again
  ↓
Final Answer
```

---

# 18. 🦙 Ollama & Local LLMs

Exploring local LLM execution using Ollama.

Topics include:

- What is Ollama?
- Running LLMs locally
- Local model inference
- Model management
- Connecting local LLMs with applications
- Using local models in GenAI workflows

---

# 🧰 Tech Stack

| Technology | Purpose |
|---|---|
| 🐍 Python | Programming Language |
| 🦜 LangChain | LLM Application Framework |
| 🤗 Hugging Face | Open-source Models |
| 🧠 LLMs | Generative AI |
| 📚 RAG | Knowledge-grounded Generation |
| 🔢 Embeddings | Semantic Representation |
| 🗄️ Vector Stores | Semantic Search |
| 🛠️ Tools | External Capabilities |
| 🤖 AI Agents | Autonomous Workflows |
| 🦙 Ollama | Local LLMs |
| 🐙 Git & GitHub | Version Control |

---



---

# 📊 Learning Progress

| # | Topic | Status |
|---|---|:---:|
| 01 | GenAI & LangChain Introduction | ⬜ |
| 02 | LangChain Components | ⬜ |
| 03 | LangChain Models | ⬜ |
| 04 | Prompts | ⬜ |
| 05 | Structured Output | ⬜ |
| 06 | Output Parsers | ⬜ |
| 07 | Chains | ⬜ |
| 08 | Runnables & LCEL | ⬜ |
| 09 | Document Loaders | ⬜ |
| 10 | Text Splitters | ⬜ |
| 11 | Vector Stores | ⬜ |
| 12 | Retrievers | ⬜ |
| 13 | RAG | ⬜ |
| 14 | YouTube Chatbot | ⬜ |
| 15 | Tools | ⬜ |
| 16 | Tool Calling | ⬜ |
| 17 | AI Agents | ⬜ |
| 18 | Ollama | ⬜ |

> 🔄 I will update the progress as I complete each topic.

---

# 🧪 Learning Methodology

For every topic, I follow a practical learning process:

```text
📖 Understand the Concept
          ↓
🧠 Understand the Architecture
          ↓
💻 Implement with Python
          ↓
🧪 Experiment & Modify
          ↓
🌎 Apply to a Real-World Use Case
          ↓
📝 Document the Learning
          ↓
🚀 Build a Project
```

The focus is on **hands-on implementation rather than passive learning**.

---

# 💡 Key Concepts I'm Building

This repository gradually connects individual LangChain components into complete GenAI systems.

```text
LLM
 │
 ├── Prompts
 │
 ├── Structured Output
 │
 ├── Chains
 │
 ├── Runnables
 │
 ├── Documents
 │      ↓
 │   Embeddings
 │      ↓
 │   Vector Store
 │      ↓
 │   Retriever
 │      ↓
 │      RAG
 │
 ├── Tools
 │      ↓
 │   Tool Calling
 │      ↓
 │    Agents
 │
 └── Local LLMs
        ↓
      Ollama
```

---

# 🚀 Projects

As I progress through the course, I will convert the concepts into practical projects.

### Planned Projects

- 📚 Document Q&A System
- ▶️ YouTube Q&A Chatbot
- 🔍 Semantic Search Application
- 🤖 Tool-Using AI Agent
- 🧠 RAG-based AI Assistant
- 🦙 Local LLM Application

Projects will be added with their own documentation, architecture, setup instructions, and implementation.

---

# 📚 Learning Resource

This repository follows the **Generative AI using LangChain** playlist by **CampusX**.

🔗 **[Generative AI using LangChain — CampusX](https://www.youtube.com/playlist?list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0)**

The playlist currently contains **21 videos with approximately 21 hours and 53 minutes of content**.

---

# 🔐 API Keys & Environment Variables

Some implementations may require API keys.

**Never commit API keys directly to GitHub.**

Use a `.env` file:

```env
OPENAI_API_KEY=your_api_key
GROQ_API_KEY=your_api_key
HUGGINGFACEHUB_API_TOKEN=your_token
```

And add `.env` to `.gitignore`:

```gitignore
.env
__pycache__/
*.pyc
.ipynb_checkpoints/
venv/
.venv/
```

---

# 🧠 What I Want to Build Next

After completing this learning journey, my goal is to move toward:

```text
LangChain
    ↓
Advanced RAG
    ↓
AI Agents
    ↓
LangGraph
    ↓
Agentic AI
    ↓
Production AI Systems
```

The ultimate goal is to build **reliable, scalable, and production-oriented Generative AI applications**.

---

# 👨‍💻 About Me

### Md Arif Raza

**AI/ML Engineer | Generative AI | Agentic AI**

I am focused on building practical AI systems using:

`Python` • `Machine Learning` • `Deep Learning` • `LLMs` • `RAG` • `LangChain` • `LangGraph` • `Agentic AI`

I enjoy learning by building projects and experimenting with modern AI technologies.

---

## 🔗 Connect With Me

- 💼 LinkedIn: [Md Arif Raza](https://www.linkedin.com/in/md-arif-raza-a599a2290/)
- 🐙 GitHub: [mdarifraza](https://github.com/mdarifraza)

---

## ⭐ Support

If you find this repository useful, feel free to ⭐ **Star** the repository.

If you have suggestions or improvements, feel free to open an **Issue** or **Pull Request**.

---

### 📌 Disclaimer

This repository is created for **educational and practical learning purposes**.

The concepts are learned from publicly available resources and are independently implemented and experimented with as part of my learning journey.

---

### 🚀 Keep Learning. Keep Building. Keep Shipping.

> **“Don't just learn AI. Build with AI.”**
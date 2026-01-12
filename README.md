# 🤖 Agentic-AI

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

> My experiments with Agentic AI - Building intelligent, autonomous agents that can reason, plan, and execute tasks

## 📋 Overview

This repository contains a collection of experimental projects exploring the capabilities of **Agentic AI** - autonomous systems powered by Large Language Models (LLMs) that can understand context, make decisions, use tools, and execute complex workflows.

Agentic AI represents a paradigm shift from simple chatbots to intelligent systems that can:
- 🧠 **Reason** about problems and plan solutions
- 🔧 **Use tools** and APIs to accomplish tasks
- 💾 **Remember** previous interactions and context
- 🎯 **Execute** multi-step workflows autonomously
- 🔄 **Learn** from feedback and adapt behavior

## 🚀 Projects

### 1. **LLM_call_simple.py**
Basic integration with OpenAI's API demonstrating fundamental LLM interactions.

**Features:**
- Simple API call structure
- Environment-based API key management
- Error handling for API requests
- Model selection (GPT-4o-mini, GPT-4.1)

**Use Case:** Starting point for understanding LLM API interactions

---

### 2. **LLM_simple_loop.py**
Interactive conversational loop with an LLM, enabling multi-turn dialogues.

**Features:**
- Continuous conversation loop
- User input handling
- Conversation history management
- Context preservation across turns

**Use Case:** Building basic chatbot interfaces and conversational AI

---

### 3. **Simple_Agent.py**
Introduction to agent patterns with basic tool usage and decision-making capabilities.

**Features:**
- Agent-based architecture
- Tool calling mechanisms
- Basic reasoning loops
- Task decomposition

**Use Case:** Understanding core agent design patterns

---

### 4. **Agent_with_memory.py**
Enhanced agent with persistent memory capabilities for context-aware interactions.

**Features:**
- Long-term memory storage
- Context retrieval and injection
- Conversation state management
- Memory-augmented decision making

**Use Case:** Building agents that learn from past interactions and maintain context

---

### 5. **Email-AutomationAgent.py**
Practical automation agent for email-related tasks.

**Features:**
- Email processing and analysis
- Automated response generation
- Task extraction from emails
- Workflow automation

**Use Case:** Automating email workflows, triaging, and intelligent responses

## 🛠️ Technology Stack

- **Python 3.8+**
- **OpenAI API** - For LLM capabilities
- **LangChain** (likely) - Agent orchestration framework
- **Environment Variables** - Secure API key management

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- OpenAI API key
- pip package manager

### Setup

1. **Clone the repository:**
```bash
git clone https://github.com/nipunbnair/Agentic-AI-.git
cd Agentic-AI-
```

2. **Install dependencies:**
```bash
pip install openai python-dotenv
# Add other dependencies as needed
```

3. **Set up environment variables:**

Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your_api_key_here
```

Or export directly:
```bash
export OPENAI_API_KEY='your_api_key_here'
```

## 🎯 Usage

### Running Individual Scripts

**Simple LLM Call:**
```bash
python LLM_call_simple.py
```

**Interactive Loop:**
```bash
python LLM_simple_loop.py
```

**Basic Agent:**
```bash
python Simple_Agent.py
```

**Agent with Memory:**
```bash
python Agent_with_memory.py
```

**Email Automation:**
```bash
python Email-AutomationAgent.py
```

## 📚 Key Concepts

### What is an Agentic System?

An **agentic system** is an AI architecture that goes beyond simple input-output models:

1. **Autonomy** - Can operate independently with minimal human intervention
2. **Goal-Oriented** - Works towards specific objectives
3. **Tool Use** - Leverages external APIs, databases, and services
4. **Planning** - Decomposes complex tasks into actionable steps
5. **Memory** - Maintains context and learns from interactions
6. **Adaptation** - Adjusts behavior based on feedback and outcomes

### Agent Design Patterns

This repository explores several agent patterns:

- **ReAct** (Reasoning + Acting) - Interleaves reasoning and action
- **Plan-and-Execute** - Plans entire workflows before execution
- **Tool-Augmented** - Extends capabilities through external tools
- **Memory-Enhanced** - Uses persistent storage for context

## 🔧 Configuration

### Model Selection

You can configure which LLM model to use:

```python
model_id = "gpt-4o-mini"    # Fast and cost-effective
# model_id = "gpt-4o"       # Higher quality, slower
# model_id = "gpt-4-turbo"  # Balanced performance
```

### API Parameters

Common parameters to adjust:

```python
response = client.chat.completions.create(
    model=model_id,
    messages=[...],
    max_tokens=1024,        # Response length
    temperature=0.7,        # Creativity (0-2)
    top_p=1.0,             # Nucleus sampling
)
```

## 🎓 Learning Path

If you're new to Agentic AI, follow this progression:

1. **Start with `LLM_call_simple.py`** - Understand basic API interactions
2. **Move to `LLM_simple_loop.py`** - Learn conversation management
3. **Explore `Simple_Agent.py`** - Grasp agent patterns
4. **Study `Agent_with_memory.py`** - Add persistent context
5. **Analyze `Email-AutomationAgent.py`** - See real-world application

## 🌟 Use Cases

Agentic AI systems are transforming various domains:

- **💼 Business Automation** - Email processing, document analysis, workflow automation
- **📊 Data Analysis** - Autonomous research, report generation, insights extraction
- **👨‍💻 Software Development** - Code generation, debugging, testing automation
- **📝 Content Creation** - Writing assistance, research, content curation
- **🎯 Personal Assistants** - Task management, scheduling, information retrieval
- **🔍 Research** - Literature review, data synthesis, hypothesis generation

## 🔐 Security & Best Practices

### API Key Management
- ✅ **DO** use environment variables for API keys
- ✅ **DO** add `.env` to `.gitignore`
- ❌ **DON'T** commit API keys to version control
- ❌ **DON'T** hardcode sensitive information

### Cost Management
- Monitor token usage and API costs
- Set `max_tokens` limits appropriately
- Use cheaper models (gpt-4o-mini) for development
- Implement rate limiting for production

### Error Handling
```python
try:
    response = client.chat.completions.create(...)
except Exception as e:
    print(f"Error: {e}")
    # Implement retry logic or fallback
```

## 🤝 Contributing

Contributions are welcome! Whether it's:
- 🐛 Bug fixes
- ✨ New agent patterns
- 📚 Documentation improvements
- 💡 Experimental features

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingAgent`)
3. Commit your changes (`git commit -m 'Add amazing agent'`)
4. Push to the branch (`git push origin feature/AmazingAgent`)
5. Open a Pull Request

## 📖 Resources

### Learning Materials
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction)
- [Anthropic's Introduction to Agentic AI](https://www.anthropic.com/research)
- [Building Effective Agents](https://lilianweng.github.io/posts/2023-06-23-agent/)

### Related Projects
- [LangChain](https://github.com/langchain-ai/langchain) - Agent orchestration framework
- [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) - Autonomous GPT-4 experiments
- [BabyAGI](https://github.com/yoheinakajima/babyagi) - Task-driven autonomous agent
- [CrewAI](https://github.com/joaomdmoura/crewAI) - Multi-agent collaboration

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Nipun B Nair**
- GitHub: [@nipunbnair](https://github.com/nipunbnair)

## 🙏 Acknowledgments

- OpenAI for providing powerful LLM APIs
- The open-source AI community for sharing knowledge and tools
- All contributors who help improve this repository

## 📬 Contact & Support

- **Issues:** [GitHub Issues](https://github.com/nipunbnair/Agentic-AI-/issues)
- **Discussions:** Share ideas and ask questions in GitHub Discussions

---

## 🗺️ Roadmap

Future experiments planned:

- [ ] Multi-agent collaboration systems
- [ ] Integration with vector databases (Pinecone, Weaviate)
- [ ] Advanced memory systems (RAG, knowledge graphs)
- [ ] Tool creation and custom function calling
- [ ] Web scraping and research agents
- [ ] Claude/Anthropic API integration
- [ ] AWS Bedrock integration for multi-model support
- [ ] Evaluation and testing frameworks
- [ ] Production deployment examples

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

*Building the future, one agent at a time* 🚀

</div>

# 🤖 AgentForge

### A Mini AI Agent Orchestration Framework Built with Python OOP

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Dependencies](https://img.shields.io/badge/Dependencies-Standard%20Library-success)](#-requirements)
[![Architecture](https://img.shields.io/badge/Architecture-Modular%20OOP-blueviolet)](#-architecture)
[![Status](https://img.shields.io/badge/Status-Portfolio%20Project-orange)](#-project-scope)

> **AgentForge** is a lightweight, modular framework for learning how agent-based systems can be structured using Python object-oriented programming.
>
> It models the core building blocks of an agent system — **messages, memory, tools, agents, routing, registries, logging, and pipelines** — without relying on external AI frameworks.

---

## ✨ Why AgentForge?

Many beginner AI projects stop at calling an API from a single Python file.

AgentForge takes a different approach: it focuses on the **software architecture behind agent systems**.

The project demonstrates how independent components can work together through:

- 🧩 **Composition** — agents contain memory and tools
- 🔌 **Abstraction** — common contracts for agents and tools
- 🔄 **Polymorphism** — different agents expose the same `run()` interface
- 🦆 **Duck typing** — compatible objects can participate without inheritance
- 🧠 **Memory management** — configurable conversation history
- 🛠️ **Tool integration** — calculator, text analysis, and simulated search
- 🚦 **Task routing** — route requests to specialized agents
- ⛓️ **Pipelines** — chain processing stages together
- 📋 **Registries** — dynamically register named components
- 📝 **Logging mixins** — reusable logging through multiple inheritance
- ⚙️ **Python magic methods** — make framework objects feel natural to use

The implementation is intentionally small so the underlying design is easy to inspect and explain.

---

## 🏗️ Architecture

```text
                         ┌──────────────────────┐
                         │      User Input      │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │     RouterAgent      │
                         │  Task Classification │
                         └──────────┬───────────┘
                                    │
                 ┌──────────────────┼──────────────────┐
                 ▼                  ▼                  ▼
          ┌────────────┐     ┌─────────────┐    ┌──────────────┐
          │ ChatAgent  │     │ AnalystAgent│    │ Other Agents │
          └─────┬──────┘     └──────┬──────┘    └──────────────┘
                │                   │
                ▼                   ▼
        ┌──────────────┐     ┌──────────────┐
        │    Tools     │     │    Memory    │
        ├──────────────┤     ├──────────────┤
        │ Calculator   │     │ Message      │
        │ Text Analyzer│     │ History      │
        │ Search       │     │ Windowing    │
        └──────────────┘     └──────────────┘

                         ┌──────────────────────┐
                         │      Pipeline        │
                         │ Stage → Stage → ...  │
                         └──────────────────────┘
```

### Core design idea

The framework separates responsibilities instead of putting everything into one agent class:

```text
Message
   │
   ├── Memory
   │
   └── Agent
         │
         ├── Tools
         │
         └── Router
                │
                └── Pipeline
```

This makes the project easier to extend because new agents and tools can follow existing contracts without changing the core architecture.

---

## 📁 Project Structure

```text
agentforge/
│
├── main.py
│
├── core/
│   ├── message.py          # Message data model
│   ├── memory.py           # Conversation memory
│   ├── base_agent.py       # Abstract agent contract
│   ├── base_tool.py        # Abstract tool contract
│   └── pipeline.py         # Sequential pipeline orchestration
│
├── agents/
│   ├── chat_agent.py       # General conversational agent
│   ├── analyst_agent.py    # Numerical analysis agent
│   └── router_agent.py     # Task routing and delegation
│
├── tools/
│   ├── calculator_tool.py  # Mathematical expressions
│   ├── text_tool.py        # Text analysis
│   └── search_tool.py      # Simulated knowledge-base search
│
├── utils/
│   ├── logger.py           # Reusable LoggingMixin
│   └── registry.py         # Named component registry
│
├── requirements.txt
└── .gitignore
```

---

## 🚀 Features

### 1. Message System

`Message` acts as the basic data unit exchanged by the framework.

It supports:

- `user`, `assistant`, `system`, and `tool` roles
- Metadata
- Automatic message IDs
- Word counting
- Serialization through `to_dict()`
- Alternative constructors
- Iteration over message words

It also demonstrates Python's data-model methods:

```python
message = Message.user("Hello AgentForge!")

print(message)
print(len(message))
print(bool(message))
print("Hello" in message)
```

---

### 2. Configurable Memory

The `Memory` class stores conversation history with a configurable maximum size.

```python
memory = Memory(max_size=3)

memory.add_user("Hello")
memory.add_assistant("Hi!")
memory.add_user("How are you?")
memory.add_assistant("I'm doing well.")
```

When the configured limit is exceeded, the oldest messages are automatically removed.

It also supports:

```python
memory.last(2)
memory.messages_by_role("user")
memory.summary()
memory.clear()
```

This demonstrates **encapsulation, properties, iteration, indexing, and composition**.

---

### 3. Extensible Tool System

All framework tools follow the `BaseTool` contract:

```python
class BaseTool(ABC):
    @property
    @abstractmethod
    def name(self):
        ...

    @property
    @abstractmethod
    def description(self):
        ...

    @abstractmethod
    def run(self, input_text):
        ...
```

Tools can then be called naturally:

```python
calculator = CalculatorTool()

result = calculator("calculate 25 * 4")
```

The base class also tracks:

- Number of calls
- Last input
- Last output
- Tool statistics

---

### 4. Built-in Tools

| Tool | Purpose |
|---|---|
| `CalculatorTool` | Evaluates basic mathematical expressions |
| `TextTool` | Word statistics, sentiment signals, keyword extraction, and reversal |
| `SearchTool` | Searches a small built-in knowledge base |

> **Important:** `SearchTool` is a simulated search component. It does **not** perform real web searches or call an external search API.

---

### 5. Specialized Agents

AgentForge includes three agent types:

#### 💬 `ChatAgent`

Handles conversational inputs, greetings, questions, and available tools.

```python
chat = ChatAgent("ChatBot", personality="friendly")

chat.add_tool(CalculatorTool())
chat.add_tool(TextTool())
chat.add_tool(SearchTool())

print(chat("Calculate 150 * 3 + 250"))
```

#### 📊 `AnalystAgent`

Extracts numbers from text and calculates descriptive statistics:

- Count
- Sum
- Mean
- Median
- Mode
- Standard deviation
- Minimum
- Maximum
- Range

Example:

```python
analyst = AnalystAgent("DataBot")

print(
    analyst(
        "Analyse this data: 10 20 30 40 50"
    )
)
```

#### 🚦 `RouterAgent`

Routes incoming tasks to registered specialized agents based on the project's routing rules.

```python
router = RouterAgent("MainRouter")

router.register_agent("chat", chat)
router.register_agent("analyst", analyst)

print(router.run("Analyse these numbers: 5 10 15 20 25"))
```

The router works against the common `run()` interface rather than depending on a concrete agent implementation.

---

## ⛓️ Pipeline Orchestration

`Pipeline` lets multiple processing stages execute sequentially.

```text
Input
  │
  ▼
Normaliser
  │
  ▼
Keyword Extractor
  │
  ▼
Next Stage
  │
  ▼
Final Output
```

Stages only need a callable `run()` method.

```python
class TextNormaliser:
    name = "normaliser"

    def run(self, text):
        return " ".join(text.lower().split())
```

Build a pipeline:

```python
pipeline = Pipeline("text_pipeline")

pipeline.add(TextNormaliser())
pipeline.add(KeywordExtractor())

result = pipeline.run(
    "Python is an amazing language for data engineering."
)
```

The framework also overloads `|`:

```python
pipeline = Pipeline("text_pipeline")

pipeline = pipeline | normaliser | extractor
```

This is a practical demonstration of **operator overloading + composition**.

---

## 🧩 Duck Typing

One of the most useful design ideas in the project is duck typing.

A pipeline stage does not have to inherit from a specific base class.

If it provides a callable `run()` method, it can participate:

```python
class CustomStage:
    name = "custom"

    def run(self, text):
        return text.upper()
```

Then:

```python
pipeline.add(CustomStage())
```

The same principle is used by `RouterAgent` when registering agents.

This keeps the framework flexible without forcing every component into the same inheritance hierarchy.

---

## 📝 Logging with Mixins

`LoggingMixin` provides reusable logging functionality without being tied to a specific agent class.

```python
class MyAgent(LoggingMixin, BaseAgent):
    ...
```

Supported levels include:

```text
DEBUG
INFO
WARN
ERROR
```

Logs can also be retrieved and filtered:

```python
LoggingMixin.all_logs()
LoggingMixin.logs_by_level("INFO")
LoggingMixin.clear_logs()
```

This demonstrates the **mixin pattern and multiple inheritance**.

---

## 🧠 OOP Concepts Demonstrated

| Concept | Where | Demonstration |
|---|---|---|
| Abstract Base Classes | `base_agent.py`, `base_tool.py` | Enforced component contracts |
| Inheritance | Agent/tool classes | Specialized implementations |
| Multiple Inheritance | Agent classes | `LoggingMixin + BaseAgent` |
| Composition | `BaseAgent` | Agent contains memory and tools |
| Encapsulation | `Memory` | Private message storage |
| Polymorphism | `RouterAgent` | Different agents share `run()` |
| Duck Typing | Router/Pipeline | Compatible objects without inheritance |
| `__str__` / `__repr__` | Multiple classes | Human/developer representations |
| `__len__` | Message/Memory/Agent/Pipeline | Pythonic size semantics |
| `__eq__` | Message/Tool | Object comparison |
| `__add__` | Message | Message concatenation |
| `__contains__` | Message/Agent/Registry | `x in object` |
| `__iter__` | Message/Memory/Pipeline | Iteration support |
| `__getitem__` | Memory/Pipeline/Registry | Index/key access |
| `__call__` | Agent/Tool | Function-like objects |
| `__or__` | Pipeline | Pipeline composition |
| `@classmethod` | Message/Agent | Alternative constructors/lookups |
| `@staticmethod` | Tools/agents | Stateless utilities |
| `@property` | Memory/Agent/Tool | Controlled attribute access |
| Method chaining | `add_tool()` | `agent.add_tool(a).add_tool(b)` |

---

## 🛠️ Requirements

- **Python 3.8+**
- No third-party packages required
- Uses Python standard-library modules such as:
  - `abc`
  - `math`

---

## ▶️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/agentforge.git
cd agentforge
```

### 2. Run the demo

```bash
python main.py
```

The demo walks through:

```text
Demo 1 → Message system
Demo 2 → Tools and Registry
Demo 3 → Agents and Memory
Demo 4 → RouterAgent
Demo 5 → Pipeline
```

---

## 🧪 What the Demo Covers

Running `main.py` exercises the framework end-to-end:

```text
Message creation
      ↓
Magic methods
      ↓
Tool registration
      ↓
Tool execution
      ↓
Agent creation
      ↓
Memory management
      ↓
Task routing
      ↓
Pipeline execution
      ↓
Execution logs
```

It also prints an OOP concept checklist at the end of the demonstration.

---

## 🎯 Example Workflow

A typical AgentForge flow looks like this:

```python
from tools.calculator_tool import CalculatorTool
from agents.chat_agent import ChatAgent
from agents.analyst_agent import AnalystAgent
from agents.router_agent import RouterAgent

chat = ChatAgent("ChatBot")
chat.add_tool(CalculatorTool())

analyst = AnalystAgent("DataBot")

router = RouterAgent("MainRouter")
router.register_agent("chat", chat)
router.register_agent("analyst", analyst)

print(router.run("Calculate 25 * 4"))
print(router.run("Analyse these numbers: 10 20 30 40"))
```

The important architectural idea is that the router does not need to know the internal implementation of each specialized agent.

---

## 🔍 Project Scope & Limitations

AgentForge is a **learning and portfolio framework**, not a production-ready autonomous-agent platform.

### What it currently does

- Provides modular agent abstractions
- Provides tool abstractions
- Maintains bounded in-memory conversation history
- Routes tasks using keyword-based rules
- Runs sequential processing pipelines
- Provides simulated search
- Demonstrates reusable logging

### What it does not currently do

- Generate responses through a real LLM
- Perform real web searches
- Persist memory to a database
- Perform semantic/vector retrieval
- Execute autonomous multi-step reasoning
- Provide production authentication or authorization
- Provide asynchronous execution
- Provide distributed execution

This distinction matters: the project demonstrates the **architecture and OOP mechanics of an agent framework**, while the actual intelligence and external integrations are intentionally simplified.

---



---

## 📜 License

This project is intended as a learning and portfolio project.

---

## 👨‍💻 Author

**Chadalavada Trinay Sai**

Built as a Python OOP portfolio project to explore the architecture behind modular AI-agent systems.

---

<div align="center">

### 🤖 AgentForge

**Build components. Compose agents. Orchestrate workflows.**

</div>

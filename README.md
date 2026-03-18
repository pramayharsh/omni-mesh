# Omni-Mesh: A Decentralized Multi-Agent AI Economy

Omni-Mesh is an experimental framework for building a "Mini-AI Economy" where specialized agents communicate via a decentralized message bus using structured **Agent Contracts**.

## 🚀 The Vision
Instead of a single monolithic LLM prompt, Omni-Mesh breaks complex workflows into a swarm of agents (Librarian, Economist, Red-Teamer, etc.) that "contract" each other to solve problems safely and cost-effectively.

## 🏗️ Architecture (Phase 1: Foundation)
- **Agent-Contract Protocol:** Uses Pydantic to enforce structured data exchange between agents.
- **Decentralized Mesh:** An asynchronous message bus (OmniMeshBus) that allows agents to be decoupled.
- **BaseAgent Class:** A standardized parent class for all specialized agents.

## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **Messaging:** Asyncio-based Pub/Sub (Scalable to Redis)
- **Validation:** Pydantic
- **Vector Memory:** FAISS (Phase 2)

## 🚦 Getting Started
1. Clone the repo.
2. Create a venv: `python -m venv venv`.
3. Install deps: `pip install -r requirements.txt`.
4. Run the test: `python test_phase1.py`.
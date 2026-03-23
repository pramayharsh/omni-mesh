# Omni-Mesh: A Decentralized Multi-Agent AI Economy

**Omni-Mesh** is a distributed Multi-Agent System (MAS) built in Python that simulates an autonomous AI company. Unlike monolithic chatbots, Omni-Mesh agents communicate over a decentralized message bus using structured **Agent Contracts**, ensuring security, fiscal responsibility, and high-quality output.

---

## 🚀 The Vision
Instead of a single monolithic LLM prompt, Omni-Mesh breaks complex workflows into a swarm of agents (Librarian, Economist, Red-Teamer, etc.) that "contract" each other to solve problems safely and cost-effectively.

---

## 🏗️ The "Swarm" Architecture

Omni-Mesh uses a **Hub-and-Spoke Mesh** where specialized agents negotiate tasks:

1. **Librarian (Memory):** Manages long-term episodic memory using **FAISS** and **HuggingFace** embeddings.
2. **Economist (Finance):** Tracks the "Unit Economics" of every agent action, managing a simulated token budget.
3. **Red-Teamer (Security):** Acts as a mandatory firewall, scanning all data for PII, API keys, and sensitive leaks.
4. **Writer (Execution):** Uses **Groq (Llama 3.3)** to generate high-speed technical reports.
5. **Refiner (Quality):** A critic agent that performs iterative editing on the Writer's drafts.
6. **Bridge (Integration):** The external gateway that delivers finalized, safe results.

---

## 📂 Project Structure

```text
omni_mesh/
├── data/                  # Persistent FAISS indexes and Ledger JSON
├── src/
│   ├── agents/            # Specialized Agent Logic (Writer, Librarian, etc.)
│   ├── core/              # The "Mesh" Message Bus and Pydantic Schemas
│   ├── memory/            # Vector Store Wrappers (FAISS/HF)
│   ├── utils/             # LLM Engines, Security Scanners, and Cost Counters
├── tests/                 # Phase-by-phase verification scripts
├── .env.example           # Configuration template
├── requirements.txt       # Production dependencies
└── main.py                # System entry point
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Inference | Groq (Llama 3.3 / 3.1) |
| Embeddings | HuggingFace (`all-MiniLM-L6-v2`) |
| Vector DB | FAISS (FlatL2 Index) |
| Validation | Pydantic (Strict Type Enforcement) |
| Backbone | Asyncio (High-concurrency Messaging) |

---

## 🚦 Getting Started

### 1. Prerequisites

- Python 3.10+
- HuggingFace API Key (Free)
- Groq API Key (Free)

### 2. Installation

```bash
git clone https://github.com/YOUR_USERNAME/omni-mesh.git
cd omni-mesh
python -m venv venv
source venv/bin/activate  # Or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Configuration

Create a `.env` file based on `.env.example`:

```text
HF_API_KEY=your_key_here
GROQ_API_KEY=your_key_here
```

### 4. Run the Full Swarm Test

```bash
python tests/test_final_swarm.py
```

---

## 🛡️ Governance & Safety

Omni-Mesh implements a **Zero-Trust AI Architecture**. No data reaches the end-user (Bridge) without passing through:

- The **Red-Teamer** for PII/Secret scanning
- The **Refiner** for quality assurance

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
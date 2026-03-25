# Omni-Mesh: A Decentralized Multi-Agent AI Economy 🚀

**Omni-Mesh** is a distributed Multi-Agent System (MAS) built in Python that simulates an autonomous AI company. Unlike monolithic chatbots, Omni-Mesh agents communicate over a decentralized message bus using structured **Agent Contracts**, ensuring security, fiscal responsibility, and high-quality output.

---

## 🎯 Why Omni-Mesh? (Value Proposition)

Omni-Mesh transforms a "project" into a **Managed AI Workforce**. It solves the three biggest hurdles in enterprise AI adoption:

- **Trust & Safety:** The **Red-Teamer** acts as a mandatory compliance officer, scanning all agent outputs for PII (emails, keys, passwords) before they reach the user.
- **Fiscal Transparency:** The **Economist** provides real-time "Unit Economics." Businesses can track the exact cost of every AI interaction in a persistent ledger.
- **Quality Guarantee:** The **Refiner** automates the "Critic-Loop." No draft is delivered until a specialized editor agent approves the clarity and tone.

---

## 👥 Target Users

- **Privacy-Conscious Enterprises:** Companies that want to leverage AI on internal data but require a **Zero-Trust** security layer to prevent data leaks.
- **AI SaaS Founders:** Developers who need to manage token budgets and operational costs at scale using the **Economist's** ledger.
- **Knowledge Workers:** Analysts who require high-grade, polished reports where the AI "argues" with itself (Writer + Refiner) to produce the best result.

---

## 🏗️ The "Swarm" Architecture

Omni-Mesh uses a **Hub-and-Spoke Mesh** where specialized agents negotiate tasks:

1. **Librarian (Memory):** Manages long-term episodic memory using **FAISS** and **HuggingFace** embeddings.
2. **Economist (Finance):** Tracks the "Unit Economics" of every agent action, managing a simulated token budget.
3. **Red-Teamer (Security):** Acts as a mandatory firewall, scanning all data for PII, API keys, and sensitive leaks.
4. **Writer (Execution):** Uses **Groq (Llama 3.3)** to generate high-speed technical reports.
5. **Refiner (Quality):** A critic agent that performs iterative editing on the Writer's drafts.
6. **Bridge (Integration):** The external gateway that delivers finalized, safe results via the UI.

---

## 📂 Project Structure

```text
omni_mesh/
├── data/                  # Persistent FAISS indexes and Ledger JSON
├── src/
│   ├── agents/            # Specialized Agent Logic (Writer, Librarian, etc.)
│   ├── core/              # The "Mesh" Message Bus and Pydantic Schemas
│   ├── memory/            # Vector Store Wrappers (FAISS/HF API)
│   ├── utils/             # LLM Engines, Security Scanners, and Cost Counters
├── templates/             # Web Dashboard (FastAPI/Jinja2/WebSockets)
├── tests/                 # Phase-by-phase verification scripts
├── .env.example           # Configuration template
├── requirements.txt       # Production dependencies
└── main.py                # Web Entry Point (FastAPI Dashboard)
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Inference | Groq (Llama 3.3 / 3.1) |
| Embeddings | HuggingFace (`all-MiniLM-L6-v2`) |
| Vector DB | FAISS (FlatL2 Index) |
| API Framework | FastAPI |
| Real-time UI | WebSockets & Jinja2 |
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
HF_API_KEY=your_huggingface_key
GROQ_API_KEY=your_groq_key
```

### 4. Launch the Web Dashboard

Experience the swarm in real-time through the FastAPI monitor:

```bash
python main.py
```

Visit `http://localhost:8000` to see the **Live Mesh Traffic**.

---

## 🛡️ Governance & Safety

Omni-Mesh implements a **Zero-Trust AI Architecture**. No data reaches the end-user (Bridge) without passing through:

- The **Red-Teamer** for PII/Secret scanning
- The **Refiner** for quality assurance

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

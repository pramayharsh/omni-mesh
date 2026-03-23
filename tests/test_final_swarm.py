import asyncio
import sys
import os

# Add root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.mesh import OmniMeshBus
from src.agents.librarian import LibrarianAgent
from src.agents.economist import EconomistAgent
from src.agents.red_teamer import RedTeamerAgent
from src.agents.writer import WriterAgent
from src.agents.refiner import RefinerAgent
from src.agents.bridge import BridgeAgent
from src.agents.base_agent import BaseAgent

class SwarmOrchestrator(BaseAgent):
    """
    Acts as the 'Human-in-the-loop' or the Brain that triggers 
    the next stage after the Librarian clears the security check.
    """
    async def handle_message(self, contract):
        if contract.task_type == "QUERY_RESULT":
            print(f"✅ [Orchestrator] Context cleared and received. Hiring Writer...")
            
            # Extract the content from the search results
            context_data = " ".join([r['content'] for r in contract.payload['results']])
            
            # Hire the Writer to turn this context into a report
            await self.send(
                receiver="Writer",
                task="WRITE_REPORT",
                data={
                    "topic": "Company 2024 Strategy",
                    "context": context_data
                }
            )
        
        elif contract.task_type == "QUERY_BLOCKED":
            print(f"❌ [Orchestrator] Workflow aborted. Security violation detected.")

async def run_test():
    mesh = OmniMeshBus()
    
    # 1. Initialize the Full Swarm
    economist = EconomistAgent("Economist", mesh, budget=1.00)
    librarian = LibrarianAgent("Librarian", mesh)
    red_teamer = RedTeamerAgent("Red-Teamer", mesh)
    writer = WriterAgent("Writer", mesh)
    refiner = RefinerAgent("Refiner", mesh)
    bridge = BridgeAgent("Bridge", mesh)
    
    # The Orchestrator (The User)
    user = SwarmOrchestrator("User", mesh)

    print("\n" + "="*50)
    print("🚀 STARTING THE OMNI-MESH MINI-AI ECONOMY")
    print("="*50)

    # STEP 1: Feed the memory (Simulate knowledge base)
    print("\n[Step 1] Feeding knowledge into the Librarian...")
    await user.send("Librarian", "MEMORIZE", {
        "content": "Our 2024 strategy is to expand into Mars and reduce coffee expenses by 50%.",
        "meta": {"source": "ceo_memo"}
    })
    await asyncio.sleep(1)

    # STEP 2: Initiate the Request
    print("\n[Step 2] Requesting a professional report...")
    await user.send("Librarian", "QUERY", {"query": "What is the 2024 strategy?"})

    # Wait for the whole chain to finish (Librarian -> Red-Teamer -> Writer -> Refiner -> Bridge)
    await asyncio.sleep(15) 
    
    # STEP 3: Final Budget Audit
    print("\n[Step 3] Final Economic Audit...")
    await user.send("Economist", "BUDGET_CHECK", {})
    await asyncio.sleep(1)

    print("\n" + "="*50)
    print("🏁 SWARM SIMULATION COMPLETE")
    print("="*50 + "\n")

if __name__ == "__main__":
    asyncio.run(run_test())
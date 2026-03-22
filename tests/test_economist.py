import asyncio
import sys
import os

# Add root to path so we can import src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.mesh import OmniMeshBus
from src.agents.librarian import LibrarianAgent
from src.agents.economist import EconomistAgent
from src.agents.base_agent import BaseAgent

# We create a specific User class to handle incoming results
class MockUser(BaseAgent):
    async def handle_message(self, contract):
        """
        Handles results coming back from the Librarian and Economist.
        """
        if contract.task_type == "QUERY_RESULT":
            print(f"✅ [User] Received search results from Librarian. Found {len(contract.payload['results'])} items.")
        
        elif contract.task_type == "BUDGET_APPROVAL":
            allowed = contract.payload.get("allowed")
            remaining = contract.payload.get("remaining")
            status = "🟢 WITHIN BUDGET" if allowed else "🔴 BUDGET EXCEEDED"
            print(f"📊 [User] Economic Audit: {status} | Remaining: ${remaining:.5f}")

async def run_test():
    # 1. Initialize the Mesh
    mesh = OmniMeshBus()
    
    # 2. Initialize Agents
    # We set a tiny budget of $0.0005 to see the effect of spending
    economist = EconomistAgent("Economist", mesh, budget=0.0005)
    librarian = LibrarianAgent("Librarian", mesh)
    user = MockUser("User", mesh)
    
    print("\n--- 💸 Starting Omni-Mesh Economic Simulation ---")

    # Step A: Memorize something (Triggers 1st Spending Report)
    print("\n[Step 1] User: Requesting Librarian to MEMORIZE...")
    await user.send("Librarian", "MEMORIZE", {
        "content": "Phase 3 is about fiscal responsibility.",
        "meta": {"priority": "low"}
    })
    await asyncio.sleep(1.5) # Wait for Librarian and Economist to finish

    # Step B: Query something (Triggers 2nd Spending Report)
    print("\n[Step 2] User: Requesting Librarian to QUERY...")
    await user.send("Librarian", "QUERY", {"query": "fiscal responsibility"})
    await asyncio.sleep(1.5)

    # Step C: Check the budget status via the Economist
    print("\n[Step 3] User: Requesting BUDGET_CHECK from Economist...")
    await user.send("Economist", "BUDGET_CHECK", {})
    await asyncio.sleep(1)

    print("\n--- 🏁 Simulation Complete ---\n")

if __name__ == "__main__":
    asyncio.run(run_test())
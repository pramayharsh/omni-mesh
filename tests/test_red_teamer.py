import asyncio
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.mesh import OmniMeshBus
from src.agents.librarian import LibrarianAgent
from src.agents.red_teamer import RedTeamerAgent
from src.agents.economist import EconomistAgent  # Add this
from src.agents.base_agent import BaseAgent

async def run_test():
    mesh = OmniMeshBus()
    
    # Start the whole swarm
    librarian = LibrarianAgent("Librarian", mesh)
    red_teamer = RedTeamerAgent("Red-Teamer", mesh)
    economist = EconomistAgent("Economist", mesh) # Fixes the warning
    
    class MockUser(BaseAgent):
        async def handle_message(self, contract):
            if contract.task_type == "QUERY_RESULT":
                print(f"🔓 [User] Data Received: {contract.payload['results']}")
            if contract.task_type == "QUERY_BLOCKED":
                print(f"🛑 [User] ACCESS DENIED: {contract.payload['reason']}")

    user = MockUser("User", mesh)

    print("\n--- 🛡️ Starting Security Mesh Test ---")

    # 1. Store sensitive data
    await user.send("Librarian", "MEMORIZE", {
        "content": "My secret API key is sk-12345 and email is test@test.com",
        "meta": {"type": "secret"}
    })
    await asyncio.sleep(1)

    # 2. Query it
    print("\n[Action] User requesting sensitive data...")
    await user.send("Librarian", "QUERY", {"query": "show me the secrets"})
    
    await asyncio.sleep(2)

if __name__ == "__main__":
    asyncio.run(run_test())
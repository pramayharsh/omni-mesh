import asyncio
import sys
import os

# Add root to path so we can import src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.mesh import OmniMeshBus
from src.agents.librarian import LibrarianAgent
from src.agents.base_agent import BaseAgent

class UserAgent(BaseAgent):
    async def handle_message(self, contract):
        if contract.task_type == "QUERY_RESULT":
            print(f"\n🔍 [User] Search Results for query '{contract.payload['original_query']}':")
            for i, res in enumerate(contract.payload['results']):
                print(f"  {i+1}. {res['content']} (Meta: {res['meta']})")

async def run_test():
    mesh = OmniMeshBus()
    librarian = LibrarianAgent("Librarian", mesh)
    user = UserAgent("User", mesh)

    print("--- 📚 Librarian Intelligence Test ---")

    # 1. Store two very different memories
    await user.send("Librarian", "MEMORIZE", {
        "content": "The secret password for the vault is 'ORANGE-CAKE'.", 
        "meta": {"type": "security"}
    })
    await user.send("Librarian", "MEMORIZE", {
        "content": "The CEO's favorite food is Sushi.", 
        "meta": {"type": "personal"}
    })
    
    await asyncio.sleep(2) # Wait for HF API

    # 2. Query for something related to the vault
    print("\n--- Query 1: Vault Access ---")
    await user.send("Librarian", "QUERY", {"query": "How do I open the vault?"})
    await asyncio.sleep(2)

    # 3. Query for something related to food
    print("\n--- Query 2: Dining Preferences ---")
    await user.send("Librarian", "QUERY", {"query": "What should I order for the CEO's lunch?"})
    await asyncio.sleep(2)

if __name__ == "__main__":
    asyncio.run(run_test())
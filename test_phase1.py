import asyncio
from src.core.mesh import OmniMeshBus
from src.agents.base_agent import BaseAgent
from src.core.schema import AgentContract

# Create a concrete implementation of BaseAgent for testing
class TestAgent(BaseAgent):
    async def handle_message(self, contract: AgentContract):
        print(f"✅ {self.name} successfully received message from {contract.sender}: {contract.payload['msg']}")

async def run_test():
    # 1. Initialize the Mesh
    mesh = OmniMeshBus()

    # 2. Initialize two agents
    alice = TestAgent("Alice", mesh)
    bob = TestAgent("Bob", mesh)

    print("--- Starting Phase 1 Mesh Test ---")

    # 3. Alice sends a message to Bob
    await alice.send(
        receiver="Bob", 
        task="GREETING", 
        data={"msg": "Hello from the Omni-Mesh!"}
    )

    # Give it a second to process
    await asyncio.sleep(0.5)

if __name__ == "__main__":
    asyncio.run(run_test())
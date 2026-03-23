from src.agents.base_agent import BaseAgent

class BridgeAgent(BaseAgent):
    async def handle_message(self, contract):
        if contract.task_type == "DELIVER_OUTPUT":
            content = contract.payload.get("final_content")
            print("\n📬 [BRIDGE] DELIVERY SUCCESSFUL!")
            print("--------------------------------------------------")
            print(f"FINAL OUTPUT:\n{content}")
            print("--------------------------------------------------")
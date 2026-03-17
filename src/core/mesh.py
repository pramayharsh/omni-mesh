import asyncio

class OmniMeshBus:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, agent_name, callback):
        self.subscribers[agent_name] = callback

    async def publish(self, contract):
        print(f"🚀 [MESH] {contract.sender} -> {contract.receiver} ({contract.task_type})")
        if contract.receiver in self.subscribers:
            # Simulate network latency
            await asyncio.sleep(0.1)
            await self.subscribers[contract.receiver](contract)
        else:
            print(f"⚠️ [MESH] Target {contract.receiver} not found.")
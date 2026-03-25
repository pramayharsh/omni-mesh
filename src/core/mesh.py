import asyncio

class OmniMeshBus:
    def __init__(self):
        self.subscribers = {}
        self.monitor_callback = None # New: For UI updates

    def set_monitor(self, callback):
        self.monitor_callback = callback

    def subscribe(self, agent_name, callback):
        self.subscribers[agent_name] = callback

    async def publish(self, contract):
        # 1. Internal Log
        msg = f"🚀 [MESH] {contract.sender} -> {contract.receiver} ({contract.task_type})"
        print(msg)
        
        # 2. UI Update (If FastAPI is connected)
        if self.monitor_callback:
            await self.monitor_callback(contract.model_dump())

        if contract.receiver in self.subscribers:
            await asyncio.sleep(0.1)
            await self.subscribers[contract.receiver](contract)
from src.core.schema import AgentContract

class BaseAgent:
    def __init__(self, name: str, mesh):
        self.name = name
        self.mesh = mesh
        self.mesh.subscribe(self.name, self.handle_message)

    async def send(self, receiver: str, task: str, data: dict):
        contract = AgentContract(sender=self.name, receiver=receiver, task_type=task, payload=data)
        await self.mesh.publish(contract)

    async def handle_message(self, contract: AgentContract):
        # To be implemented by subclasses
        raise NotImplementedError
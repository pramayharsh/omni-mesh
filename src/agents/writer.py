from src.agents.base_agent import BaseAgent
from src.utils.llm import LLMEngine

class WriterAgent(BaseAgent):
    def __init__(self, name, mesh):
        super().__init__(name, mesh)
        self.llm = LLMEngine()

    async def handle_message(self, contract):
        if contract.task_type == "WRITE_REPORT":
            context = contract.payload.get("context", "")
            topic = contract.payload.get("topic", "")
            
            prompt = f"Using this context: {context}, write a professional summary about {topic}."
            draft = self.llm.generate("You are a helpful technical writer.", prompt)
            
            print(f"✍️ [Writer] Draft completed. Sending to Refiner...")
            
            # Send to Refiner for editing
            await self.send(
                receiver="Refiner",
                task="REFINE_TEXT",
                data={"draft": draft, "original_topic": topic}
            )
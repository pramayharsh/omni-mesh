from src.agents.base_agent import BaseAgent
from src.utils.llm import LLMEngine

class RefinerAgent(BaseAgent):
    def __init__(self, name, mesh):
        super().__init__(name, mesh)
        self.llm = LLMEngine()

    async def handle_message(self, contract):
        if contract.task_type == "REFINE_TEXT":
            draft = contract.payload.get("draft")
            
            refinement_prompt = f"Improve this draft for clarity and professional tone: {draft}"
            final_text = self.llm.generate("You are a senior editor.", refinement_prompt)
            
            print(f"✨ [Refiner] Refined the draft. Sending to Bridge...")
            
            # Send to Bridge (The Exit)
            await self.send(
                receiver="Bridge",
                task="DELIVER_OUTPUT",
                data={"final_content": final_text}
            )
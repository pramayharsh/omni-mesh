import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class LLMEngine:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.model = "llama-3.3-70b-versatile" # Fast and free-tier friendly

    def generate(self, system_prompt: str, user_prompt: str):
        try:
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.7
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"Error generating response: {str(e)}"
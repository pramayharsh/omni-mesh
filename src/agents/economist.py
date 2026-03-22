import json
import os
from src.agents.base_agent import BaseAgent
from src.core.schema import AgentContract

class EconomistAgent(BaseAgent):
    def __init__(self, name, mesh, budget=0.05): # Start with a tiny $0.05 budget
        super().__init__(name, mesh)
        self.ledger_path = "data/ledger.json"
        self.budget = budget
        self.total_spent = 0.0
        self._load_ledger()

    def _load_ledger(self):
        if os.path.exists(self.ledger_path):
            with open(self.ledger_path, 'r') as f:
                data = json.load(f)
                self.total_spent = data.get("total_spent", 0.0)
        else:
            self._save_ledger()

    def _save_ledger(self):
        with open(self.ledger_path, 'w') as f:
            json.dump({"total_spent": self.total_spent, "budget": self.budget}, f)

    async def handle_message(self, contract: AgentContract):
        if contract.task_type == "REPORT_SPENDING":
            amount = contract.payload.get("amount", 0.0)
            self.total_spent += amount
            self._save_ledger()
            print(f"💰 [ECONOMIST] Recorded ${amount:.5f}. Total Mesh Spend: ${self.total_spent:.5f}")

        elif contract.task_type == "BUDGET_CHECK":
            allowed = self.total_spent < self.budget
            await self.send(
                receiver=contract.sender,
                task="BUDGET_APPROVAL",
                data={"allowed": allowed, "remaining": self.budget - self.total_spent}
            )
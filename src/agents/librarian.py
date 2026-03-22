from src.agents.base_agent import BaseAgent
from src.memory.vector_store import LibrarianStore
from src.core.schema import AgentContract
from src.utils.token_counter import estimate_cost

class LibrarianAgent(BaseAgent):
    def __init__(self, name, mesh):
        super().__init__(name, mesh)
        self.store = LibrarianStore()

    async def handle_message(self, contract: AgentContract):
        """
        Handles memory storage and retrieval.
        Reports simulated costs to the Economist after every API action.
        """
        
        if contract.task_type == "MEMORIZE":
            content = contract.payload.get("content")
            meta = contract.payload.get("meta", {})
            
            # 1. Perform the action
            self.store.add_memory(content, meta)
            print(f"📜 [Librarian] Memorized: {content[:50]}...")
            
            # 2. Report Spending to Economist
            cost = estimate_cost("embedding")
            await self.send(
                receiver="Economist", 
                task="REPORT_SPENDING", 
                data={"amount": cost, "action": "memorize"}
            )

        elif contract.task_type == "QUERY":
            query_text = contract.payload.get("query")
            
            # 1. Search the vector store
            results = self.store.query(query_text)
            
            # 2. Report Spending to Economist
            cost = estimate_cost("embedding")
            await self.send(
                receiver="Economist", 
                task="REPORT_SPENDING", 
                data={"amount": cost, "action": "query"}
            )
            
            # 3. Send results back to the original requester
            await self.send(
                receiver=contract.sender,
                task="QUERY_RESULT",
                data={
                    "results": results, 
                    "original_query": query_text
                }
            )
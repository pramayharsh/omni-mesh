from src.agents.base_agent import BaseAgent
from src.memory.vector_store import LibrarianStore
from src.core.schema import AgentContract

class LibrarianAgent(BaseAgent):
    def __init__(self, name, mesh):
        super().__init__(name, mesh)
        self.store = LibrarianStore()

    async def handle_message(self, contract: AgentContract):
        if contract.task_type == "MEMORIZE":
            content = contract.payload.get("content")
            meta = contract.payload.get("meta", {})
            self.store.add_memory(content, meta)
            print(f"📜 [Librarian] Memorized: {content[:50]}...")

        elif contract.task_type == "QUERY":
            query = contract.payload.get("query")
            results = self.store.query(query)
            # Send the results back to the requester
            await self.send(
                receiver=contract.sender,
                task="QUERY_RESULT",
                data={"results": results, "original_query": query}
            )
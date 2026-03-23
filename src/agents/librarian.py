from src.agents.base_agent import BaseAgent
from src.memory.vector_store import LibrarianStore
from src.core.schema import AgentContract
from src.utils.token_counter import estimate_cost

class LibrarianAgent(BaseAgent):
    def __init__(self, name, mesh):
        super().__init__(name, mesh)
        self.store = LibrarianStore()
        # "Waiting room" for data being checked by Red-Teamer
        self.pending_queries = {} 

    async def handle_message(self, contract: AgentContract):
        # --- 1. MEMORIZE TASK ---
        if contract.task_type == "MEMORIZE":
            content = contract.payload.get("content")
            self.store.add_memory(content, contract.payload.get("meta", {}))
            
            # Report cost (Attempt to find Economist)
            await self.send("Economist", "REPORT_SPENDING", {"amount": estimate_cost("embedding")})

        # --- 2. QUERY TASK (The Gatekeeper Step) ---
        elif contract.task_type == "QUERY":
            query_text = contract.payload.get("query")
            results = self.store.query(query_text)
            
            # Store results in the 'waiting room' using contract_id
            self.pending_queries[contract.contract_id] = {
                "results": results,
                "original_sender": contract.sender,
                "query": query_text
            }

            # ASK RED-TEAMER FIRST
            combined_text = " ".join([r['content'] for r in results])
            await self.send(
                receiver="Red-Teamer",
                task="SECURITY_REVIEW",
                data={
                    "content": combined_text,
                    "query_ref": contract.contract_id # Pass the ID back
                }
            )

        # --- 3. SECURITY REPORT (The Decision Step) ---
        elif contract.task_type == "SECURITY_REPORT":
            is_safe = contract.payload.get("is_safe")
            query_ref = contract.payload.get("query_ref")
            
            # Get data from the waiting room
            pending = self.pending_queries.pop(query_ref, None)
            
            if not pending:
                return

            if is_safe:
                print(f"🛡️ [Librarian] Approved. Sending data to {pending['original_sender']}.")
                await self.send(
                    receiver=pending['original_sender'],
                    task="QUERY_RESULT",
                    data={"results": pending['results'], "query": pending['query']}
                )
            else:
                print(f"🚨 [Librarian] SECURITY BLOCK! Sensitive data detected for {pending['original_sender']}.")
                await self.send(
                    receiver=pending['original_sender'],
                    task="QUERY_BLOCKED",
                    data={"reason": "PII/Sensitive data detected", "query": pending['query']}
                )
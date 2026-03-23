from src.agents.base_agent import BaseAgent
from src.utils.security import SecurityScanner
from src.core.schema import AgentContract

class RedTeamerAgent(BaseAgent):
    def __init__(self, name, mesh):
        super().__init__(name, mesh)
        self.scanner = SecurityScanner()

    async def handle_message(self, contract: AgentContract):
        if contract.task_type == "SECURITY_REVIEW":
            content_to_scan = contract.payload.get("content", "")
            # Capture the reference ID sent by the Librarian
            query_ref = contract.payload.get("query_ref") 
            
            findings = self.scanner.scan_text(content_to_scan)
            is_safe = len(findings) == 0
            reason = "Safe" if is_safe else f"Rejected: Found {', '.join(findings)}"
            
            print(f"🛡️ [Red-Teamer] Reviewing content... Status: {'✅' if is_safe else '❌'}")
            
            # Send the report back with the CORRECT KEY: 'query_ref'
            await self.send(
                receiver=contract.sender,
                task="SECURITY_REPORT",
                data={
                    "is_safe": is_safe,
                    "reason": reason,
                    "query_ref": query_ref # This is the crucial handshake key!
                }
            )
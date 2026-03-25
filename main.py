from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import asyncio
import uvicorn
import os

from src.core.mesh import OmniMeshBus
from src.agents.librarian import LibrarianAgent
from src.agents.economist import EconomistAgent
from src.agents.red_teamer import RedTeamerAgent
from src.agents.writer import WriterAgent
from src.agents.refiner import RefinerAgent
from src.agents.bridge import BridgeAgent
from src.agents.base_agent import BaseAgent

app = FastAPI()

# Make sure the templates directory exists
templates = Jinja2Templates(directory="templates")

# Initialize the Mesh and Swarm
mesh = OmniMeshBus()
economist = EconomistAgent("Economist", mesh)
librarian = LibrarianAgent("Librarian", mesh)
red_teamer = RedTeamerAgent("Red-Teamer", mesh)
writer = WriterAgent("Writer", mesh)
refiner = RefinerAgent("Refiner", mesh)
bridge = BridgeAgent("Bridge", mesh)

@app.get("/", response_class=HTMLResponse)
async def get_dashboard(request: Request):
    # Use keyword arguments to avoid "unhashable type: dict" error
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={}
    )

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    
    async def send_to_ui(contract_data):
        try:
            # If contract_data is a Pydantic model, it needs to be converted to a dict
            if hasattr(contract_data, "model_dump"):
                payload = contract_data.model_dump()
            else:
                payload = contract_data
            await websocket.send_json(payload)
        except Exception as e:
            print(f"UI Update Error: {e}") 

    mesh.set_monitor(send_to_ui)
    
    try:
        while True:
            await asyncio.sleep(10) # Keep connection alive
    except:
        print("WebSocket connection closed")

@app.post("/run")
async def run_swarm(topic: str, content: str):
    # This acts as the Orchestrator/User from the Web
    class WebOrchestrator(BaseAgent):
        async def handle_message(self, contract):
            # We use the same logic as test_final_swarm
            if contract.task_type == "QUERY_RESULT":
                context_data = " ".join([r['content'] for r in contract.payload['results']])
                await self.send("Writer", "WRITE_REPORT", {
                    "topic": topic,
                    "context": context_data
                })

    user = WebOrchestrator("WebUser", mesh)
    
    # 1. Store the knowledge
    await user.send("Librarian", "MEMORIZE", {"content": content})
    await asyncio.sleep(1) # Wait for storage
    
    # 2. Trigger the chain
    await user.send("Librarian", "QUERY", {"query": topic})
    
    return {"status": "Swarm activated", "topic": topic}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
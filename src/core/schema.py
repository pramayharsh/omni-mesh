from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from uuid import uuid4
from datetime import datetime

class AgentContract(BaseModel):
    contract_id: str = Field(default_factory=lambda: str(uuid4()))
    sender: str
    receiver: str
    task_type: str 
    payload: Dict[str, Any]
    status: str = "PENDING"
    result: Optional[Any] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)
    timestamp: str = Field(default_factory=lambda: datetime.now().isoformat())
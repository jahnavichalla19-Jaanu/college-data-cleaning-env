from pydantic import BaseModel
from typing import List, Optional

class Observation(BaseModel):
    data: List[dict]
    message: str

class Action(BaseModel):
    action_type: str
class GraderRequest(BaseModel):
    task_id: str
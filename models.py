from pydantic import BaseModel
from typing import List

class Observation(BaseModel):
    data: List[dict]
    message: str

class Action(BaseModel):
    action_type: str
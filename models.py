from pydantic import BaseModel

class CanInput(BaseModel):
    uid: str
    num_id: int
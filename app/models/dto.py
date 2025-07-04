from pydantic import BaseModel
from typing import Optional

class OperatorCreateDTO(BaseModel):
    user_id: str
    branch_id: int
    role: str
    is_active: Optional[bool] = True

class OperatorOutDTO(BaseModel):
    id: int
    user_id: str
    branch_id: int
    role: str
    is_active: bool

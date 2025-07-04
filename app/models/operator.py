from pydantic import BaseModel

class Operator:
    def __init__(self, id: int, user_id: str, branch_id: int, role: str, is_active: bool):
        self.id = id
        self.user_id = user_id
        self.branch_id = branch_id
        self.role = role
        self.is_active = is_active

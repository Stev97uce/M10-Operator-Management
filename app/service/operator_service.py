from typing import List, Optional
from app.models.dto import OperatorCreateDTO, OperatorOutDTO
from app.models.operator import Operator
from app.repository import operator_repository


def create_operator(data: OperatorCreateDTO) -> OperatorOutDTO:
    new_id = operator_repository.create_operator(data)
    return OperatorOutDTO(
        id=new_id,
        user_id=data.user_id,
        branch_id=data.branch_id,
        role=data.role,
        is_active=data.is_active
    )


def get_all_operators() -> List[OperatorOutDTO]:
    operators = operator_repository.get_all_operators()
    return [
        OperatorOutDTO(
            id=op.id,
            user_id=op.user_id,
            branch_id=op.branch_id,
            role=op.role,
            is_active=op.is_active
        )
        for op in operators
    ]


def get_operator_by_id(operator_id: int) -> Optional[OperatorOutDTO]:
    op = operator_repository.get_operator_by_id(operator_id)
    if not op:
        return None
    return OperatorOutDTO(
        id=op.id,
        user_id=op.user_id,
        branch_id=op.branch_id,
        role=op.role,
        is_active=op.is_active
    )


def update_operator(operator_id: int, data: OperatorCreateDTO) -> bool:
    existing = operator_repository.get_operator_by_id(operator_id)
    if not existing:
        return False
    op = Operator(
        id=operator_id,
        user_id=data.user_id,
        branch_id=data.branch_id,
        role=data.role,
        is_active=data.is_active
    )
    return operator_repository.update_operator(op)


def delete_operator(operator_id: int) -> bool:
    return operator_repository.delete_operator(operator_id)

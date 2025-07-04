from typing import List, Optional
from fastapi import HTTPException
from app.models.dto import OperatorCreateDTO, OperatorOutDTO
from app.models.operator import Operator
from app.repository import operator_repository
import httpx
from app.core.config import settings


async def validate_user(user_id: str) -> bool:
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(f"{settings.USER_SERVICE}/users/{user_id}", timeout=5.0)
            return resp.status_code == 200
    except httpx.RequestError:
        raise HTTPException(status_code=503, detail="No se pudo validar el usuario")


async def validate_branch(branch_id: int) -> bool:
    try:
        async with httpx.AsyncClient() as client:
            #Poner el link de la EC2 del micro laundry branch
            resp = await client.get(f"http://laundry-branch:8080/api/branches/{branch_id}", timeout=5.0)
            return resp.status_code == 200
    except httpx.RequestError:
        raise HTTPException(status_code=503, detail="No se pudo validar la sucursal")


async def create_operator(data: OperatorCreateDTO) -> OperatorOutDTO:
    if not await validate_user(data.user_id):
        raise HTTPException(status_code=400, detail="Usuario no válido")

    if not await validate_branch(data.branch_id):
        raise HTTPException(status_code=400, detail="Sucursal no válida")

    new_id = operator_repository.create_operator(data)
    return OperatorOutDTO(
        id=new_id,
        user_id=data.user_id,
        branch_id=data.branch_id,
        role=data.role,
        is_active=data.is_active
    )


async def get_all_operators() -> List[OperatorOutDTO]:
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


async def get_operator_by_id(operator_id: int) -> Optional[OperatorOutDTO]:
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


async def update_operator(operator_id: int, data: OperatorCreateDTO) -> bool:
    existing = operator_repository.get_operator_by_id(operator_id)
    if not existing:
        return False

    if not await validate_user(data.user_id):
        raise HTTPException(status_code=400, detail="Usuario no válido")

    if not await validate_branch(data.branch_id):
        raise HTTPException(status_code=400, detail="Sucursal no válida")

    op = Operator(
        id=operator_id,
        user_id=data.user_id,
        branch_id=data.branch_id,
        role=data.role,
        is_active=data.is_active
    )
    return operator_repository.update_operator(op)


async def delete_operator(operator_id: int) -> bool:
    return operator_repository.delete_operator(operator_id)

from fastapi import HTTPException
from app.service import operator_service
from app.models.dto import OperatorCreateDTO, OperatorOutDTO
from typing import List


async def create_operator(data: OperatorCreateDTO) -> OperatorOutDTO:
    return await operator_service.create_operator(data)


async def get_all_operators() -> List[OperatorOutDTO]:
    return await operator_service.get_all_operators()


async def get_operator_by_id(operator_id: int) -> OperatorOutDTO:
    result = await operator_service.get_operator_by_id(operator_id)
    if not result:
        raise HTTPException(status_code=404, detail="Operador no encontrado")
    return result


async def update_operator(operator_id: int, data: OperatorCreateDTO) -> dict:
    success = await operator_service.update_operator(operator_id, data)
    if not success:
        raise HTTPException(status_code=404, detail="No se pudo actualizar el operador")
    return {"message": "Operador actualizado correctamente"}


async def delete_operator(operator_id: int) -> dict:
    success = await operator_service.delete_operator(operator_id)
    if not success:
        raise HTTPException(status_code=404, detail="No se pudo eliminar el operador")
    return {"message": "Operador eliminado correctamente"}

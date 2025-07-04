from fastapi import HTTPException
from app.service import operator_service
from app.models.dto import OperatorCreateDTO, OperatorOutDTO
from typing import List


def create_operator(data: OperatorCreateDTO) -> OperatorOutDTO:
    return operator_service.create_operator(data)


def get_all_operators() -> List[OperatorOutDTO]:
    return operator_service.get_all_operators()


def get_operator_by_id(operator_id: int) -> OperatorOutDTO:
    result = operator_service.get_operator_by_id(operator_id)
    if not result:
        raise HTTPException(status_code=404, detail="Operador no encontrado")
    return result


def update_operator(operator_id: int, data: OperatorCreateDTO) -> dict:
    success = operator_service.update_operator(operator_id, data)
    if not success:
        raise HTTPException(status_code=404, detail="No se pudo actualizar el operador")
    return {"message": "Operador actualizado correctamente"}


def delete_operator(operator_id: int) -> dict:
    success = operator_service.delete_operator(operator_id)
    if not success:
        raise HTTPException(status_code=404, detail="No se pudo eliminar el operador")
    return {"message": "Operador eliminado correctamente"}

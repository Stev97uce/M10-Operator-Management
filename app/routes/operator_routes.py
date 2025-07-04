from fastapi import APIRouter, Depends
from app.models.dto import OperatorCreateDTO, OperatorOutDTO
from app.controller import operator_controller
from typing import List

router = APIRouter()

@router.post("/", response_model=OperatorOutDTO)
def create_operator(data: OperatorCreateDTO):
    return operator_controller.create_operator(data)

@router.get("/", response_model=List[OperatorOutDTO])
def get_all_operators():
    return operator_controller.get_all_operators()

@router.get("/{operator_id}", response_model=OperatorOutDTO)
def get_operator(operator_id: int):
    return operator_controller.get_operator_by_id(operator_id)

@router.put("/{operator_id}")
def update_operator(operator_id: int, data: OperatorCreateDTO):
    return operator_controller.update_operator(operator_id, data)

@router.delete("/{operator_id}")
def delete_operator(operator_id: int):
    return operator_controller.delete_operator(operator_id)

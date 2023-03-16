from typing import List, Optional

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from starlette import status

from ..models.auth import User
from ..models.operations import Operation, OperationKind, OperationCreate, OperationUpdate
from ..services.auth import get_current_user

from .. services.operations import OperationsService

router = APIRouter(
    prefix='/operations'
)


@router.get('/', response_model=List[Operation])
def get_operations(
    kind: Optional[OperationKind] = None,
    user: User = Depends(get_current_user),
    service: OperationsService = Depends()
):
    return service.get_list(kind=kind, user_id=user.id)


@router.get('/{operation_id}', response_model=Operation)
def get_operation(
    operation_id: int,
    user: User = Depends(get_current_user),
    service: OperationsService = Depends()
):
    return service.get(
        operation_id=operation_id,
        user_id=user.id)


@router.post('/', response_model=Operation)
def create_operation(
    operation_data: OperationCreate,
    user: User = Depends(get_current_user),
    service: OperationsService = Depends(),
):
    return service.create(
        operation_data=operation_data,
        user_id=user.id)


@router.put('/{operation_id}', response_model=Operation)
def update_operation(
    operation_id: int,
    operation_data: OperationUpdate,
    service: OperationsService = Depends(),
    user: User = Depends(get_current_user),
):
    return service.update(
        operation_id=operation_id,
        operation_data=operation_data,
        user_id=user.id)


@router.delete('/{operation_id}')
def delete_operation(
    operation_id: int,
    service: OperationsService = Depends(),
    user: User = Depends(get_current_user),
):
    service.delete(
        operation_id=operation_id,
        user_id=user.id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
from typing import Annotated
from uuid import UUID
from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException, Path
from pydantic import BaseModel, Field

from ugc_service.src.models.jwt import JWTPayload
from ugc_service.src.local.api.v1 import views as errors
from ugc_service.src.services.autorization import get_token_payload
from ugc_service.src.services.views import ViewsService, get_views_service

router = APIRouter()


class ViewsPost(BaseModel):
    film_id: UUID = Field(title="UUID фильма",
                          example="9b3c278c-665f-4055-a824-891f19cb4993")
    time: int = Field(title="unix timestamp",
                      description="Время, на которой сейчас находится пользователь при просмотре фильма.",
                      example=1611039931, gt=0, lt=9999999999)


class ViewsResponse(BaseModel):
    timestamp: int = Field(title="Время фильма",
                           example=1611039931)
    status: bool = Field(title="Успех", example=True)


@router.post('/',
             response_model=ViewsResponse,
             summary="Отправка данных")
async def views_post(
        view: ViewsPost,
        jwt: None | JWTPayload = Depends(get_token_payload),
        views_service: ViewsService = Depends(get_views_service)
):
    if jwt is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=errors.NO_AUTHORIZED)
    user_id = jwt.user_id
    status = await views_service.add_new_data(user_id, view.film_id, view.time)
    if not status:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=errors.ERROR)
    return ViewsResponse(timestamp=view.time, status=status)


@router.get('/{film_id}',
            response_model=ViewsResponse,
            summary="Получение данных")
async def views_get(
        film_id: Annotated[UUID, Path(
            description="UUID фильма",
            example="9b3c278c-665f-4055-a824-891f19cb4993"
        )],
        jwt: None | JWTPayload = Depends(get_token_payload),
        views_service: ViewsService = Depends(get_views_service)
):
    if jwt is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=errors.NO_AUTHORIZED)
    user_id = jwt.user_id
    timestamp = await views_service.get_film_time(user_id, film_id)
    if not timestamp:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=errors.NOT_FOUND)
    return ViewsResponse(timestamp=timestamp, status=True)

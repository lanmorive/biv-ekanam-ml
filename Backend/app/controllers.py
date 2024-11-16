from result import Ok, Err

from fastapi.responses import JSONResponse
from fastapi import APIRouter, HTTPException
from dishka.integrations.fastapi import FromDishka, inject

from app.schemas import PurposeEnum
from app.useCases import PurposerInterface


router = APIRouter(prefix="/purpose_of_payment")


@router.get("/{payment}")
@inject
async def get_purpose_of_payment(
        payment: str,
        purposer: FromDishka[PurposerInterface]
) -> PurposeEnum:
    match(await purposer.get(payment=payment)):
        case Ok(v):  return v
        case Err(e): raise HTTPException(status_code=422, detail=e)

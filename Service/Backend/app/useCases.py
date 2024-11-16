from abc import ABC, abstractmethod
from result import Result, as_result, Ok, Err

from app.gateways import ModelInterface
from app.schemas import PurposeEnum


class PurposerInterface(ABC):
    @abstractmethod
    async def get(self, payment: str) -> Result[PurposeEnum, str]: ...


class Purposer(PurposerInterface):
    def __init__(self, model: ModelInterface):
        self._model = model

    async def get(self, payment: str) -> Result[PurposeEnum, str]:
        try:
            return Ok(await self._model.predict(payment))

        except Exception as exc:
            return Err(exc)

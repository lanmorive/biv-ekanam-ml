from abc import ABC, abstractmethod

from app.schemas import PurposeEnum


class ModelInterface(ABC):
    @abstractmethod
    async def predict(self, text: str) -> PurposeEnum: ...


class BiGRUModel(ModelInterface):
    async def predict(self, text: str) -> PurposeEnum:
        return PurposeEnum.SERVICE

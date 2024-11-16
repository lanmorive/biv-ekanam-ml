from dishka import (
    Provider,
    Scope,
    provide,
    make_async_container
)

from app.gateways import ModelInterface, BiGRUModel
from app.useCases import PurposerInterface, Purposer


class UseCasesProvider(Provider):
    scope = Scope.REQUEST

    purposer = provide(Purposer, provides=PurposerInterface)


class GatewayProvider(Provider):
    scope = Scope.APP

    model = provide(BiGRUModel, provides=ModelInterface)


container = make_async_container(
    UseCasesProvider(),
    GatewayProvider()
)

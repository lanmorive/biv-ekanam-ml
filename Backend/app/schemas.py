from enum import Enum


class PurposeEnum(str, Enum):
    BANK_SERVICE: str = 'BANK_SERVICE'
    FOOD_GOODS: str = 'FOOD_GOODS'
    NON_FOOD_GOODS: str = 'NON_FOOD_GOODS'
    LEASING: str = 'LEASING'
    LOAN: str = 'LOAN'
    REALE_STATE: str = 'REALE_STATE'
    SERVICE: str = 'SERVICE'
    TAX: str = 'TAX'
    NOT_CLASSIFIED: str = 'NOT_CLASSIFIED'

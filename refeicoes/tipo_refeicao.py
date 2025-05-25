from enum import Enum

class TipoRefeicao(str, Enum):
    CAFE_MANHA = "café da manhã"
    ALMOCO = "almoço"
    LANCHE = "lanche"
    JANTAR = "jantar"

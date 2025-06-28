from dao.dao import DAO
from model.nutricionista import Nutricionista

class NutricionistaDAO(DAO):
    def __init__(self):
        super().__init__('nutricionistas.pkl')

    def add(self, nutricionista: Nutricionista):
        if nutricionista is not None and isinstance(nutricionista, Nutricionista) and isinstance(nutricionista.cpf, str):
            super().add(nutricionista.cpf, nutricionista)

    def update(self, nutricionista: Nutricionista):
        if nutricionista is not None and isinstance(nutricionista, Nutricionista) and isinstance(nutricionista.cpf, str):
            super().update(nutricionista.cpf, nutricionista)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
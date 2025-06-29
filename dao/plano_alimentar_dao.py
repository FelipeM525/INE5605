from dao.dao import DAO
from model.plano_alimentar import PlanoAlimentar

class PlanoAlimentarDAO(DAO):
    def __init__(self):
        super().__init__('planos_alimentares.pkl')

    def add(self, key: str, plano_alimentar: PlanoAlimentar):
        if isinstance(plano_alimentar, PlanoAlimentar) and isinstance(key, str):
            super().add(key, plano_alimentar)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str):
        if isinstance(key, str):
            return super().remove(key)
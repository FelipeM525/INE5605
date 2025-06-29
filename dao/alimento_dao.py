from dao.dao import DAO
from model.alimento import Alimento

class AlimentoDAO(DAO):
    def __init__(self):
        super().__init__('alimentos.pkl')

    def add(self, key: str, alimento: Alimento):
        if isinstance(alimento, Alimento) and isinstance(key, str):
            super().add(key, alimento)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)
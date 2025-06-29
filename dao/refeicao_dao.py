from dao.dao import DAO
from model.refeicao import Refeicao

class RefeicaoDAO(DAO):
    def __init__(self):
        super().__init__('refeicoes.pkl')

    def add(self, key: str, refeicao: Refeicao):
        if isinstance(refeicao, Refeicao) and isinstance(key, str):
            super().add(key, refeicao)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str):
        if isinstance(key, str):
            return super().remove(key)
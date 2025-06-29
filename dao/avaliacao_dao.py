from dao.dao import DAO
from model.avaliacao import Avaliacao

class AvaliacaoDAO(DAO):
    def __init__(self):
        super().__init__('avaliacoes.pkl')

    def add(self, key: str, avaliacao: Avaliacao):
        if isinstance(avaliacao, Avaliacao) and isinstance(key, str):
            super().add(key, avaliacao)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str):
        if isinstance(key, str):
            return super().remove(key)
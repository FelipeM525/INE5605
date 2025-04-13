from avaliacao import Avaliacao
from usuario import Usuario


class Nutricionista(Usuario):
    def __init__(self, nome: str, email: str, senha: str, cpf: str, clinica: str, crn: str, avaliacoes: list[Avaliacao]):
        super().__init__(nome, email, senha, cpf)
        self.__clinica = clinica
        self.__crn = crn
        self.__avaliacoes = avaliacoes

    @property
    def clinica(self):
        return self.__clinica

    @clinica.setter
    def clinica(self, clinica):
        self.__clinica = clinica

    @property
    def crn(self):
        return self.__crn

    @crn.setter
    def crn(self, crn):
        self.__crn = crn

    @property
    def avaliacoes(self):
        return self.__avaliacoes

    def adicionar_avaliacao(self, avaliacao: Avaliacao):
        self.__avaliacoes.append(avaliacao)
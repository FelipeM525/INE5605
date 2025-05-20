from usuario import Usuario
from model.clinica import Clinica
from model.avaliacao import Avaliacao



class Nutricionista(Usuario):
    def __init__(self, nome: str, email: str, senha: str, cpf: str, clinica: Clinica, crn: str, avaliacoes: list):
        super().__init__(nome, email, senha, cpf)
        self.__clinica = clinica
        self.__crn = crn
        self.__avaliacoes = avaliacoes

    @property
    def clinica(self):
        return self.__clinica

    @clinica.setter
    def clinica(self, clinica: Clinica):
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

    def adicionar_avaliacao(self, avaliacao):
        if isinstance(avaliacao, Avaliacao):
            self.__avaliacoes.append(avaliacao)

    def cadastrar(self):
        print(f"Nutricionista {self.nome} cadastrado com sucesso.")
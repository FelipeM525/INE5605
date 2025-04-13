from objetivo import Objetivo
from plano_alimentar import PlanoAlimentar
from usuario import Usuario


class Cliente(Usuario):
    def __init__(self, nome: str, email: str, senha: str, cpf: str, idade: int, genero: str, peso: float, altura: float, objetivo: Objetivo, plano_alimentar: PlanoAlimentar):
        super().__init__(nome, email, senha, cpf)
        self.__idade = idade
        self.__genero = genero
        self.__peso = peso
        self.__altura = altura
        self.__objetivo = objetivo
        self.__plano_alimentar = plano_alimentar

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, peso):
        self.__peso = peso

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura):
        self.__altura = altura


    @property
    def objetivo(self):
        return self.__objetivo

    @objetivo.setter
    def objetivo(self, objetivo):
        self.__objetivo = objetivo

    @property
    def plano_alimentar(self):
        return self.__plano_alimentar

    def add_plano_alimentar(self,  plano_alimentar: PlanoAlimentar):
        self.__plano_alimentar = plano_alimentar

    def calcular_imc(self):
        if self.__altura <= 0:
            return 0
        imc = self.__peso / (self.__altura ** 2)
        return round(imc, 2)

    def calcular_tmb(self):
        if self.__genero == 'masculino':
            tmb = 88.36 + (13.4 * self.__peso) + (4.8 * self.__altura) - (5.7 * self.__idade)
        elif self.__genero == 'feminino':
            tmb = 447.6 + (9.2 * self.__peso) + (3.1 * self.__altura) - (4.3 * self.__idade)
        else:
            return "genero inválido. Use 'masculino' ou 'feminino'."

        return round(tmb, 2)
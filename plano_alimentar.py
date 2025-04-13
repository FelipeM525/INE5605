from refeicao import Refeicao:
from nutricionista import Nutricionista
from cliente import Cliente

class PlanoAlimentar:
    def __init__(self, refeicoes: list[Refeicao], nutricionista: Nutricionista, cliente: Cliente):
        self.__refeicoes = refeicoes
        self.__nutricionista = nutricionista
        self.__cliente = cliente
    
    @property
    def refeicoes(self):
        return self.__refeicoes
    
    @property
    def nutricionista(self):
        return self.__nutricionista

    @nutricionista.setter
    def nutricionista(self, nutricionista: Nutricionista):
        if isinstance(nutricionista, Nutricionista):
            self.__nutricionista = nutricionista
        
    @property
    def cliente(self):
        return self.__cliente
    
    @cliente.setter
    def cliente(self, cliente: Cliente):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente

    def adicionar_refeicao(self, refeicao: Refeicao):
        if isinstance(refeicao, Refeicao):
            self.__refeicoes.append(refeicao)
from refeicao import Refeicao:

class PlanoAlimentar:
    def __init__(self, refeicoes: list[Refeicao], nutricionista: Nutricionista, cliente: Cliente):
        self.__refeicoes = refeicoes
        self.__nutricionista = nutricionista
        self.__cliente = cliente
    
    @property
    def refeicoes(self):
        return self.__refeicoes
    
    @refeicoes.setter
    def refeicoes(self, refeicoes: list[Refeicao]):
        self.__refeicoes = refeicoes
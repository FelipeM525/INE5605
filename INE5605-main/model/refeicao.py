from model.alimento import Alimento

class Refeicao:
    def __init__(self, alimentos: list[Alimento], tipo: str):
        self.__alimentos = alimentos
        self.__tipo = tipo
    
    @property
    def alimentos(self):
        return self.__alimentos

    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, tipo: str):
        self.__tipo = tipo
    
    def adicionar_alimento(self, alimento: Alimento):
        if isinstance(alimento, Alimento):
            self.__alimentos.append(alimento)
    
    def calorias_totais(self):
        return sum(alimento.calorias for alimento in self.__alimentos)
    
    def carboidratos_totais(self):
        return sum(alimento.carboidratos for alimento in self.__alimentos)
    
    def gorduras_totais(self):
        return sum(alimento.gorduras for alimento in self.__alimentos)

    def proteinas_totais(self):
        return sum(alimento.proteinas for alimento in self.__alimentos)
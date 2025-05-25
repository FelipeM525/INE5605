from alimentos.alimento import Alimento

class Refeicao:
    def __init__(self, nome: str, alimentos: list[Alimento], tipo):
        self.__nome = nome
        self.__alimentos = alimentos
        self.__tipo = tipo

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

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

    def __str__(self):
        alimentos_str = ", ".join([alimento.__str__() for alimento in self.__alimentos])
        return (
            f"Refeição: {self.__nome}\n"
            f"Tipo: {self.__tipo}\n"
            f"Alimentos: {alimentos_str}\n"
            f"Calorias Totais: {self.calorias_totais()} kcal\n"
            f"Carboidratos Totais: {self.carboidratos_totais()}g\n"
            f"Gorduras Totais: {self.gorduras_totais()}g\n"
            f"Proteínas Totais: {self.proteinas_totais()}g"
        )
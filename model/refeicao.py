from model.alimento import Alimento

class Refeicao:
    def __init__(self, codigo: str, alimentos: list[Alimento], tipo):
        self.__codigo = codigo
        self.__alimentos = alimentos
        self.__tipo = tipo

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, nome: str):
        self.__codigo = nome

    @property
    def alimentos(self):
        return self.__alimentos

    @alimentos.setter
    def alimentos(self, alimentos: list[Alimento]):
        self.__alimentos = alimentos

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
            f"Refeição: {self.__codigo}\n"
            f"Tipo: {self.__tipo}\n"
            f"Alimentos: {alimentos_str}\n"
            f"Calorias Totais: {self.calorias_totais()} kcal\n"
            f"Carboidratos Totais: {self.carboidratos_totais()}g\n"
            f"Gorduras Totais: {self.gorduras_totais()}g\n"
            f"Proteínas Totais: {self.proteinas_totais()}g"
        )
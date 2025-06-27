class Alimento:
    def __init__(self, codigo: str, calorias: int, carboidratos: int, gorduras: int, proteinas: int):
        self.__codigo = codigo
        self.__calorias = calorias
        self.__carboidratos = carboidratos
        self.__gorduras = gorduras
        self.__proteinas = proteinas
    
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo: str):
        self.__codigo = codigo
    
    @property
    def calorias(self):
        return self.__calorias
    
    @calorias.setter
    def calorias(self, calorias: int):
        self.__calorias = calorias

    @property
    def carboidratos(self):
        return self.__carboidratos

    @carboidratos.setter
    def carboidratos(self, carboidratos: int):
        self.__carboidratos = carboidratos
    
    @property
    def gorduras(self):
        return self.__gorduras

    @gorduras.setter
    def gorduras(self, gorduras: int):
        self.__gorduras = gorduras
    
    @property
    def proteinas(self):
        return self.__proteinas
    
    @proteinas.setter
    def proteinas(self, proteinas: int):
        self.__proteinas = proteinas

    def __str__(self):
        return (
            f"Alimento: {self.__nome}, "
            f"Calorias: {self.__calorias} kcal, "
            f"Carboidratos: {self.__carboidratos}g, "
            f"Gorduras: {self.__gorduras}g, "
            f"Proteínas: {self.__proteinas}g"
        )

class Alimento:
    def __init__(self, nome: str, calorias: int, carboidratos: int, gorduras: int, proteinas: int):
        self.__nome = nome
        self.__calorias = calorias
        self.__carboidratos = carboidratos
        self.__gorduras = gorduras
        self.__proteinas = proteinas
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome
    
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

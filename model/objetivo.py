class Objetivo:

    def __init__(self, meta: str, quantidade: int, tempo: int):
        self.__meta = meta
        self.__quantidade = quantidade
        self.__tempo = tempo
    
    @property
    def meta(self):
        return self.__meta
    
    @meta.setter
    def meta(self, meta: str):
        self.__meta = meta
    
    @property
    def quantidade(self):
        return self.__quantidade
    
    @quantidade.setter
    def quantidade(self, quantidade: int):
        self.__quantidade = quantidade

    @property
    def tempo(self):
        return self.__tempo
    
    @tempo.setter
    def tempo(self, tempo: int):
        self.__tempo = tempo
    
    
class Avaliacao:
    def __init__(self, cliente, nutricionista, data: str, imc: float, taxa_mb: int):
        from usuarios.model.cliente import Cliente
        from usuarios.model.nutricionista import Nutricionista

        if isinstance(cliente, Cliente) and isinstance(nutricionista, Nutricionista):
            self.__cliente = cliente
            self.__nutricionista = nutricionista
        self.__data = data
        self.__imc = imc
        self.__taxa_mb = taxa_mb

    @property
    def cliente(self):
        return self.__cliente

    @property
    def nutricionista(self):
        return self.__nutricionista

    @property
    def data(self):
        return self.__data

    @property
    def imc(self):
        return self.__imc

    @property
    def taxa_mb(self):
        return self.__taxa_mb

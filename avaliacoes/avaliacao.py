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

    def __str__(self):
        return (
            f"Avaliação:\n"
            f"Cliente: {self.__cliente}\n"
            f"Nutricionista: {self.__nutricionista}\n"
            f"Data: {self.__data}\n"
            f"IMC: {self.__imc}\n"
            f"Taxa Metabólica Basal: {self.__taxa_mb} kcal"
        )

class Avaliacao:
    def __init__(self, nome: str, cliente, nutricionista, data: str, imc: float, taxa_mb: int):
        from model.cliente import Cliente
        from model.nutricionista import Nutricionista

        self.__nome = nome
        if isinstance(cliente, Cliente) and isinstance(nutricionista, Nutricionista):
            self.__cliente = cliente
            self.__nutricionista = nutricionista
        self.__data = data
        self.__imc = imc
        self.__taxa_mb = taxa_mb

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        from model.cliente import Cliente
        if isinstance(cliente, Cliente):
            self.__cliente = cliente

    @property
    def nutricionista(self):
        return self.__nutricionista
    
    @nutricionista.setter
    def nutricionista(self, nutricionista):
        from model.nutricionista import Nutricionista
        if isinstance(nutricionista, Nutricionista):
            self.__nutricionista = nutricionista

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data

    @property
    def imc(self):
        return self.__imc
    
    @imc.setter
    def imc(self, imc: float):
        self.__imc = imc

    @property
    def taxa_mb(self):
        return self.__taxa_mb

    @taxa_mb.setter
    def taxa_mb(self, taxa_mb: int):
        self.__taxa_mb = taxa_mb

    def __str__(self):
        cliente_info = self.cliente.nome if self.cliente else "N/A"
        nutri_info = str(self.nutricionista) if self.nutricionista else "N/A"
        return (
            f"--- Avaliação: {self.nome} ---\n"
            f"Cliente: {cliente_info}\n"
            f"Nutricionista: {nutri_info}\n"
            f"Data: {self.data}\n"
            f"IMC: {self.imc}\n"
            f"Taxa Metabólica Basal: {self.taxa_mb} kcal"
        )
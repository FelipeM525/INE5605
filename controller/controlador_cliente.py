from model.cliente import Cliente

class ControladorCliente:

    @property
    def __init__(self):
        self.__clientes = []

    def calcular_imc(cliente: Cliente):
        if isinstance(cliente, Cliente):
            return cliente.calcular_imc()
        else:
            raise Exception("Nao foi possivel calcular o IMC, Parametro invalido!")

    def calcular_tmb(cliente: Cliente):
        if isinstance(cliente, Cliente):
            return cliente.calcular_tmb()
        else:
            raise Exception("Nao foi possivel calcular o TMB, Parametro invalido!")
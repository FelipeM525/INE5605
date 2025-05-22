from model.cliente import Cliente
from exception.jahCadastradoException import JahCadastradoException

class ControladorCliente:

    @property
    def __init__(self):
        self.__clientes = []

    def buscar_cliente_por_cpf(self, cpf: str):
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                return cliente
            
        return None

    def incluir_cliente(self):
        novo_cliente = self.tela_cliente.cadastrar_cliente()

        if not isinstance(novo_cliente, Cliente):
            raise ValueError("Valores inválidos")
        
        if self.buscar_cliente_por_cpf(novo_cliente.cpf):
            raise JahCadastradoException()
        
        else:
            self.__clientes.append(novo_cliente)

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
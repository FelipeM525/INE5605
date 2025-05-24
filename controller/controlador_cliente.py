from model.cliente import Cliente
from exception.jahCadastradoException import JahCadastradoException
from exception.cadastroInexistenteException import CadastroInexistenteException
from view.tela_cliente import TelaCliente

class ControladorCliente:

    def __init__(self):
        self.__clientes = []
        self.tela_cliente = TelaCliente()

    def buscar_cliente_por_cpf(self, cpf: str):
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                return cliente
            
        return None

    def incluir_cliente(self):
        novo_cliente = self.tela_cliente.pegar_dados_cliente()

        if not isinstance(novo_cliente, Cliente):
            raise ValueError("Valores inválidos")
        
        if self.buscar_cliente_por_cpf(novo_cliente.cpf):
            raise JahCadastradoException()
        
        else:
            self.__clientes.append(novo_cliente)

    def remover_cliente(self):
        cpf = self.tela_cliente.selecionar_cliente_cpf()
        cliente = self.buscar_cliente_por_cpf(cpf)

        if cliente:
            self.__clientes.remove(cliente)
        
        else:
            raise CadastroInexistenteException()
    
    def listar_clientes(self):
        lista_de_clientes = self.__clientes
        self.tela_cliente.listar_clientes(lista_de_clientes)
        
    def alterar_cliente(self):
        cpf = self.tela_cliente.selecionar_cliente_cpf()
        cliente = self.buscar_cliente_por_cpf(cpf)

        if cliente:
            self.tela_cliente.mostrar_mensagem("Digite os novos dados para o cliente")
            
            cliente_com_novos_dados = self.tela_cliente.pegar_dados_cliente()

            cliente.nome = cliente_com_novos_dados.nome
            cliente.email = cliente_com_novos_dados.email
            cliente.senha = cliente_com_novos_dados.senha
            cliente.idade = cliente_com_novos_dados.idade
            cliente.genero = cliente_com_novos_dados.genero
            cliente.peso = cliente_com_novos_dados.peso
            cliente.altura = cliente_com_novos_dados.altura
            
            cliente.objetivo = cliente_com_novos_dados.objetivo
            
            self.tela_cliente.mostrar_mensagem("Cliente alterado com sucesso!")
            self.tela_cliente.mostrar_dados_do_cliente(cliente)
        
        else:
            raise CadastroInexistenteException()

#    def calcular_imc(cliente: Cliente):
#        if isinstance(cliente, Cliente):
#            return cliente.calcular_imc()
#        else:
#            raise Exception("Nao foi possivel calcular o IMC, Parametro invalido!")

#    def calcular_tmb(cliente: Cliente):
#        if isinstance(cliente, Cliente):
#            return cliente.calcular_tmb()
#        else:
#            raise Exception("Nao foi possivel calcular o TMB, Parametro invalido!")
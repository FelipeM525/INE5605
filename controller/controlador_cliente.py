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
        novo_cliente = self.tela_cliente.cadastrar_cliente()

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
        
    def alterar_cliente(self):
        cpf = self.tela_cliente.selecionar_cliente_cpf()
        cliente = self.buscar_cliente_por_cpf(cpf)

        if cliente:
            opcoes = {
                "1": ("nome", str),
                "2": ("email", str),
                "3": ("senha", str),
                "4": ("idade", int),
                "5": ("genero", str),
                "6": ("peso", float),
                "7": ("altura", float),
            }
        
            while True:
                self.tela_cliente.mostrar_dados_do_cliente(cliente)
                opcao = self.tela_cliente.mostrar_menu_alteracao()

                if opcao == "0":
                    self.tela_cliente.mostrar_mensagem("Alterações concluídas")
                    break

                elif opcao == "8":
                    novos_dados_obj = self.tela_cliente.pegar_dados_novo_objetivo()
                    cliente.objetivo.meta = novos_dados_obj["meta"]
                    cliente.objetivo.quantidade = novos_dados_obj["quantidade"]
                    cliente.objetivo.tempo = novos_dados_obj["tempo"]
                    self.tela_cliente.mostrar_mensagem("Objetivo alterado com sucesso")

                elif opcao in opcoes:
                    atributo, tipo = opcoes[opcao]
                    novo_valor_str = self.tela_cliente.pegar_dados_valor_alteracao(atributo)

                    try:
                        novo_valor = tipo(novo_valor_str)
                        setattr(cliente, atributo, novo_valor)
                    except ValueError:
                        self.tela_cliente.mostrar_mensagem("Valor inválido para este campo")
                    
                else:
                    self.tela_cliente.mostrar_mensagem("Opcao inválida")
            
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
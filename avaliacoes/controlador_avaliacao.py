from usuarios.controller.controlador_cliente import ControladorCliente
from usuarios.controller.controlador_nutricionista import ControladorNutricionista
from exception.cadastroInexistenteException import CadastroInexistenteException
from avaliacoes.avaliacao import Avaliacao
from usuarios.model.cliente import Cliente
from usuarios.model.nutricionista import Nutricionista
from avaliacoes.tela_avaliacao import TelaAvaliacao


class ControladorAvaliacao:
    def __init__(self):# (self, controlador_cliente: ControladorCliente, controlador_nutricionista: ControladorNutricionista):
        self.__tela_avaliacao = TelaAvaliacao()
        self.__controlador_cliente = ControladorCliente() #substituindo esse
        self.__controlador_nutricionista = ControladorNutricionista() #substituindo esse
        #self.__controlador_cliente = controlador_cliente
        #elf.__controlador_nutricionista = controlador_nutricionista

        self.__avaliacoes = []
    
    def abre_tela(self):
        while True:
            try:
                opcao = self.__tela_avaliacao.mostrar_menu()
                if opcao == 1:
                    self.incluir_avaliacao()
                elif opcao == 2:
                    self.lista_avaliacao()
                elif opcao == 3:
                    self.remover_avaliacao()
                elif opcao == 0:
                    break
                else:
                    self.__tela_avaliacao.mostra_mensagem("Opção inválida. Tente novamente.")
            except ValueError:
                self.__tela_avaliacao.mostra_mensagem("Entrada inválida. Por favor, digite um número.")
            except CadastroInexistenteException as e:
                self.__tela_avaliacao.mostra_mensagem(e)
            except Exception as e:
                self.__tela_avaliacao.mostra_mensagem(f"Ocorreu um erro: {e}")

    def incluir_avaliacao(self):
        dados_avaliacao = self.__tela_avaliacao.pega_dados_avaliacao(self)
        cliente: Cliente = self.__controlador_cliente.buscar_cliente_por_cpf(dados_avaliacao.cpf_cliente)
        nutricionista: Nutricionista = self.__controlador_nutricionista.buscar_nutricionista_por_cpf(dados_avaliacao.cpf_nutricionista)

        avaliacao = Avaliacao(cliente, nutricionista, dados_avaliacao.data, dados_avaliacao.imc, dados_avaliacao.tmb)

        self.__avaliacoes.append(avaliacao)

        self.__tela_avaliacao.mostra_mensagem(f"Avaliacao de {avaliacao.cliente.nome} incluida com sucesso!")

#    # ALTERAÇÃO 3 (BUG FIX): Corrigido o método para funcionar corretamente
#    def incluir_avaliacao(self):
#        dados_avaliacao = self.__tela_avaliacao.pega_dados_avaliacao()
#        
#        cliente = self.__controlador_cliente.buscar_cliente_por_cpf(dados_avaliacao["cpf_cliente"])
#        nutricionista = self.__controlador_nutricionista.buscar_nutricionista_por_cpf(dados_avaliacao["cpf_nutricionista"])
#
#        if not cliente or not nutricionista:
#            raise CadastroInexistenteException("Cliente ou Nutricionista não encontrado.")
#
#        avaliacao = Avaliacao(cliente, nutricionista, dados_avaliacao["data"], dados_avaliacao["imc"], dados_avaliacao["tmb"])
#        self.__avaliacoes.append(avaliacao)
#        self.__tela_avaliacao.mostra_mensagem(f"Avaliação de {cliente.nome} incluída com sucesso!")

    def list_avaliacao_cliente(self, cpf_cliente):
        for avaliacao in self.__avaliacoes:
            if avaliacao.cliente.cpf == cpf_cliente:
                self.__tela_avaliacao.mostra_avaliacao(avaliacao.__dict__)

    def lista_avaliacao_nutricionista(self, cpf_nutricionista):
        for avaliacao in self.__avaliacoes:
            if avaliacao.nutricionista.cpf == cpf_nutricionista:
                self.__tela_avaliacao.mostra_avaliacao(avaliacao.__dict__)


    def lista_avaliacao(self):
        for avaliacao in self.__avaliacoes:
            self.__tela_avaliacao.mostra_avaliacao(avaliacao.__dict__)

    def remover_avaliacao(self):
        cpf_cliente = self.__tela_avaliacao.excluir_avaliacao()
        avaliacao = self.busca_avaliacao_por_cpf_cliente(cpf_cliente)

        if avaliacao:
            self.__avaliacoes.remove(avaliacao)
            return self.__tela_avaliacao.mostra_mensagem(f"Avaliacao de {avaliacao.cliente.nome} removida com sucesso!")
        else:
            raise CadastroInexistenteException()


    def busca_avaliacao_por_cpf_cliente(self, cpf_cliente):
        for avaliacao in self.__avaliacoes:
            if avaliacao.cliente.cpf == cpf_cliente:
                return avaliacao

        return None
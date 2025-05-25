from avaliacoes.avaliacao import Avaliacao
from avaliacoes.tela_avaliacao import TelaAvaliacao
from core.controlador_sistema import ControladorSistema
from exception.avaliacao_inexistente_exception import AvaliacaoInexistenteException
from usuarios.controller.controlador_cliente import ControladorCliente
from usuarios.controller.controlador_nutricionista import ControladorNutricionista
from usuarios.model.cliente import Cliente
from usuarios.model.nutricionista import Nutricionista


class ControladorAvaliacao:
    def __init__(self, controlador_sistema: ControladorSistema, controlador_cliente: ControladorCliente, controlador_nutricionista: ControladorNutricionista):
        self.__tela_avaliacao = TelaAvaliacao()
        self.__controlador_cliente = controlador_cliente
        self.__controlador_nutricionista = controlador_nutricionista
        self.__controlador_sistema = controlador_sistema
        self.__avaliacoes = []

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_avaliacao,
            2: self.lista_avaliacao,
            3: self.remover_avaliacao,
            0: self.retornar
        }

        while True:
            opcao = self.__tela_avaliacao.mostrar_menu()

            if opcao == 0:
                self.retornar()
                break

            funcao_escolhida = lista_opcoes.get(opcao)

            if funcao_escolhida:
                funcao_escolhida()
            else:
                self.__tela_avaliacao.mostra_mensagem("Opção inválida. Tente novamente.")


    def incluir_avaliacao(self):
        dados_avaliacao = self.__tela_avaliacao.pega_dados_avaliacao()

        cliente: Cliente = self.__controlador_cliente.buscar_cliente_por_cpf(dados_avaliacao["cpf_cliente"])
        nutricionista: Nutricionista = self.__controlador_nutricionista.buscar_nutricionista_por_cpf(dados_avaliacao["cpf_nutricionista"])

        avaliacao = Avaliacao(cliente, nutricionista, dados_avaliacao["data"], dados_avaliacao["imc"], dados_avaliacao["tmb"])

        self.__avaliacoes.append(avaliacao)

        self.__tela_avaliacao.mostra_mensagem(f"Avaliacao de {avaliacao.cliente.nome} incluida com sucesso!")


    def list_avaliacao_cliente(self, cpf_cliente):

        if self.veriricar_se_avaliacoes_existem():
            for avaliacao in self.__avaliacoes:
                if avaliacao.cliente.cpf == cpf_cliente:
                    self.__tela_avaliacao.mostra_avaliacao(avaliacao)

    def lista_avaliacao_nutricionista(self, cpf_nutricionista):
        if self.veriricar_se_avaliacoes_existem():
            for avaliacao in self.__avaliacoes:
                if avaliacao.nutricionista.cpf == cpf_nutricionista:
                    self.__tela_avaliacao.mostra_avaliacao(avaliacao)


    def lista_avaliacao(self):
        if self.veriricar_se_avaliacoes_existem():
            for avaliacao in self.__avaliacoes:
                self.__tela_avaliacao.mostra_avaliacao(avaliacao)

    def remover_avaliacao(self):
        cpf_cliente = self.__tela_avaliacao.seleciona_avaliacao()
        avaliacao = self.busca_avaliacao_por_cpf_cliente(cpf_cliente)

        try:
            if avaliacao:
                self.__avaliacoes.remove(avaliacao)
                return self.__tela_avaliacao.mostra_mensagem(f"Avaliacao de {avaliacao.cliente.nome} removida com sucesso!")
            else:
                raise AvaliacaoInexistenteException()
        except AvaliacaoInexistenteException:
            return self.__tela_avaliacao.mostra_mensagem(f"Avaliacao de {cpf_cliente} nao existe!")


    def busca_avaliacao_por_cpf_cliente(self, cpf_cliente):
        for avaliacao in self.__avaliacoes:
            if avaliacao.cliente.cpf == cpf_cliente:
                return avaliacao

        return None

    def retornar(self):
        pass

    def veriricar_se_avaliacoes_existem(self):
        if len(self.__avaliacoes) == 0:
            self.__tela_avaliacao.mostra_mensagem("Nao ha avaliacoes cadastradas!")
            return False
        else:
            return True
from alimentos.alimento import Alimento
from alimentos.tela_alimento import TelaAlimento
from core.controlador_sistema import ControladorSistema
from exception.alimento_inexistente_exception import AlimentoInexistenteException


class ControladorAlimento:
    def __init__(self, controlador_sistema: ControladorSistema):
        self.__tela_alimento = TelaAlimento()
        self.__alimentos = []
        self.__controlador_sistema = controlador_sistema

    def incluir_alimento(self):
        dados_alimento = self.__tela_alimento.pega_dados_alimento()
        alimento: Alimento = self.busca_alimento_por_nome(dados_alimento["nome"])

        try:
            if alimento:
                self.__alimentos.append(alimento)
                self.__tela_alimento.mostra_mensagem("Alimento incluido com sucesso!")
            else:
                raise AlimentoInexistenteException
        except AlimentoInexistenteException:
            self.__tela_alimento.mostra_mensagem("Alimento nao existe!")

    def busca_alimento_por_nome(self, nome):
        for alimento in self.__alimentos:
            if alimento.nome == nome:
                return alimento

        return None

    def listar_alimento(self):
        if len(self.__alimentos) == 0:
            self.__tela_alimento.mostra_mensagem("Nao ha alimentos cadastrados!")
        else:
            for alimento in self.__alimentos:
                self.__tela_alimento.mostra_alimento(alimento)

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_alimento, 2: self.listar_alimento, 3: self.retornar}

        continua = True
        opcao = self.__tela_alimento.mostrar_menu()

        if opcao < 1 or opcao > 3:
            self.__tela_alimento.mostra_mensagem("Opcao invalida!")
            self.retornar()

        while continua:
            lista_opcoes[opcao]()

    def retornar(self):
        self.__controlador_sistema.inicializa_sistema()

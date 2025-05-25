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
        nome_alimento = dados_alimento["nome"]
        if self.busca_alimento_por_nome(nome_alimento):
            self.__tela_alimento.mostra_mensagem(f"Alimento com o nome '{nome_alimento}' já existe!")
        else:
            novo_alimento = Alimento(
                nome=dados_alimento["nome"],
                calorias=dados_alimento["calorias"],
                carboidratos=dados_alimento["carboidratos"],
                gorduras=dados_alimento["gorduras"],
                proteinas=dados_alimento["proteinas"]
            )
            self.__alimentos.append(novo_alimento)
            self.__tela_alimento.mostra_mensagem("Alimento incluido com sucesso!")

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
        lista_opcoes = {1: self.incluir_alimento, 2: self.listar_alimento, 0: self.retornar}
        while True:
            opcao = self.__tela_alimento.mostrar_menu()
            if opcao == 0:
                self.retornar()
                break

            funcao_escolhida = lista_opcoes.get(opcao)
            if funcao_escolhida:
                funcao_escolhida()
            else:
                self.__tela_alimento.mostra_mensagem("Opção inválida, tente novamente.")

    def retornar(self):
        self.__controlador_sistema.inicializa_sistema()

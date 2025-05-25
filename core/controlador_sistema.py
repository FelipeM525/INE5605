from core.tela_sistema import TelaSistema
from usuarios.controller.controlador_cliente import ControladorCliente
from usuarios.controller.controlador_nutricionista import ControladorNutricionista
from alimentos.controlador_alimento import ControladorAlimento
from avaliacoes.controlador_avaliacao import ControladorAvaliacao
from refeicoes.controlador_refeicao import ControladorRefeicao
from plano.controlador_plano_alimentar import ControladorPlanoAlimentar

class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_cliente = ControladorCliente()
        self.__controlador_nutricionista = ControladorNutricionista()
        self.__controlador_alimento = ControladorAlimento()
        self.__controlador_avaliacao = ControladorAvaliacao(self.__controlador_cliente, self.__controlador_nutricionista)
        self.__controlador_refeicao = ControladorRefeicao(self.__controlador_alimento)
        self.__controlador_plano_alimentar = ControladorPlanoAlimentar(self.__controlador_cliente, self.__controlador_nutricionista, self.__controlador_refeicao)
        self.__controlador_cliente = ControladorCliente(self)
        self.__controlador_nutricionista = ControladorNutricionista(self)
        self.__controlador_alimento = ControladorAlimento(self)
        self.__controlador_avaliacao = ControladorAvaliacao(self, self.__controlador_cliente, self.__controlador_nutricionista)
        self.__controlador_refeicao = ControladorRefeicao(self.__controlador_alimento, self)

    def inicializa_sistema(self):
        while True:
            opcao = self.__tela_sistema.tela_opcoes()

            if opcao == 1:
                self.__controlador_cliente.abre_tela()
            elif opcao == 2:
                self.__controlador_nutricionista.abre_tela()
            elif opcao == 3:
                self.__controlador_alimento.abre_tela()
            elif opcao == 4:
                self.__controlador_avaliacao.abre_tela()
            elif opcao == 5:
                self.__controlador_refeicao.abre_tela()
            elif opcao == 6:
                self.__controlador_plano_alimentar.abre_tela()
            elif opcao == 0:
                print("Encerrando o sistema")
                break
            else:
                print("Opção inválida. Selecione uma das opções disponíveis")
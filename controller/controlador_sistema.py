import tkinter as tk
from view.tela_sistema_tkinter import TelaSistemaTk
from controller.controlador_cliente import ControladorCliente
from controller.controlador_nutricionista import ControladorNutricionista
from controller.controlador_alimento import ControladorAlimento
from controller.controlador_avaliacao import ControladorAvaliacao
from controller.controlador_refeicao import ControladorRefeicao
from controller.controlador_plano_alimentar import ControladorPlanoAlimentar


class ControladorSistema:

    def __init__(self):
        self.__root = tk.Tk()
        self.__tela_sistema = TelaSistemaTk(self.__root, self)
        self.__controlador_cliente = ControladorCliente(self)
        self.__controlador_nutricionista = ControladorNutricionista(self)
        self.__controlador_alimento = ControladorAlimento(self)
        self.__controlador_refeicao = ControladorRefeicao(self.__controlador_alimento, self)
        self.__controlador_plano_alimentar = ControladorPlanoAlimentar(self.__controlador_cliente,
                                                                       self.__controlador_nutricionista,
                                                                       self.__controlador_refeicao, self)
        self.__controlador_avaliacao = ControladorAvaliacao(self, self.__controlador_cliente,
                                                            self.__controlador_nutricionista)

    def inicializa_sistema(self):
        self.__root.mainloop()

    def chama_controlador_cliente(self):
        self.__root.withdraw()
        self.__controlador_cliente.abre_tela()

    def chama_controlador_nutricionista(self):
        self.__root.withdraw()
        self.__controlador_nutricionista.abre_tela()

    def chama_controlador_alimento(self):
        self.__root.withdraw()
        self.__controlador_alimento.abre_tela()

    def chama_controlador_refeicao(self):
        self.__root.withdraw()
        self.__controlador_refeicao.abre_tela()

    def chama_controlador_plano_alimentar(self):
        self.__root.withdraw()
        self.__controlador_plano_alimentar.abre_tela()

    def chama_controlador_avaliacao(self):
        self.__root.withdraw()
        self.__controlador_avaliacao.abre_tela()

    def reabre_tela_principal(self):
        self.__root.deiconify()

    @property
    def root(self):
        return self.__root
from controller.controlador_cliente import ControladorCliente
from model.avaliacao import Avaliacao
from view.tela_avaliacao import TelaAvaliacao


class ControladorAvaliacao:
    def __init__(self):
        self.__tela_avaliacao = TelaAvaliacao()
        self.__controlador_cliente = ControladorCliente()
        self.__avaliacoes = []

    def incluir_avaliacao(self):
        dados_avaliacao = self.__tela_avaliacao.pega_dados_avaliacao(self)

        Avaliacao()
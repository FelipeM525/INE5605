from exception.jahCadastradoException import JahCadastradoException
from view.tela_alimento import TelaAlimento


class ControladorAlimento:
    def __init__(self):
        self.__tela_alimento = TelaAlimento()
        self.__alimentos = []

    def incluir_alimento(self):
        dados_alimento = self.__tela_alimento.pega_dados_alimento()
        if self.busca_alimento_por_nome(dados_alimento.nome):
            raise JahCadastradoException()
        else:
            self.__alimentos.append(dados_alimento)
            self.__tela_alimento.mostra_mensagem("Alimento incluido com sucesso!")

    def busca_alimento_por_nome(self, nome):
        for alimento in self.__alimentos:
            if alimento.nome == nome:
                return alimento

        return None

    def listar_alimento(self):
        for alimento in self.__alimentos:
            self.__tela_alimento.mostra_alimento(alimento.__dict__)
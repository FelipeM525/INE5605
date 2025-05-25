from alimentos.controlador_alimento import ControladorAlimento
from alimentos.tela_alimento import TelaAlimento
from exception.refeicao_existente_exception import RefeicaoExistenteException
from exception.refeicao_inexistente_exception import RefeicaoInexistenteException
from refeicoes.refeicao import Refeicao
from refeicoes.tela_refeicao import TelaRefeicao


class ControladorRefeicao:
    def __init__(self):
        self.__controlador_alimento = ControladorAlimento()
        self.__tela_refeicao = TelaRefeicao()
        self.__tela_alimento = TelaAlimento()
        self.__refeicoes = []

    def incluir_refeicao(self):
        dados_refeicao = self.__tela_refeicao.pega_dados_refeicao()
        alimentos = []

        if self.busca_refeicao_por_nome(dados_refeicao.nome):
            raise RefeicaoExistenteException
        for nome in dados_refeicao.nomes_alimento:
            alimento = self.__controlador_alimento.busca_alimento_por_nome(nome)
            alimentos.append(alimento)

        self.__refeicoes.append(Refeicao(dados_refeicao.nome, alimentos, dados_refeicao.tipo))

        return self.__tela_refeicao.mostra_mensagem(f"Refeicao {dados_refeicao.tipo} incluida com sucesso!")

    def busca_refeicao_por_nome(self, nome):
        for refeicao in self.__refeicoes:
            if refeicao.nome == nome:
                return refeicao
        raise RefeicaoInexistenteException

    def excluir_refeicao(self):
        nome = self.__tela_refeicao.seleciona_refeicao()
        refeicao = self.busca_refeicao_por_nome(nome)

        if not refeicao:
            raise RefeicaoInexistenteException
        else:
            self.__refeicoes.remove(refeicao)
            return self.__tela_refeicao.mostra_mensagem(f"Refeicao {nome} removida com sucesso!")


    def excluir_alimento_da_refeicao(self):
        nome = self.__tela_refeicao.seleciona_refeicao()
        nome_alimento = self.__tela_alimento.seleciona_alimento()
        refeicao = self.busca_refeicao_por_nome(nome)

        if not refeicao:
            raise RefeicaoInexistenteException

        for alimento in refeicao.alimentos:
            if alimento.nome == nome_alimento:
                refeicao.alimentos.remove(alimento)
                return self.__tela_refeicao.mostra_mensagem(
                    f"Alimento {nome_alimento} removido da refeicao {nome} com sucesso!")
            else:
                return self.__tela_refeicao.mostra_mensagem(f"Alimento {nome_alimento} nao encontrado na refeicao {nome}")

        return None

    def listar_refeicoes(self):
        for refeicao in self.__refeicoes:
            self.__tela_refeicao.mostra_refeicao(refeicao)

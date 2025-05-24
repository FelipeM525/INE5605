from controller.controlador_alimento import ControladorAlimento
from exception.alimento_inexistente_exception import AlimentoInexistenteException
from exception.cadastroInexistenteException import CadastroInexistenteException
from exception.refeicao_inexistente_exception import RefeicaoInexistenteException
from model.refeicao import Refeicao
from view.tela_refeicao import TelaRefeicao


class ControladorRefeicao:
    def __init__(self):
        self.__controlador_alimento = ControladorAlimento()
        self.__tela_refeicao = TelaRefeicao()
        self.__refeicoes = []

    def incluir_refeicao(self):
        dados_refeicao = self.__tela_refeicao.pega_dados_refeicao()
        alimentos = []

        for nome in dados_refeicao.nomes_alimento:
            alimento = self.__controlador_alimento.busca_alimento_por_nome(nome)
            alimentos.append(alimento)

        self.__refeicoes.append(Refeicao(alimentos, dados_refeicao.tipo))

        return self.__tela_refeicao.mostra_mensagem(f"Refeicao {dados_refeicao.tipo} incluida com sucesso!")

    def excluir_refeicao(self):
        tipo_refeicao = self.__tela_refeicao.excluir_refeicao()

        for refeicao in self.__refeicoes:
            if refeicao.tipo == tipo_refeicao:
                self.__refeicoes.remove(refeicao)
                return self.__tela_refeicao.mostra_mensagem(f"Refeicao {tipo_refeicao} removida com sucesso!")
            else:
                raise CadastroInexistenteException()
        return None

    def excluir_alimento_da_refeicao(self):
        tipo_refeicao, nome_alimento = self.__tela_refeicao.excluir_alimento_refeicao()
        for refeicao in self.__refeicoes:
            if refeicao.tipo == tipo_refeicao:
                for alimento in refeicao.alimentos:
                    if alimento.nome == nome_alimento:
                        refeicao.alimentos.remove(alimento)
                        return self.__tela_refeicao.mostra_mensagem(f"Alimento {nome_alimento} removido da refeicao {tipo_refeicao} com sucesso!")
                    else:
                        raise AlimentoInexistenteException()
            else:
                raise RefeicaoInexistenteException()
        return None

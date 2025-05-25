from alimentos.controlador_alimento import ControladorAlimento
from alimentos.tela_alimento import TelaAlimento
from core.controlador_sistema import ControladorSistema
from exception.alimento_inexistente_exception import AlimentoInexistenteException
from exception.refeicao_existente_exception import RefeicaoExistenteException
from exception.refeicao_inexistente_exception import RefeicaoInexistenteException
from refeicoes.refeicao import Refeicao
from refeicoes.tela_refeicao import TelaRefeicao


class ControladorRefeicao:
    def __init__(self, controlador_alimento: ControladorAlimento, controlador_sistema: ControladorSistema):
        self.__controlador_alimento = controlador_alimento
        self.__controlador_sistema = controlador_sistema
        self.__tela_refeicao = TelaRefeicao()
        self.__tela_alimento = TelaAlimento()
        self.__refeicoes = []

    def incluir_refeicao(self):
        dados_refeicao = self.__tela_refeicao.pega_dados_refeicao()
        alimentos = []
        try:
            if self.busca_refeicao_por_nome(dados_refeicao.nome):
                raise RefeicaoExistenteException
            for nome in dados_refeicao.nomes_alimento:
                alimento = self.__controlador_alimento.busca_alimento_por_nome(nome)
                alimentos.append(alimento)

            self.__refeicoes.append(Refeicao(dados_refeicao.nome, alimentos, dados_refeicao.tipo))

            return self.__tela_refeicao.mostra_mensagem(f"Refeicao {dados_refeicao.tipo} incluida com sucesso!")
        except RefeicaoExistenteException:
            return self.__tela_refeicao.mostra_mensagem(f"Refeicao {dados_refeicao.tipo} ja existe!")
    def busca_refeicao_por_nome(self, nome):
        for refeicao in self.__refeicoes:
            if refeicao.nome == nome:
                return refeicao
        return None

    def excluir_refeicao(self):
        nome = self.__tela_refeicao.seleciona_refeicao()
        refeicao = self.busca_refeicao_por_nome(nome)
        try:
            if not refeicao:
                raise RefeicaoInexistenteException
            else:
                self.__refeicoes.remove(refeicao)
                return self.__tela_refeicao.mostra_mensagem(f"Refeicao {nome} removida com sucesso!")
        except RefeicaoInexistenteException:
            return self.__tela_refeicao.mostra_mensagem(f"Refeicao {nome} nao existe!")


    def excluir_alimento_da_refeicao(self):
        nome = self.__tela_refeicao.seleciona_refeicao()
        nome_alimento = self.__tela_alimento.seleciona_alimento()
        refeicao = self.busca_refeicao_por_nome(nome)

        try:
            if not refeicao:
                raise RefeicaoInexistenteException

            for alimento in refeicao.alimentos:
                if alimento.nome == nome_alimento:
                    refeicao.alimentos.remove(alimento)
                    return self.__tela_refeicao.mostra_mensagem(
                        f"Alimento {nome_alimento} removido da refeicao {nome} com sucesso!")
                else:
                    return self.__tela_refeicao.mostra_mensagem(f"Alimento {nome_alimento} nao encontrado na refeicao {nome}")
        except RefeicaoInexistenteException:
            return self.__tela_refeicao.mostra_mensagem(f"Refeicao {nome} nao existe!")

        return None

    def incluir_alimento_na_refeicao(self):
        nome = self.__tela_refeicao.seleciona_refeicao()
        refeicao = self.busca_refeicao_por_nome(nome)
        nome_alimento = self.__tela_alimento.seleciona_alimento()

        try:
            alimento = self.__controlador_alimento.busca_alimento_por_nome(nome_alimento)

            if not alimento:
                raise AlimentoInexistenteException

            refeicao.alimentos.append(alimento)

            return self.__tela_refeicao.mostra_mensagem(f"Alimento {nome_alimento} incluido na refeicao {nome} com sucesso!")
        except AlimentoInexistenteException:
            return self.__tela_refeicao.mostra_mensagem(f"Alimento {nome_alimento} nao existe!")

    def listar_refeicoes(self):
        if len(self.__refeicoes) == 0:
            self.__tela_refeicao.mostra_mensagem("Nao ha refeicoes cadastradas!")
        else:
            for refeicao in self.__refeicoes:
                self.__tela_refeicao.mostra_refeicao(refeicao)

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_refeicao, 2: self.listar_refeicoes, 3: self.incluir_alimento_na_refeicao,
                        4: self.excluir_alimento_da_refeicao, 5: self.excluir_refeicao, 6: self.retornar}

        while True:
            opcao = self.__tela_refeicao.mostrar_menu()
            if opcao == 6:
                self.retornar()
                break

            funcao_escolhida = lista_opcoes.get(opcao)
            if funcao_escolhida:
                funcao_escolhida()
            else:
                self.__tela_refeicao.mostra_mensagem("Opção inválida!")

    def retornar(self):
        pass
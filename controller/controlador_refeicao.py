from tkinter import Toplevel
from view.tela_refeicao_tkinter import TelaRefeicaoTk
from exception.alimento_inexistente_exception import AlimentoInexistenteException
from exception.refeicao_existente_exception import RefeicaoExistenteException
from exception.refeicao_inexistente_exception import RefeicaoInexistenteException
from model.refeicao import Refeicao
from dao.refeicao_dao import RefeicaoDAO


class ControladorRefeicao:
    def __init__(self, controlador_alimento, controlador_sistema):
        self.__controlador_alimento = controlador_alimento
        self.__controlador_sistema = controlador_sistema
        self.__tela_refeicao = None
        self.__refeicao_dao = RefeicaoDAO()
        self.__top_level = None

    def abre_tela(self):
        self.__top_level = Toplevel(self.__controlador_sistema.root)
        self.__tela_refeicao = TelaRefeicaoTk(self.__top_level, self)
        self.__top_level.protocol("WM_DELETE_WINDOW", self.retornar)

    def incluir_refeicao(self):
        dados_refeicao = self.__tela_refeicao.pega_dados_refeicao()
        if not dados_refeicao.get("codigo"):
            self.__tela_refeicao.mostra_mensagem("Cancelado", "Criação de refeição cancelada.")
            return

        try:
            if self.busca_refeicao_por_codigo(dados_refeicao["codigo"]):
                raise RefeicaoExistenteException()

            nova_refeicao = Refeicao(dados_refeicao["codigo"], [], dados_refeicao["tipo"])
            self.__refeicao_dao.add(nova_refeicao.codigo, nova_refeicao)
            self.__tela_refeicao.mostra_mensagem("Sucesso", "Refeição incluída com sucesso!")
        except RefeicaoExistenteException:
            self.__tela_refeicao.mostra_mensagem("Erro", "Refeição já existe!")

    def busca_refeicao_por_codigo(self, codigo):
        return self.__refeicao_dao.get(codigo)

    def remover_refeicao(self):
        codigo_refeicao = self.__tela_refeicao.seleciona_refeicao()
        if not codigo_refeicao: return

        try:
            if self.busca_refeicao_por_codigo(codigo_refeicao):
                self.__refeicao_dao.remove(codigo_refeicao)
                self.__tela_refeicao.mostra_mensagem("Sucesso", "Refeição removida com sucesso!")
            else:
                raise RefeicaoInexistenteException()
        except RefeicaoInexistenteException:
            self.__tela_refeicao.mostra_mensagem("Erro", f"Refeição '{codigo_refeicao}' não encontrada.")

    def excluir_alimento_da_refeicao(self):
        codigo_refeicao = self.__tela_refeicao.seleciona_refeicao()
        if not codigo_refeicao: return

        refeicao = self.busca_refeicao_por_codigo(codigo_refeicao)
        if not refeicao:
            self.__tela_refeicao.mostra_mensagem("Erro", f"Refeição '{codigo_refeicao}' não encontrada.")
            return

        nome_alimento = self.__tela_refeicao.seleciona_alimento()
        if not nome_alimento: return

        alimento_encontrado = next((alimento for alimento in refeicao.alimentos if alimento.nome == nome_alimento),
                                   None)

        if alimento_encontrado:
            refeicao.alimentos.remove(alimento_encontrado)
            self.__refeicao_dao.update(refeicao.codigo, refeicao)
            self.__tela_refeicao.mostra_mensagem("Sucesso", f"Alimento '{nome_alimento}' removido.")
        else:
            self.__tela_refeicao.mostra_mensagem("Info", f"Alimento '{nome_alimento}' não encontrado na refeição.")

    def incluir_alimento_na_refeicao(self):
        codigo_refeicao = self.__tela_refeicao.seleciona_refeicao()
        if not codigo_refeicao: return

        refeicao = self.busca_refeicao_por_codigo(codigo_refeicao)
        if not refeicao:
            self.__tela_refeicao.mostra_mensagem("Erro", f"Refeição '{codigo_refeicao}' não encontrada.")
            return

        nome_alimento = self.__tela_refeicao.seleciona_alimento()
        if not nome_alimento: return

        try:
            alimento = self.__controlador_alimento.buscar_alimento_por_nome(nome_alimento)
            if not alimento:
                raise AlimentoInexistenteException()

            refeicao.adicionar_alimento(alimento)
            self.__refeicao_dao.update(refeicao.codigo, refeicao)
            self.__tela_refeicao.mostra_mensagem("Sucesso", f"Alimento '{nome_alimento}' incluído.")
        except AlimentoInexistenteException:
            self.__tela_refeicao.mostra_mensagem("Erro", f"Alimento '{nome_alimento}' não existe!")

    def listar_refeicoes(self):
        refeicoes = self.__refeicao_dao.get_all()
        if not refeicoes:
            self.__tela_refeicao.mostra_mensagem("Info", "Nenhuma refeição cadastrada!")
        else:
            dados_para_tela = [{
                "codigo": r.codigo, "tipo": r.tipo, "calorias_total": r.calorias_totais(),
                "alimentos": [a.nome for a in r.alimentos]
            } for r in refeicoes]
            self.__tela_refeicao.mostra_refeicao(dados_para_tela)

    def retornar(self):
        self.__top_level.destroy()
        self.__controlador_sistema.reabre_tela_principal()
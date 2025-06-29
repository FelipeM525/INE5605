from tkinter import Toplevel
from view.tela_alimento_tkinter import TelaAlimentoTk
from model.alimento import Alimento
from exception.alimento_inexistente_exception import AlimentoInexistenteException
from exception.jahCadastradoException import JahCadastradoException
from dao.alimento_dao import AlimentoDAO

class ControladorAlimento():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__alimento_dao = AlimentoDAO()
        self.__tela_alimento = None
        self.__top_level = None

    def abre_tela(self):
        self.__top_level = Toplevel(self.__controlador_sistema.root)
        self.__tela_alimento = TelaAlimentoTk(self.__top_level, self)
        self.__top_level.protocol("WM_DELETE_WINDOW", self.retornar)

    @property
    def alimentos(self):
        return self.__alimento_dao.get_all()

    def incluir_alimento(self):
        try:
            dados_alimento = self.__tela_alimento.pega_dados_alimento()
            if not dados_alimento.get("nome"):
                self.__tela_alimento.mostra_mensagem("Cancelado", "Inclusão cancelada.")
                return

            nome_alimento = dados_alimento["nome"]

            if self.__alimento_dao.get(nome_alimento):
                raise JahCadastradoException

            novo_alimento = Alimento(nome_alimento,
                                     dados_alimento["calorias"],
                                     dados_alimento["carboidratos"],
                                     dados_alimento["proteinas"],
                                     dados_alimento["gorduras"])
            self.__alimento_dao.add(novo_alimento.nome, novo_alimento)
            self.__tela_alimento.mostra_mensagem("Sucesso", "Alimento cadastrado com sucesso!")

        except JahCadastradoException:
            self.__tela_alimento.mostra_mensagem("Erro", "Alimento já cadastrado!")
        except Exception as e:
            self.__tela_alimento.mostra_mensagem("Erro", f"Ocorreu um erro: {e}")

    def alterar_alimento(self):
        nome_alimento = self.__tela_alimento.seleciona_alimento()
        if not nome_alimento: return

        alimento = self.buscar_alimento_por_nome(nome_alimento)

        try:
            if not alimento:
                raise AlimentoInexistenteException()

            novos_dados = self.__tela_alimento.pega_dados_alimento(alimento)
            if not novos_dados.get("nome"):
                self.__tela_alimento.mostra_mensagem("Cancelado", "Alteração cancelada.")
                return

            alimento.calorias = novos_dados["calorias"]
            alimento.carboidratos = novos_dados["carboidratos"]
            alimento.proteinas = novos_dados["proteinas"]
            alimento.gorduras = novos_dados["gorduras"]

            self.__alimento_dao.update(alimento.nome, alimento)
            self.__tela_alimento.mostra_mensagem("Sucesso", "Alimento alterado com sucesso!")

        except AlimentoInexistenteException:
            self.__tela_alimento.mostra_mensagem("Erro", f"Alimento '{nome_alimento}' não encontrado.")

    def excluir_alimento(self):
        nome_alimento = self.__tela_alimento.seleciona_alimento()
        if not nome_alimento: return

        try:
            if self.__alimento_dao.get(nome_alimento):
                self.__alimento_dao.remove(nome_alimento)
                self.__tela_alimento.mostra_mensagem("Sucesso", "Alimento removido com sucesso!")
            else:
                raise AlimentoInexistenteException()

        except AlimentoInexistenteException:
            self.__tela_alimento.mostra_mensagem("Erro", f"Alimento '{nome_alimento}' não encontrado.")

    def listar_alimento(self):
        if not self.alimentos:
            self.__tela_alimento.mostra_mensagem("Info", "Nenhum alimento cadastrado.")
            return

        dados_para_tela = [{
            "nome": alimento.nome, "calorias": alimento.calorias,
            "carboidratos": alimento.carboidratos, "proteinas": alimento.proteinas,
            "gorduras": alimento.gorduras
        } for alimento in self.alimentos]

        self.__tela_alimento.mostra_alimento(dados_para_tela)

    def buscar_alimento_por_nome(self, nome: str):
        return self.__alimento_dao.get(nome)

    def retornar(self):
        self.__top_level.destroy()
        self.__controlador_sistema.reabre_tela_principal()
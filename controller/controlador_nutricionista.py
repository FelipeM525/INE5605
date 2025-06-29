from tkinter import Toplevel
from view.tela_nutricionista_tkinter import TelaNutricionistaTk
from model.nutricionista import Nutricionista
from exception.jahCadastradoException import JahCadastradoException
from exception.cadastroInexistenteException import CadastroInexistenteException
from dao.nutricionista_dao import NutricionistaDAO

class ControladorNutricionista:
    def __init__(self, controlador_sistema):
        self.__nutricionista_dao = NutricionistaDAO()
        self.__tela_nutricionista = None
        self.__controlador_sistema = controlador_sistema
        self.__top_level = None

    def abre_tela(self):
        self.__top_level = Toplevel(self.__controlador_sistema.root)
        self.__tela_nutricionista = TelaNutricionistaTk(self.__top_level, self)
        self.__top_level.protocol("WM_DELETE_WINDOW", self.retornar)

    def buscar_nutricionista_por_cpf(self, cpf: str):
        return self.__nutricionista_dao.get(cpf)

    def incluir_nutricionista(self):
        dados_nutri = self.__tela_nutricionista.cadastrar_nutricionista()
        if not dados_nutri.get("cpf"):
            self.__tela_nutricionista.mostrar_mensagem("Cancelado", "Cadastro cancelado.")
            return

        try:
            if self.buscar_nutricionista_por_cpf(dados_nutri["cpf"]):
                raise JahCadastradoException()

            novo_nutricionista = Nutricionista(
                nome=dados_nutri["nome"],
                email=dados_nutri["email"],
                senha=dados_nutri["senha"],
                cpf=dados_nutri["cpf"],
                crn=dados_nutri["crn"],
                clinica=dados_nutri["clinica"]
            )

            self.__nutricionista_dao.add(novo_nutricionista)
            self.__tela_nutricionista.mostrar_mensagem("Sucesso", "Nutricionista cadastrado com sucesso!")

        except JahCadastradoException:
            self.__tela_nutricionista.mostrar_mensagem("Erro", f"Nutricionista com CPF {dados_nutri['cpf']} já existe!")
        except Exception as e:
            self.__tela_nutricionista.mostrar_mensagem("Erro", f"Ocorreu um erro inesperado: {e}")

    def remover_nutricionista(self):
        cpf = self.__tela_nutricionista.selecionar_nutricionista_cpf()
        if not cpf: return
        nutricionista = self.buscar_nutricionista_por_cpf(cpf)

        try:
            if nutricionista:
                self.__nutricionista_dao.remove(cpf)
                self.__tela_nutricionista.mostrar_mensagem("Sucesso", f"Nutricionista com CPF {cpf} removido com sucesso!")

            else:
                raise CadastroInexistenteException()
        except CadastroInexistenteException:
            self.__tela_nutricionista.mostrar_mensagem("Erro", f"Nutricionista com CPF {cpf} não existe!")

    def mostrar_dados_nutricionista(self):
        cpf = self.__tela_nutricionista.selecionar_nutricionista_cpf()
        if not cpf: return
        nutricionista = self.buscar_nutricionista_por_cpf(cpf)
        try:
            if nutricionista:
                self.__tela_nutricionista.pegar_dados_nutricionista(nutricionista)

            else:
                raise CadastroInexistenteException()
        except CadastroInexistenteException:
            self.__tela_nutricionista.mostrar_mensagem("Erro", f"Nutricionista com CPF {cpf} não existe!")

    def listar_nutricionistas(self):
        nutricionistas = self.__nutricionista_dao.get_all()

        if not nutricionistas:
            self.__tela_nutricionista.mostrar_mensagem("Info", "Não há nutricionistas cadastrados.")
            return

        dados_para_tela = []
        for nutricionista in nutricionistas:
            dados_para_tela.append({
                "nome": nutricionista.nome,
                "cpf": nutricionista.cpf
            })

        self.__tela_nutricionista.listar_nutricionistas(dados_para_tela)

    def retornar(self):
        self.__top_level.destroy()
        self.__controlador_sistema.reabre_tela_principal()
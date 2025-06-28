from model.nutricionista import Nutricionista
from exception.jahCadastradoException import JahCadastradoException
from exception.cadastroInexistenteException import CadastroInexistenteException
from view.tela_nutricionista import TelaNutricionista
from dao.nutricionista_dao import NutricionistaDAO

class ControladorNutricionista:
    def __init__(self, controlador_sistema):
        self.__nutricionista_dao = NutricionistaDAO()
        self.__tela_nutricionista = TelaNutricionista()
        self.__controlador_sistema = controlador_sistema

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_nutricionista, 2: self.mostrar_dados_nutricionista, 3: self.listar_nutricionistas,
                        4: self.remover_nutricionista, 0: self.retornar}

        while True:
            opcao = self.__tela_nutricionista.mostrar_menu()
            if opcao == 0:
                self.retornar()
                break

            funcao_escolhida = lista_opcoes.get(opcao)
            if funcao_escolhida:
                funcao_escolhida()
            else:
                self.__tela_nutricionista.mostrar_mensagem("Opção inválida!")

    def buscar_nutricionista_por_cpf(self, cpf: str):
        return self.__nutricionista_dao.get(cpf)

    def incluir_nutricionista(self):
        novo_nutricionista = self.__tela_nutricionista.cadastrar_nutricionista()

        if not isinstance(novo_nutricionista, Nutricionista):
            raise ValueError("Valores inválidos")

        try:
        
            if self.buscar_nutricionista_por_cpf(novo_nutricionista.cpf):
                raise JahCadastradoException()
        
            else:
                self.__nutricionista_dao.add(novo_nutricionista)
                return self.__tela_nutricionista.mostrar_mensagem("Nutricionista cadastrado com sucesso")

        except JahCadastradoException:
            return self.__tela_nutricionista.mostrar_mensagem(f"Nutricionista com cpf {novo_nutricionista.cpf} ja existe!")

    def remover_nutricionista(self):
        cpf = self.__tela_nutricionista.selecionar_nutricionista_cpf()
        nutricionista = self.buscar_nutricionista_por_cpf(cpf)

        try:
            if nutricionista:
                self.__nutricionista_dao.remove(cpf)
                return self.__tela_nutricionista.mostrar_mensagem(f"Nutricionista com cpf {cpf} removido com sucesso!")

            else:
                raise CadastroInexistenteException()
        except CadastroInexistenteException:
            return self.__tela_nutricionista.mostrar_mensagem(f"Nutricionista com cpf {cpf} nao existe!")

    def mostrar_dados_nutricionista(self):
        cpf = self.__tela_nutricionista.selecionar_nutricionista_cpf()
        nutricionista = self.buscar_nutricionista_por_cpf(cpf)
        try:
            if nutricionista:
                return self.__tela_nutricionista.pegar_dados_nutricionista(nutricionista)

            else:
                raise CadastroInexistenteException()
        except CadastroInexistenteException:
            return self.__tela_nutricionista.mostrar_mensagem(f"Nutricionista com cpf {cpf} nao existe!")

    def listar_nutricionistas(self):
        nutricionistas = self.__nutricionista_dao.get_all()
        if not nutricionistas:
            self.__tela_nutricionista.mostra_mensagem("Nao ha nutricionistas cadastrados!")
        else:
            dados_para_tela = []
            for nutricionista in nutricionistas:
                dados_para_tela.append({
                    "nome": nutricionista.nome,
                    "cpf": nutricionista.cpf
                })
            self.__tela_nutricionista.listar_nutricionistas(dados_para_tela)

    def retornar(self):
        pass
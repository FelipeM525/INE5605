from usuarios.model.nutricionista import Nutricionista
from exception.jahCadastradoException import JahCadastradoException
from exception.cadastroInexistenteException import CadastroInexistenteException
from usuarios.view.tela_nutricionista import TelaNutricionista

class ControladorNutricionista:
    def __init__(self, controlador_sistema):
        self.__nutricionistas = []
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
        for nutricionista in self.__nutricionistas:
            if nutricionista.cpf == cpf:
                return nutricionista
        return None

    def incluir_nutricionista(self):
        novo_nutricionista = self.__tela_nutricionista.cadastrar_nutricionista()

        if not isinstance(novo_nutricionista, Nutricionista):
            raise ValueError("Valores inválidos")

        try:
        
            if self.buscar_nutricionista_por_cpf(novo_nutricionista.cpf):
                raise JahCadastradoException()
        
            else:
                self.__nutricionistas.append(novo_nutricionista)

        except JahCadastradoException:
            return self.__tela_nutricionista.mostrar_mensagem(f"Nutricionista com cpf {novo_nutricionista.cpf} ja existe!")

    def remover_nutricionista(self):
        cpf = self.__tela_nutricionista.selecionar_nutricionista_cpf()
        nutricionista = self.buscar_nutricionista_por_cpf(cpf)

        try:
            if nutricionista:
                self.__nutricionistas.remove(nutricionista)
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
        lista_de_nutricionistas = self.__nutricionistas
        if len(self.__nutricionistas) == 0:
             self.__tela_nutricionista.mostrar_mensagem("Nao ha nutricionistas cadastrados!")
        else:
            self.__tela_nutricionista.listar_nutricionistas(lista_de_nutricionistas)

    def retornar(self):
        pass
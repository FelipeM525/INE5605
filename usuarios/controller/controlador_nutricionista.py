from usuarios.model.nutricionista import Nutricionista
from exception.jahCadastradoException import JahCadastradoException
from exception.cadastroInexistenteException import CadastroInexistenteException
from usuarios.view.tela_nutricionista import TelaNutricionista

class ControladorNutricionista:
    def __init__(self):
        self.__nutricionistas = []
        self.tela_nutricionista = TelaNutricionista()

    def abre_tela(self):
        while True:
            try:
                opcao = self.tela_nutricionista.mostrar_menu()

                if opcao == 1:
                    self.incluir_nutricionista()
                elif opcao == 2:
                    self.mostrar_dados_nutricionista()
                elif opcao == 3:
                    self.listar_nutricionistas()
                elif opcao == 4:
                    self.remover_nutricionista()
                elif opcao == 0: #menu
                    break
                else:
                    self.tela_nutricionista.mostrar_mensagem("Opção inválida. Insira um número listado.")

            except ValueError:
                self.tela_nutricionista.mostrar_mensagem("Entrada inválida. Por favor, insira um número dentre os listados.")

            except (JahCadastradoException, CadastroInexistenteException) as e:
                self.tela_nutricionista.mostrar_mensagem(e)

    def buscar_nutricionista_por_cpf(self, cpf: str):
        for nutricionista in self.__nutricionistas:
            if nutricionista.cpf == cpf:
                return nutricionista
        return None

    def incluir_nutricionista(self):
        novo_nutricionista = self.tela_nutricionista.cadastrar_nutricionista()

        if not isinstance(novo_nutricionista, Nutricionista):
            raise ValueError("Valores inválidos")
        
        if self.buscar_nutricionista_por_cpf(novo_nutricionista.cpf):
            raise JahCadastradoException()
        
        else:
            self.__nutricionistas.append(novo_nutricionista)

    def remover_nutricionista(self):
        cpf = self.tela_nutricionista.selecionar_nutricionista_cpf()
        nutricionista = self.buscar_nutricionista_por_cpf(cpf)

        if nutricionista:
            self.__nutricionistas.remove(nutricionista)

        else:
            raise CadastroInexistenteException()

    def mostrar_dados_nutricionista(self):
        cpf = self.tela_nutricionista.selecionar_nutricionista_cpf()
        nutricionista = self.buscar_nutricionista_por_cpf(cpf)

        if nutricionista:
            self.tela_nutricionista.pegar_dados_nutricionista(nutricionista)

        else:
            raise CadastroInexistenteException()

    def listar_nutricionistas(self):
        lista_de_nutricionistas = self.__nutricionistas
        self.tela_nutricionista.listar_nutricionistas(lista_de_nutricionistas)
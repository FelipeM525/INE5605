from exception.alimento_inexistente_exception import AlimentoInexistenteException
from exception.jahCadastradoException import JahCadastradoException
from alimentos.tela_alimento import TelaAlimento
#from alimentos.alimento import Alimento


class ControladorAlimento:
    def __init__(self):
        self.__tela_alimento = TelaAlimento()
        self.__alimentos = []
    
    def abre_tela(self):
        while True:
            try:
                opcao = self.__tela_alimento.mostrar_menu()
                if opcao == 1:
                    self.incluir_alimento()
                if opcao == 2:
                    self.listar_alimento()
                if opcao == 3:
                    break
                else:
                    self.__tela_alimento.mostra_mensagem("Opção inválida, favor escolher uma das disponíveis.")
            except (JahCadastradoException) as e:
                self.__tela_alimento.mostra_mensagem(e)
            except ValueError:
                self.__tela_alimento.mostra_mensagem("Entrada inválida. Por favor, insira um número.")        

    def incluir_alimento(self):
        dados_alimento = self.__tela_alimento.pega_dados_alimento()
        if self.busca_alimento_por_nome(dados_alimento.nome):
            raise JahCadastradoException()
        else:
            self.__alimentos.append(dados_alimento)
            self.__tela_alimento.mostra_mensagem("Alimento incluido com sucesso!")


#    def incluir_alimento(self):
#        dados_alimento = self.__tela_alimento.pega_dados_alimento()
#        
#        # O busca_alimento_por_nome espera objetos, então buscamos pelo nome no dicionário
#        if self.busca_alimento_por_nome(dados_alimento["nome"]):
#            raise JahCadastradoException()
#        else:
#            # ALTERAÇÃO 3 (BUG FIX): Criar um objeto Alimento em vez de adicionar um dicionário na lista
#            novo_alimento = Alimento(
#                nome=dados_alimento["nome"],
#                calorias=dados_alimento["calorias"],
#                carboidratos=dados_alimento["carboidratos"],
#                gorduras=dados_alimento["gorduras"],
#                proteinas=dados_alimento["proteinas"]
#            )
#            self.__alimentos.append(novo_alimento)
#            self.__tela_alimento.mostra_mensagem("Alimento incluido com sucesso!")


    def busca_alimento_por_nome(self, nome):
        for alimento in self.__alimentos:
            if alimento.nome == nome:
                return alimento

        raise AlimentoInexistenteException

    def listar_alimento(self):
        for alimento in self.__alimentos:
            self.__tela_alimento.mostra_alimento(alimento)
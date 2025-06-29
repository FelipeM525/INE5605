from view.tela_alimento import TelaAlimento
from model.alimento import Alimento
from exception.alimento_inexistente_exception import AlimentoInexistenteException
from exception.jahCadastradoException import JahCadastradoException

class ControladorAlimento():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_alimento = TelaAlimento()
        self.__alimentos = []

    @property
    def alimentos(self):
        return self.__alimentos

    def incluir_alimento(self):
        try:
            dados_alimento = self.__tela_alimento.pega_dados_alimento()
            nome_alimento = dados_alimento["nome"]

            for alimento in self.__alimentos:
                if alimento.nome == nome_alimento:
                    raise JahCadastradoException

            novo_alimento = Alimento(nome_alimento,
                                     dados_alimento["calorias"],
                                     dados_alimento["carboidratos"],
                                     dados_alimento["proteinas"],
                                     dados_alimento["gorduras"])
            self.__alimentos.append(novo_alimento)
            self.__tela_alimento.mostra_mensagem("Alimento cadastrado com sucesso!")

        except JahCadastradoException as e:
            self.__tela_alimento.mostra_mensagem(e)

    def alterar_alimento(self):
        if not self.__alimentos:
            self.__tela_alimento.mostra_mensagem("Nenhum alimento cadastrado para alterar.")
            return

        nome_alimento = self.__tela_alimento.seleciona_alimento()
        alimento = self.buscar_alimento_por_nome(nome_alimento)

        try:
            if not alimento:
                raise AlimentoInexistenteException

            novos_dados_alimento = self.__tela_alimento.pega_dados_alimento()

            alimento.nome = novos_dados_alimento["nome"]
            alimento.calorias = novos_dados_alimento["calorias"]
            alimento.carboidratos = novos_dados_alimento["carboidratos"]
            alimento.proteinas = novos_dados_alimento["proteinas"]
            alimento.gorduras = novos_dados_alimento["gorduras"]

            self.listar_alimento()
            self.__tela_alimento.mostra_mensagem("Alimento alterado com sucesso!")

        except AlimentoInexistenteException as e:
            self.__tela_alimento.mostra_mensagem(f"Erro: {e}")

    def excluir_alimento(self):
        if not self.__alimentos:
            self.__tela_alimento.mostra_mensagem("Nenhum alimento cadastrado para excluir.")
            return

        nome_alimento = self.__tela_alimento.seleciona_alimento()
        alimento = self.buscar_alimento_por_nome(nome_alimento)

        try:
            if alimento:
                self.__alimentos.remove(alimento)
                self.listar_alimento()
                self.__tela_alimento.mostra_mensagem("Alimento removido com sucesso!")
            else:
                raise AlimentoInexistenteException

        except AlimentoInexistenteException as e:
            self.__tela_alimento.mostra_mensagem(f"Erro: {e}")

    def listar_alimento(self):
        if not self.__alimentos:
            self.__tela_alimento.mostra_mensagem("Nenhum alimento cadastrado.")
            return

        dados_para_tela = []
        for alimento in self.__alimentos:
            dados_para_tela.append({
                "nome": alimento.nome,
                "calorias": alimento.calorias,
                "carboidratos": alimento.carboidratos,
                "proteinas": alimento.proteinas,
                "gorduras": alimento.gorduras
            })

        self.__tela_alimento.mostra_alimento(dados_para_tela)

    def buscar_alimento_por_nome(self, nome: str):
        for alimento in self.__alimentos:
            if alimento.nome == nome:
                return alimento
        return None

    def retornar(self):
        pass

    def abrir_tela(self):
        lista_opcoes = {
            1: self.incluir_alimento,
            2: self.alterar_alimento,
            3: self.listar_alimento,
            4: self.excluir_alimento,
            0: self.retornar
        }
        while True:
            opcao_escolhida = self.__tela_alimento.tela_opcoes()
            funcao_escolhida = lista_opcoes.get(opcao_escolhida)
            if funcao_escolhida:
                funcao_escolhida()

            else:
                self.__tela_alimento.mostra_mensagem("Opção inválida!")

            if opcao_escolhida == 0:
                self.retornar()
                break

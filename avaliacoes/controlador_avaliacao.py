from avaliacoes.avaliacao import Avaliacao
from avaliacoes.tela_avaliacao import TelaAvaliacao
from exception.avaliacao_inexistente_exception import AvaliacaoInexistenteException
from exception.cadastroInexistenteException import CadastroInexistenteException
from exception.cliente_inexistente_exception import ClienteInexistenteException
from usuarios.controller.controlador_cliente import ControladorCliente
from usuarios.controller.controlador_nutricionista import ControladorNutricionista
from usuarios.model.cliente import Cliente
from usuarios.model.nutricionista import Nutricionista


class ControladorAvaliacao:
    def __init__(self, controlador_sistema, controlador_cliente: ControladorCliente, controlador_nutricionista: ControladorNutricionista):
        self.__tela_avaliacao = TelaAvaliacao()
        self.__controlador_cliente = controlador_cliente
        self.__controlador_nutricionista = controlador_nutricionista
        self.__controlador_sistema = controlador_sistema
        self.__avaliacoes = []

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_avaliacao,
            2: self.lista_avaliacao,
            3: self.alterar_avaliacao,
            4: self.remover_avaliacao,
            0: self.retornar
        }

        while True:
            opcao = self.__tela_avaliacao.mostrar_menu()

            if opcao == 0:
                self.retornar()
                break

            funcao_escolhida = lista_opcoes.get(opcao)

            if funcao_escolhida:
                funcao_escolhida()
            else:
                self.__tela_avaliacao.mostra_mensagem("Opção inválida. Tente novamente.")

    def incluir_avaliacao(self):
        dados_avaliacao = self.__tela_avaliacao.pega_dados_avaliacao()
        nome_avaliacao = dados_avaliacao["nome"]

        if self.busca_avaliacao_por_nome(nome_avaliacao):
            self.__tela_avaliacao.mostra_mensagem(f"Já existe uma avaliação com o nome '{nome_avaliacao}'.")
            return

        cliente: Cliente = self.__controlador_cliente.buscar_cliente_por_cpf(dados_avaliacao["cpf_cliente"])
        try:
            if not cliente:
                raise ClienteInexistenteException
        except ClienteInexistenteException:
            self.__tela_avaliacao.mostra_mensagem(f"Cliente com cpf {dados_avaliacao['cpf_cliente']} não existe!")
            return

        nutricionista: Nutricionista = self.__controlador_nutricionista.buscar_nutricionista_por_cpf(
            dados_avaliacao["cpf_nutricionista"])
        try:
            if not nutricionista:
                raise CadastroInexistenteException
        except CadastroInexistenteException:
            self.__tela_avaliacao.mostra_mensagem(f"Nutricionista com cpf {dados_avaliacao['cpf_nutricionista']} não existe!")
            return

        avaliacao = Avaliacao(nome_avaliacao, cliente, nutricionista, dados_avaliacao["data"], dados_avaliacao["imc"], dados_avaliacao["tmb"])

        self.__avaliacoes.append(avaliacao)
        self.__tela_avaliacao.mostra_mensagem(f"Avaliacao '{avaliacao.nome}' incluida com sucesso!")

    def alterar_avaliacao(self):
            if not self.veriricar_se_avaliacoes_existem():
                return
            nome_alvo = self.__tela_avaliacao.seleciona_avaliacao()
            avaliacao = self.busca_avaliacao_por_nome(nome_alvo)

            try:
                if not avaliacao:
                    raise AvaliacaoInexistenteException

                self.__tela_avaliacao.mostra_mensagem("\nDigite os novos dados para a avaliação:")
                novos_dados = self.__tela_avaliacao.pega_dados_avaliacao()
                novo_nome = novos_dados["nome"]

                if novo_nome != nome_alvo and self.busca_avaliacao_por_nome(novo_nome):
                    self.__tela_avaliacao.mostra_mensagem(f"O nome '{novo_nome}' já está em uso por outra avaliação.")
                    return

                cliente = self.__controlador_cliente.buscar_cliente_por_cpf(novos_dados["cpf_cliente"])
                if not cliente:
                    raise ClienteInexistenteException

                nutricionista = self.__controlador_nutricionista.buscar_nutricionista_por_cpf(
                    novos_dados["cpf_nutricionista"])
                if not nutricionista:
                    raise CadastroInexistenteException

                avaliacao.nome = novo_nome
                avaliacao.cliente = cliente
                avaliacao.nutricionista = nutricionista
                avaliacao.data = novos_dados["data"]
                avaliacao.imc = novos_dados["imc"]
                avaliacao.taxa_mb = novos_dados["tmb"]

                self.__tela_avaliacao.mostra_mensagem("Avaliação alterada com sucesso!")

            except AvaliacaoInexistenteException as e:
                print(e)
            except ClienteInexistenteException as e:
               print(e)
            except CadastroInexistenteException as e:
               print(e)

    def list_avaliacao_cliente(self, cpf_cliente):

        if self.veriricar_se_avaliacoes_existem():
            for avaliacao in self.__avaliacoes:
                if avaliacao.cliente.cpf == cpf_cliente:
                    self.__tela_avaliacao.mostra_avaliacao(avaliacao)

    def lista_avaliacao_nutricionista(self, cpf_nutricionista):
        if self.veriricar_se_avaliacoes_existem():
            for avaliacao in self.__avaliacoes:
                if avaliacao.nutricionista.cpf == cpf_nutricionista:
                    self.__tela_avaliacao.mostra_avaliacao(avaliacao)


    def lista_avaliacao(self):
        if self.veriricar_se_avaliacoes_existem():
            for avaliacao in self.__avaliacoes:
                self.__tela_avaliacao.mostra_avaliacao(avaliacao)

    def remover_avaliacao(self):
        if not self.veriricar_se_avaliacoes_existem():
            return
        nome_avaliacao = self.__tela_avaliacao.seleciona_avaliacao()
        avaliacao = self.busca_avaliacao_por_nome(nome_avaliacao)

        try:
            if avaliacao:
                self.__avaliacoes.remove(avaliacao)
                self.__tela_avaliacao.mostra_mensagem(f"Avaliacao '{avaliacao.nome}' removida com sucesso!")
            else:
                raise AvaliacaoInexistenteException()
        except AvaliacaoInexistenteException as e:
            print(e)

    def busca_avaliacao_por_nome(self, nome: str):
        for avaliacao in self.__avaliacoes:
            if avaliacao.nome == nome:
                return avaliacao
        return None

    def retornar(self):
        pass

    def veriricar_se_avaliacoes_existem(self):
        if len(self.__avaliacoes) == 0:
            self.__tela_avaliacao.mostra_mensagem("Não há avaliacoes cadastradas!")
            return False
        else:
            return True
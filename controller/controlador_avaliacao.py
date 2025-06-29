from model.avaliacao import Avaliacao
from view.tela_avaliacao import TelaAvaliacao
from exception.avaliacao_inexistente_exception import AvaliacaoInexistenteException
from exception.cadastroInexistenteException import CadastroInexistenteException
from exception.cliente_inexistente_exception import ClienteInexistenteException
from controller.controlador_cliente import ControladorCliente
from controller.controlador_nutricionista import ControladorNutricionista
from model.cliente import Cliente
from model.nutricionista import Nutricionista
from dao.avaliacao_dao import AvaliacaoDAO


class ControladorAvaliacao:
    def __init__(self, controlador_sistema, controlador_cliente: ControladorCliente,
                 controlador_nutricionista: ControladorNutricionista):
        self.__tela_avaliacao = TelaAvaliacao()
        self.__controlador_cliente = controlador_cliente
        self.__controlador_nutricionista = controlador_nutricionista
        self.__controlador_sistema = controlador_sistema
        self.__avaliacao_dao = AvaliacaoDAO()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_avaliacao,
            2: self.lista_avaliacao,
            3: self.alterar_avaliacao,
            4: self.remover_avaliacao,
            5: self.relatorio_de_avaliacoes,
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
        codigo_avaliacao = dados_avaliacao["codigo"]

        if self.busca_avaliacao_por_codigo(codigo_avaliacao):
            self.__tela_avaliacao.mostra_mensagem(f"Já existe uma avaliação com o codigo '{codigo_avaliacao}'.")
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
            self.__tela_avaliacao.mostra_mensagem(
                f"Nutricionista com cpf {dados_avaliacao['cpf_nutricionista']} não existe!")
            return

        avaliacao = Avaliacao(codigo_avaliacao, cliente, nutricionista, dados_avaliacao["data"], dados_avaliacao["imc"],
                              dados_avaliacao["tmb"])

        self.__avaliacao_dao.add(avaliacao.codigo, avaliacao)
        self.__tela_avaliacao.mostra_mensagem(f"Avaliacao '{avaliacao.codigo}' incluida com sucesso!")

    def alterar_avaliacao(self):
        if not self.veriricar_se_avaliacoes_existem():
            return
        codigo_alvo = self.__tela_avaliacao.seleciona_avaliacao()
        avaliacao = self.busca_avaliacao_por_codigo(codigo_alvo)

        try:
            if not avaliacao:
                raise AvaliacaoInexistenteException

            self.__tela_avaliacao.mostra_mensagem("\nDigite os novos dados para a avaliação:")
            novos_dados = self.__tela_avaliacao.pega_dados_avaliacao()
            novo_codigo = novos_dados["codigo"]

            if novo_codigo != codigo_alvo and self.busca_avaliacao_por_codigo(novo_codigo):
                self.__tela_avaliacao.mostra_mensagem(f"O codigo '{novo_codigo}' já está em uso por outra avaliação.")
                return

            cliente = self.__controlador_cliente.buscar_cliente_por_cpf(novos_dados["cpf_cliente"])
            if not cliente:
                raise ClienteInexistenteException

            nutricionista = self.__controlador_nutricionista.buscar_nutricionista_por_cpf(
                novos_dados["cpf_nutricionista"])
            if not nutricionista:
                raise CadastroInexistenteException

            avaliacao.codigo = novo_codigo
            avaliacao.cliente = cliente
            avaliacao.nutricionista = nutricionista
            avaliacao.data = novos_dados["data"]
            avaliacao.imc = novos_dados["imc"]
            avaliacao.taxa_mb = novos_dados["tmb"]

            self.__avaliacao_dao.update(avaliacao.codigo, avaliacao)
            self.__tela_avaliacao.mostra_mensagem("Avaliação alterada com sucesso!")

        except AvaliacaoInexistenteException as e:
            print(e)
        except ClienteInexistenteException as e:
            print(e)
        except CadastroInexistenteException as e:
            print(e)

    def lista_avaliacao(self):
        if not self.__avaliacao_dao.get_all():
            self.__tela_avaliacao.mostra_mensagem("Nao ha avaliacoes cadastradas!")
        else:
            dados_para_tela = []
            for avaliacao in self.__avaliacao_dao.get_all():
                dados_para_tela.append({
                    "codigo": avaliacao.codigo,
                    "cliente_nome": avaliacao.cliente.nome,
                    "nutricionista_nome": avaliacao.nutricionista.nome,
                    "data": avaliacao.data,
                })
            self.__tela_avaliacao.mostra_avaliacao(dados_para_tela)

    def remover_avaliacao(self):
        if not self.veriricar_se_avaliacoes_existem():
            return
        codigo_avaliacao = self.__tela_avaliacao.seleciona_avaliacao()

        try:
            if self.__avaliacao_dao.get(codigo_avaliacao):
                self.__avaliacao_dao.remove(codigo_avaliacao)
                self.__tela_avaliacao.mostra_mensagem(f"Avaliacao '{codigo_avaliacao}' removida com sucesso!")
            else:
                raise AvaliacaoInexistenteException()
        except AvaliacaoInexistenteException as e:
            print(e)

    def busca_avaliacao_por_codigo(self, codigo: str):
        return self.__avaliacao_dao.get(codigo)

    def retornar(self):
        pass

    def veriricar_se_avaliacoes_existem(self):
        if len(self.__avaliacao_dao.get_all()) == 0:
            self.__tela_avaliacao.mostra_mensagem("Não há avaliacoes cadastradas!")
            return False
        else:
            return True

    def relatorio_de_avaliacoes(self):
        lista_opcoes = {
            1: self.relatorio_por_cliente,
            2: self.relatorio_por_nutricionista,
            0: self.retornar
        }

        while True:
            opcao = self.__tela_avaliacao.seleciona_tipo_de_relatorio()

            if opcao == 0:
                self.retornar()
                break

            funcao_escolhida = lista_opcoes.get(opcao)

            if funcao_escolhida:
                funcao_escolhida()
            else:
                self.__tela_avaliacao.mostra_mensagem("Opção inválida. Tente novamente.")

    def relatorio_por_cliente(self):
        cliente_alvo_cpf = self.__tela_avaliacao.selecionar_cliente_cpf()
        avaliacoes_do_cliente = []

        for avaliacao in self.__avaliacao_dao.get_all():
            if avaliacao.cliente.cpf == cliente_alvo_cpf:
                avaliacoes_do_cliente.append(avaliacao)

        if avaliacoes_do_cliente:
            dados_para_tela = []
            for avaliacao in avaliacoes_do_cliente:
                dados_para_tela.append({
                    "codigo": avaliacao.codigo,
                    "cliente_nome": avaliacao.cliente.nome,
                    "nutricionista_nome": avaliacao.nutricionista.nome,
                    "data": avaliacao.data,
                })
            self.__tela_avaliacao.mostra_avaliacao(dados_para_tela)
        else:
            self.__tela_avaliacao.mostra_mensagem(
                f"Nenhuma avaliação encontrada para o cliente com CPF {cliente_alvo_cpf}.")

    def relatorio_por_nutricionista(self):
        nutricionista_alvo_cpf = self.__tela_avaliacao.selecionar_nutricionista_cpf()
        avaliacoes_do_nutricionista = []

        for avaliacao in self.__avaliacao_dao.get_all():
            if avaliacao.nutricionista.cpf == nutricionista_alvo_cpf:
                avaliacoes_do_nutricionista.append(avaliacao)

        if avaliacoes_do_nutricionista:
            dados_para_tela = []
            for avaliacao in avaliacoes_do_nutricionista:
                dados_para_tela.append({
                    "codigo": avaliacao.codigo,
                    "cliente_nome": avaliacao.cliente.nome,
                    "nutricionista_nome": avaliacao.nutricionista.nome,
                    "data": avaliacao.data,
                })
            self.__tela_avaliacao.mostra_avaliacao(dados_para_tela)
        else:
            self.__tela_avaliacao.mostra_mensagem(
                f"Nenhuma avaliação encontrada para o nutricionista com CPF {nutricionista_alvo_cpf}.")
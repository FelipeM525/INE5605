from tkinter import Toplevel
from model.avaliacao import Avaliacao
from view.tela_avaliacao_tkinter import TelaAvaliacaoTk
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
        self.__tela_avaliacao = None
        self.__controlador_cliente = controlador_cliente
        self.__controlador_nutricionista = controlador_nutricionista
        self.__controlador_sistema = controlador_sistema
        self.__avaliacao_dao = AvaliacaoDAO()
        self.__top_level = None

    def abre_tela(self):
        self.__top_level = Toplevel(self.__controlador_sistema.root)
        self.__tela_avaliacao = TelaAvaliacaoTk(self.__top_level, self)
        self.__top_level.protocol("WM_DELETE_WINDOW", self.retornar)


    def incluir_avaliacao(self):
        dados_avaliacao = self.__tela_avaliacao.pega_dados_avaliacao()
        if not dados_avaliacao.get("codigo"):
            return

        codigo_avaliacao = dados_avaliacao["codigo"]

        if self.busca_avaliacao_por_codigo(codigo_avaliacao):
            self.__tela_avaliacao.mostra_mensagem("Erro", f"Já existe uma avaliação com o código '{codigo_avaliacao}'.")
            return

        try:
            cliente: Cliente = self.__controlador_cliente.buscar_cliente_por_cpf(dados_avaliacao["cpf_cliente"])
            if not cliente:
                raise ClienteInexistenteException

            nutricionista: Nutricionista = self.__controlador_nutricionista.buscar_nutricionista_por_cpf(
                dados_avaliacao["cpf_nutricionista"])
            if not nutricionista:
                raise CadastroInexistenteException

            avaliacao = Avaliacao(codigo_avaliacao, cliente, nutricionista, dados_avaliacao["data"], dados_avaliacao["imc"],
                                  dados_avaliacao["tmb"])

            self.__avaliacao_dao.add(avaliacao.codigo, avaliacao)
            self.__tela_avaliacao.mostra_mensagem("Sucesso", f"Avaliação '{avaliacao.codigo}' incluída com sucesso!")

        except ClienteInexistenteException:
            self.__tela_avaliacao.mostra_mensagem("Erro", f"Cliente com CPF {dados_avaliacao['cpf_cliente']} não existe!")
        except CadastroInexistenteException:
            self.__tela_avaliacao.mostra_mensagem("Erro", f"Nutricionista com CPF {dados_avaliacao['cpf_nutricionista']} não existe!")


    def alterar_avaliacao(self):
        if not self.verificar_se_avaliacoes_existem():
            return
        codigo_alvo = self.__tela_avaliacao.seleciona_avaliacao()
        if not codigo_alvo: return

        avaliacao = self.busca_avaliacao_por_codigo(codigo_alvo)

        try:
            if not avaliacao:
                raise AvaliacaoInexistenteException

            novos_dados = self.__tela_avaliacao.pega_dados_avaliacao()
            if not novos_dados.get("codigo"): return

            novo_codigo = novos_dados["codigo"]

            if novo_codigo != codigo_alvo and self.busca_avaliacao_por_codigo(novo_codigo):
                self.__tela_avaliacao.mostra_mensagem("Erro", f"O código '{novo_codigo}' já está em uso por outra avaliação.")
                return

            cliente = self.__controlador_cliente.buscar_cliente_por_cpf(novos_dados["cpf_cliente"])
            if not cliente: raise ClienteInexistenteException

            nutricionista = self.__controlador_nutricionista.buscar_nutricionista_por_cpf(
                novos_dados["cpf_nutricionista"])
            if not nutricionista: raise CadastroInexistenteException

            self.__avaliacao_dao.remove(codigo_alvo)

            avaliacao.codigo = novo_codigo
            avaliacao.cliente = cliente
            avaliacao.nutricionista = nutricionista
            avaliacao.data = novos_dados["data"]
            avaliacao.imc = novos_dados["imc"]
            avaliacao.taxa_mb = novos_dados["tmb"]

            self.__avaliacao_dao.add(avaliacao.codigo, avaliacao)
            self.__tela_avaliacao.mostra_mensagem("Sucesso", "Avaliação alterada com sucesso!")

        except AvaliacaoInexistenteException:
            self.__tela_avaliacao.mostra_mensagem("Erro", f"Avaliação com código {codigo_alvo} não existe!")
        except ClienteInexistenteException:
            self.__tela_avaliacao.mostra_mensagem("Erro", "Cliente não encontrado!")
        except CadastroInexistenteException:
            self.__tela_avaliacao.mostra_mensagem("Erro", "Nutricionista não encontrado!")


    def lista_avaliacao(self):
        if not self.__avaliacao_dao.get_all():
            self.__tela_avaliacao.mostra_mensagem("Info", "Não há avaliações cadastradas!")
        else:
            dados_para_tela = []
            for avaliacao in self.__avaliacao_dao.get_all():
                dados_para_tela.append({
                    "codigo": avaliacao.codigo,
                    "cliente_nome": avaliacao.cliente.nome,
                    "nutricionista_nome": avaliacao.nutricionista.nome,
                    "data": avaliacao.data,
                    "imc": avaliacao.imc,          # <-- ADICIONADO
                    "tmb": avaliacao.taxa_mb      # <-- ADICIONADO
                })
            self.__tela_avaliacao.mostra_avaliacao(dados_para_tela)

    def remover_avaliacao(self):
        if not self.verificar_se_avaliacoes_existem():
            return

        codigo_avaliacao = self.__tela_avaliacao.seleciona_avaliacao()
        if not codigo_avaliacao: return

        try:
            if self.__avaliacao_dao.get(codigo_avaliacao):
                self.__avaliacao_dao.remove(codigo_avaliacao)
                self.__tela_avaliacao.mostra_mensagem("Sucesso", f"Avaliação '{codigo_avaliacao}' removida com sucesso!")
            else:
                raise AvaliacaoInexistenteException()
        except AvaliacaoInexistenteException:
            self.__tela_avaliacao.mostra_mensagem("Erro", "Avaliação não existente!")

    def busca_avaliacao_por_codigo(self, codigo: str):
        return self.__avaliacao_dao.get(codigo)

    def retornar(self):
        self.__top_level.destroy()
        self.__controlador_sistema.reabre_tela_principal()

    def verificar_se_avaliacoes_existem(self):
        if len(self.__avaliacao_dao.get_all()) == 0:
            self.__tela_avaliacao.mostra_mensagem("Info", "Não há avaliações cadastradas!")
            return False
        return True

    def relatorio_de_avaliacoes(self):
        tipo = self.__tela_avaliacao.seleciona_tipo_de_relatorio()
        if tipo == "cliente":
            self.relatorio_por_cliente()
        elif tipo == "nutricionista":
            self.relatorio_por_nutricionista()

    def relatorio_por_cliente(self):
        cliente_alvo_cpf = self.__tela_avaliacao.selecionar_cliente_cpf()
        if not cliente_alvo_cpf: return

        avaliacoes_do_cliente = [ava for ava in self.__avaliacao_dao.get_all() if ava.cliente.cpf == cliente_alvo_cpf]

        if avaliacoes_do_cliente:
            dados_para_tela = [{
                "codigo": avaliacao.codigo, "cliente_nome": avaliacao.cliente.nome,
                "nutricionista_nome": avaliacao.nutricionista.nome, "data": avaliacao.data,
                "imc": avaliacao.imc,      # <-- ADICIONADO
                "tmb": avaliacao.taxa_mb  # <-- ADICIONADO
            } for avaliacao in avaliacoes_do_cliente]
            self.__tela_avaliacao.mostra_avaliacao(dados_para_tela)
        else:
            self.__tela_avaliacao.mostra_mensagem(
                "Info", f"Nenhuma avaliação encontrada para o cliente com CPF {cliente_alvo_cpf}.")

    def relatorio_por_nutricionista(self):
        nutri_alvo_cpf = self.__tela_avaliacao.selecionar_nutricionista_cpf()
        if not nutri_alvo_cpf: return

        avaliacoes_do_nutri = [ava for ava in self.__avaliacao_dao.get_all() if ava.nutricionista.cpf == nutri_alvo_cpf]

        if avaliacoes_do_nutri:
            dados_para_tela = [{
                "codigo": avaliacao.codigo, "cliente_nome": avaliacao.cliente.nome,
                "nutricionista_nome": avaliacao.nutricionista.nome, "data": avaliacao.data,
                "imc": avaliacao.imc,      # <-- ADICIONADO
                "tmb": avaliacao.taxa_mb  # <-- ADICIONADO
            } for avaliacao in avaliacoes_do_nutri]
            self.__tela_avaliacao.mostra_avaliacao(dados_para_tela)
        else:
            self.__tela_avaliacao.mostra_mensagem(
                "Info", f"Nenhuma avaliação encontrada para o nutricionista com CPF {nutri_alvo_cpf}.")
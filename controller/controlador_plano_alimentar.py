from tkinter import Toplevel
from exception.cliente_inexistente_exception import ClienteInexistenteException
from exception.nutricionista_inexistente_exception import NutricionistaInexistenteException
from exception.plano_inexistente_exception import PlanoInexistenteException
from exception.plano_ja_cadastrado_exception import PlanoJaCadastradoException
from exception.refeicao_inexistente_exception import RefeicaoInexistenteException
from model.plano_alimentar import PlanoAlimentar
from view.tela_plano_alimentar_tkinter import TelaPlanoAlimentarTk
from dao.plano_alimentar_dao import PlanoAlimentarDAO

class ControladorPlanoAlimentar:
    def __init__(self, controlador_cliente, controlador_nutricionista, controlador_refeicao, controlador_sistema):
        self.__plano_dao = PlanoAlimentarDAO()
        self.__tela_plano_alimentar = None
        self.__controlador_cliente = controlador_cliente
        self.__controlador_nutricionista = controlador_nutricionista
        self.__controlador_refeicao = controlador_refeicao
        self.__controlador_sistema = controlador_sistema
        self.__top_level = None

    def abre_tela(self):
        self.__top_level = Toplevel(self.__controlador_sistema.root)
        self.__tela_plano_alimentar = TelaPlanoAlimentarTk(self.__top_level, self)
        self.__top_level.protocol("WM_DELETE_WINDOW", self.retornar)

    def incluir_plano_alimentar(self):
        dados_plano = self.__tela_plano_alimentar.pegar_dados_plano()
        if not dados_plano.get("cpf_cliente"):
            self.__tela_plano_alimentar.mostra_mensagem("Cancelado", "Inclusão cancelada.")
            return

        try:
            cliente = self.__controlador_cliente.buscar_cliente_por_cpf(dados_plano["cpf_cliente"])
            if not cliente: raise ClienteInexistenteException()

            nutricionista = self.__controlador_nutricionista.buscar_nutricionista_por_cpf(dados_plano["cpf_nutricionista"])
            if not nutricionista: raise NutricionistaInexistenteException()

            if self.busca_plano_por_cliente(cliente.cpf):
                raise PlanoJaCadastradoException()

            plano = PlanoAlimentar([], nutricionista, cliente)
            self.__plano_dao.add(cliente.cpf, plano)
            self.__tela_plano_alimentar.mostra_mensagem("Sucesso", "Plano alimentar incluído!")
        except (ClienteInexistenteException, NutricionistaInexistenteException, PlanoJaCadastradoException) as e:
            self.__tela_plano_alimentar.mostra_mensagem("Erro", str(e))

    def inclui_refeicao_no_plano(self):
        cpf_cliente = self.__tela_plano_alimentar.seleciona_plano_por_cliente()
        if not cpf_cliente: return

        plano = self.busca_plano_por_cliente(cpf_cliente)
        if not plano:
            self.__tela_plano_alimentar.mostra_mensagem("Erro", f"Plano não encontrado para o cliente {cpf_cliente}.")
            return

        codigo_refeicao = self.__tela_plano_alimentar.seleciona_refeicao_cod()
        if not codigo_refeicao: return

        refeicao_nova = self.__controlador_refeicao.busca_refeicao_por_codigo(codigo_refeicao)
        if not refeicao_nova:
            self.__tela_plano_alimentar.mostra_mensagem("Erro", "Refeição não encontrada.")
            return

        plano.adicionar_refeicao(refeicao_nova)
        self.__plano_dao.update(plano.cliente.cpf, plano)
        self.__tela_plano_alimentar.mostra_mensagem("Sucesso", "Refeição incluída no plano!")

    def busca_plano_por_cliente(self, cpf_cliente):
        return self.__plano_dao.get(cpf_cliente)

    def remover_plano(self):
        cpf_cliente = self.__tela_plano_alimentar.seleciona_plano_por_cliente()
        if not cpf_cliente: return

        if self.busca_plano_por_cliente(cpf_cliente):
            self.__plano_dao.remove(cpf_cliente)
            self.__tela_plano_alimentar.mostra_mensagem("Sucesso", "Plano removido.")
        else:
            self.__tela_plano_alimentar.mostra_mensagem("Erro", "Plano não encontrado.")

    def remover_refeicao(self):
        cpf_cliente = self.__tela_plano_alimentar.seleciona_plano_por_cliente()
        if not cpf_cliente: return

        plano = self.busca_plano_por_cliente(cpf_cliente)
        if not plano:
            self.__tela_plano_alimentar.mostra_mensagem("Erro", "Plano não encontrado.")
            return

        codigo_refeicao = self.__tela_plano_alimentar.seleciona_refeicao_cod()
        if not codigo_refeicao: return

        refeicao_encontrada = next((r for r in plano.refeicoes if r.codigo == codigo_refeicao), None)
        if refeicao_encontrada:
            plano.refeicoes.remove(refeicao_encontrada)
            self.__plano_dao.update(plano.cliente.cpf, plano)
            self.__tela_plano_alimentar.mostra_mensagem("Sucesso", "Refeição removida do plano.")
        else:
            self.__tela_plano_alimentar.mostra_mensagem("Erro", "Refeição não encontrada no plano.")

    def listar_planos(self):
        planos = self.__plano_dao.get_all()
        if not planos:
            self.__tela_plano_alimentar.mostra_mensagem("Info", "Nenhum plano cadastrado.")
            return

        dados_para_tela = [{
            "codigo": p.cliente.cpf, "cliente_nome": p.cliente.nome,
            "nutricionista_nome": p.nutricionista.nome,
            "refeicoes": [r.codigo for r in p.refeicoes]
        } for p in planos]
        self.__tela_plano_alimentar.mostra_plano(dados_para_tela)

    def retornar(self):
        self.__top_level.destroy()
        self.__controlador_sistema.reabre_tela_principal()
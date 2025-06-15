from exception.cliente_inexistente_exception import ClienteInexistenteException
from exception.nutricionista_inexistente_exception import NutricionistaInexistenteException
from exception.plano_inexistente_exception import PlanoInexistenteException
from exception.plano_ja_cadastrado_exception import PlanoJaCadastradoException
from exception.refeicao_inexistente_exception import RefeicaoInexistenteException
from model.plano_alimentar import PlanoAlimentar
from view.tela_plano_alimentar import TelaPlanoAlimentar
from controller.controlador_refeicao import ControladorRefeicao
from view.tela_refeicao import TelaRefeicao
from controller.controlador_cliente import ControladorCliente
from controller.controlador_nutricionista import ControladorNutricionista


class ControladorPlanoAlimentar:

    def __init__(self, controlador_cliente: ControladorCliente, controlador_nutricionista: ControladorNutricionista, controlador_refeicao: ControladorRefeicao, controlador_sistema):
        self.__planos = []
        self.__tela_plano_alimentar = TelaPlanoAlimentar()
        self.__tela_refeicao = TelaRefeicao()
        self.__controlador_nutricionista = controlador_nutricionista
        self.__controlador_cliente = controlador_cliente
        self.__controlador_refeicao = controlador_refeicao
        self.__controlador_sistema = controlador_sistema

    def incluir_plano_alimentar(self):
        dados_plano = self.__tela_plano_alimentar.pegar_dados_plano()
        cpf_cliente = dados_plano["cpf_cliente"]
        cpf_nutricionista = dados_plano["cpf_nutricionista"]

        cliente = self.__controlador_cliente.buscar_cliente_por_cpf(cpf_cliente)
        try:
            if not cliente:
                raise ClienteInexistenteException
        except ClienteInexistenteException:
            self.__tela_plano_alimentar.mostra_mensagem(f"Cliente {cpf_cliente} nao existe!")

        nutricionista = self.__controlador_nutricionista.buscar_nutricionista_por_cpf(cpf_nutricionista)

        try:
            if not nutricionista:
                raise NutricionistaInexistenteException
        except NutricionistaInexistenteException:
            self.__tela_plano_alimentar.mostra_mensagem(f"Nutricionista com cpf {cpf_nutricionista} nao existe!")

        try:
            if cliente.plano_alimentar is None:
                plano_alimentar = PlanoAlimentar([], nutricionista, cliente)
                cliente.plano_alimentar = plano_alimentar
                self.__controlador_cliente.atualizar_cliente(cliente)
                self.__planos.append(plano_alimentar)
                return self.__tela_plano_alimentar.mostra_mensagem("Plano alimentar incluido com sucesso!")
            else:
                raise PlanoJaCadastradoException
        except PlanoJaCadastradoException:
            return self.__tela_plano_alimentar.mostra_mensagem(f"Cliente {cpf_cliente} ja possui um plano alimentar cadastrado!")

    def inclui_refeicao_no_plano(self):
        cpf_cliente = self.__tela_plano_alimentar.seleciona_plano_por_cliente()

        plano = self.busca_plano_por_cliente(cpf_cliente)

        try:
            if not plano:
                raise PlanoInexistenteException
        except PlanoInexistenteException:
            return self.__tela_plano_alimentar.mostra_mensagem(f"Plano alimentar nao existe para o cliente {cpf_cliente}!")

        nome_refeicao = self.__tela_refeicao.seleciona_refeicao()

        refeicao_nova = self.__controlador_refeicao.busca_refeicao_por_nome(nome_refeicao)

        try:
            if not refeicao_nova:
                raise RefeicaoInexistenteException
        except RefeicaoInexistenteException:
            return self.__tela_plano_alimentar.mostra_mensagem(f"Refeicao nao existe!")

        plano.refeicoes.append(refeicao_nova)
        self.__controlador_cliente.atualizar_cliente(plano.cliente)

        return self.__tela_plano_alimentar.mostra_mensagem(f"Refeicao incluida no plano alimentar!")

    def busca_plano_por_cliente(self, cpf_cliente):
        for plano in self.__planos:
            if plano.cliente.cpf == cpf_cliente:
                return plano
        return None

    def remover_plano(self):
        cpf_cliente = self.__tela_plano_alimentar.seleciona_plano_por_cliente()

        plano = self.busca_plano_por_cliente(cpf_cliente)

        try:
            if not plano:
                raise PlanoInexistenteException
        except PlanoInexistenteException:
            return self.__tela_plano_alimentar.mostra_mensagem(f"Plano alimentar nao existe para o cliente {cpf_cliente}!")

        self.__planos.remove(plano)
        self.__controlador_cliente.atualizar_cliente(plano.cliente)

        return self.__tela_plano_alimentar.mostra_mensagem("Plano alimentar removido com sucesso!")

    def remover_refeicao(self):
        cpf_cliente  = self.__tela_plano_alimentar.seleciona_plano_por_cliente()
        nome_refeicao = self.__tela_refeicao.seleciona_refeicao()

        plano = self.busca_plano_por_cliente(cpf_cliente)
        try:
            if not plano:
                raise PlanoInexistenteException
        except PlanoInexistenteException:
             return self.__tela_plano_alimentar.mostra_mensagem(f"Plano alimentar nao existe para o cliente {cpf_cliente}!")

        for refeicao in plano.refeicoes:
            if refeicao.nome == nome_refeicao:
                plano.refeicoes.remove(refeicao)
                return self.__tela_plano_alimentar.mostra_mensagem(f"Refeicao {nome_refeicao} removida do plano alimentar!")

        raise RefeicaoInexistenteException


    def listar_planos(self):
        if not self.__planos:
            return self.__tela_plano_alimentar.mostra_mensagem("Nao ha planos cadastrados!")
        else:
            for plano in self.__planos:
                self.__tela_plano_alimentar.mostra_plano(plano)
            return None

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_plano_alimentar,
            2: self.listar_planos,
            3: self.inclui_refeicao_no_plano,
            4: self.remover_refeicao,
            5: self.remover_plano,
            0: self.retornar
        }

        while True:
            opcao = self.__tela_plano_alimentar.mostra_tela()
            if opcao == 0:
                self.retornar()
                break

            funcao_escolhida = lista_opcoes.get(opcao)
            if funcao_escolhida:
                funcao_escolhida()
            else:
                self.__tela_plano_alimentar.mostra_mensagem("Opção inválida!")

    def retornar(self):
        pass





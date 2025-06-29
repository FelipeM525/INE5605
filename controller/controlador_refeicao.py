from view.tela_alimento import TelaAlimento
from exception.alimento_inexistente_exception import AlimentoInexistenteException
from exception.refeicao_existente_exception import RefeicaoExistenteException
from exception.refeicao_inexistente_exception import RefeicaoInexistenteException
from model.refeicao import Refeicao
from view.tela_plano_alimentar import TelaPlanoAlimentar
from view.tela_refeicao import TelaRefeicao
from dao.refeicao_dao import RefeicaoDAO


class ControladorRefeicao:
    def __init__(self, controlador_alimento, controlador_sistema):
        self.__controlador_alimento = controlador_alimento
        self.__controlador_sistema = controlador_sistema
        self.__tela_refeicao = TelaRefeicao()
        self.__tela_alimento = TelaAlimento()
        self.__tela_plano_alimentar = TelaPlanoAlimentar()
        self.__refeicao_dao = RefeicaoDAO()

    def incluir_refeicao(self):
        dados_refeicao = self.__tela_refeicao.pega_dados_refeicao()
        try:
            if self.busca_refeicao_por_codigo(dados_refeicao["codigo"]):
                raise RefeicaoExistenteException

            nova_refeicao = Refeicao(dados_refeicao["codigo"], [], dados_refeicao["tipo"])
            self.__refeicao_dao.add(nova_refeicao.codigo, nova_refeicao)

            return self.__tela_refeicao.mostra_mensagem(f"Refeicao incluida com sucesso!")
        except RefeicaoExistenteException:
            return self.__tela_refeicao.mostra_mensagem(f"Refeicao ja existe!")

    def busca_refeicao_por_codigo(self, codigo):
        return self.__refeicao_dao.get(codigo)

    def remover_refeicao(self):
        codigo_refeicao = self.__tela_refeicao.seleciona_refeicao()

        try:
            if self.busca_refeicao_por_codigo(codigo_refeicao):
                self.__refeicao_dao.remove(codigo_refeicao)
                self.__tela_refeicao.mostra_mensagem("Refeição removida do sistema com sucesso!")
            else:
                raise RefeicaoInexistenteException
        except RefeicaoInexistenteException:
            self.__tela_refeicao.mostra_mensagem(
                f"Erro: A refeição com código '{codigo_refeicao}' não foi encontrada no sistema.")

    def excluir_alimento_da_refeicao(self):
        codigo_refeicao = self.__tela_refeicao.seleciona_refeicao()
        nome_alimento = self.__tela_alimento.seleciona_alimento()
        refeicao = self.busca_refeicao_por_codigo(codigo_refeicao)

        try:
            if not refeicao:
                raise RefeicaoInexistenteException

            alimento_encontrado = None
            for alimento in refeicao.alimentos:
                if alimento.nome == nome_alimento:
                    alimento_encontrado = alimento
                    break

            if alimento_encontrado:
                refeicao.alimentos.remove(alimento_encontrado)
                self.__refeicao_dao.update(refeicao.codigo, refeicao)
                return self.__tela_refeicao.mostra_mensagem(
                    f"Alimento '{nome_alimento}' removido da refeição '{refeicao.codigo}' com sucesso!")
            else:
                return self.__tela_refeicao.mostra_mensagem(
                    f"Alimento '{nome_alimento}' não encontrado na refeição '{refeicao.codigo}'.")

        except RefeicaoInexistenteException:
            return self.__tela_refeicao.mostra_mensagem(f"Refeição '{codigo_refeicao}' não existe!")

    def incluir_alimento_na_refeicao(self):
        codigo_refeicao = self.__tela_refeicao.seleciona_refeicao()
        refeicao = self.busca_refeicao_por_codigo(codigo_refeicao)
        try:
            if not refeicao:
                raise RefeicaoInexistenteException
        except RefeicaoInexistenteException:
            return self.__tela_refeicao.mostra_mensagem(f"Refeicao {codigo_refeicao} nao existe!")

        nome_alimento = self.__tela_alimento.seleciona_alimento()

        try:
            alimento = self.__controlador_alimento.buscar_alimento_por_nome(nome_alimento)

            if not alimento:
                raise AlimentoInexistenteException

            refeicao.adicionar_alimento(alimento)
            self.__refeicao_dao.update(refeicao.codigo, refeicao)

            return self.__tela_refeicao.mostra_mensagem(
                f"Alimento {nome_alimento} incluido na refeicao {codigo_refeicao} com sucesso!")
        except AlimentoInexistenteException:
            return self.__tela_refeicao.mostra_mensagem(f"Alimento {nome_alimento} nao existe!")

    def listar_refeicoes(self):
        refeicoes = self.__refeicao_dao.get_all()
        if not refeicoes:
            self.__tela_refeicao.mostra_mensagem("Nenhuma refeicao cadastrada!")
        else:
            dados_para_tela = []
            for refeicao in refeicoes:
                alimentos_da_refeicao = [alimento.nome for alimento in refeicao.alimentos]
                dados_para_tela.append({
                    "codigo": refeicao.codigo,
                    "tipo": refeicao.tipo,
                    "calorias_total": refeicao.calorias_totais(),
                    "alimentos": alimentos_da_refeicao
                })
            self.__tela_refeicao.mostra_refeicao(dados_para_tela)

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_refeicao, 2: self.listar_refeicoes, 3: self.incluir_alimento_na_refeicao,
                        4: self.excluir_alimento_da_refeicao, 5: self.remover_refeicao, 0: self.retornar}

        while True:
            opcao = self.__tela_refeicao.mostrar_menu()
            if opcao == 0:
                self.retornar()
                break

            funcao_escolhida = lista_opcoes.get(opcao)
            if funcao_escolhida:
                funcao_escolhida()
            else:
                self.__tela_refeicao.mostra_mensagem("Opção inválida!")

    def retornar(self):
        pass
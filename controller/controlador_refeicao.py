from view.tela_alimento import TelaAlimento
from exception.alimento_inexistente_exception import AlimentoInexistenteException
from exception.refeicao_existente_exception import RefeicaoExistenteException
from exception.refeicao_inexistente_exception import RefeicaoInexistenteException
from model.refeicao import Refeicao
from view.tela_plano_alimentar import TelaPlanoAlimentar
from view.tela_refeicao import TelaRefeicao
from exception.plano_inexistente_exception import PlanoInexistenteException


class ControladorRefeicao:
    def __init__(self, controlador_alimento, controlador_sistema):
        self.__controlador_alimento = controlador_alimento
        self.__controlador_sistema = controlador_sistema
        self.__tela_refeicao = TelaRefeicao()
        self.__tela_alimento = TelaAlimento()
        self.__tela_plano_alimentar = TelaPlanoAlimentar()
        self.__refeicoes = []

    def incluir_refeicao(self):
        dados_refeicao = self.__tela_refeicao.pega_dados_refeicao()
        alimentos = []
        try:
            refeicao = self.busca_refeicao_por_codigo(dados_refeicao["codigo"])
            if refeicao:
                raise RefeicaoExistenteException

            self.__refeicoes.append(Refeicao(dados_refeicao["codigo"], alimentos, dados_refeicao["tipo"]))

            return self.__tela_refeicao.mostra_mensagem(f"Refeicao incluida com sucesso!")
        except RefeicaoExistenteException:
            return self.__tela_refeicao.mostra_mensagem(f"Refeicao ja existe!")

    def busca_refeicao_por_codigo(self, codigo):
        for refeicao in self.__refeicoes:
            if refeicao.codigo == codigo:
                return refeicao
        return None

    def remover_refeicao(self):
        codigo_refeicao = self.__tela_refeicao.seleciona_refeicao()
        refeicao = self.busca_refeicao_por_codigo(codigo_refeicao)

        try:
            if refeicao:
                self.__refeicoes.remove(refeicao)
                self.__tela_refeicao.mostra_mensagem("Refeição removida do sistema com sucesso!")
            else:
                raise RefeicaoInexistenteException
        except RefeicaoInexistenteException:
            self.__tela_refeicao.mostra_mensagem(
                f"Erro: A refeição com código '{codigo_refeicao}' não foi encontrada no sistema.")

    def excluir_alimento_da_refeicao(self):
        codigo = self.__tela_refeicao.seleciona_refeicao()
        nome_alimento = self.__tela_alimento.seleciona_alimento()
        refeicao = self.busca_refeicao_por_codigo(codigo)

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
                return self.__tela_refeicao.mostra_mensagem(
                    f"Alimento '{nome_alimento}' removido da refeição '{codigo}' com sucesso!")
            else:
                return self.__tela_refeicao.mostra_mensagem(
                    f"Alimento '{nome_alimento}' não encontrado na refeição '{codigo}'.")

        except RefeicaoInexistenteException:
            return self.__tela_refeicao.mostra_mensagem(f"Refeição '{codigo}' não existe!")

    def incluir_alimento_na_refeicao(self):
        codigo = self.__tela_refeicao.seleciona_refeicao()
        refeicao = self.busca_refeicao_por_codigo(codigo)
        try:
            if not refeicao:
                raise RefeicaoInexistenteException
        except RefeicaoInexistenteException:
            return self.__tela_refeicao.mostra_mensagem(f"Refeicao {codigo} nao existe!")

        nome_alimento = self.__tela_alimento.seleciona_alimento()

        try:
            alimento = self.__controlador_alimento.buscar_alimento_por_nome(nome_alimento)

            if not alimento:
                raise AlimentoInexistenteException

            refeicao.adicionar_alimento(alimento)

            return self.__tela_refeicao.mostra_mensagem(f"Alimento {nome_alimento} incluido na refeicao {codigo} com sucesso!")
        except AlimentoInexistenteException:
            return self.__tela_refeicao.mostra_mensagem(f"Alimento {nome_alimento} nao existe!")

    def listar_refeicoes(self):
        if not self.__refeicoes:
            self.__tela_refeicao.mostra_mensagem("Nenhuma refeicao cadastrada!")
        else:
            dados_para_tela = []
            for refeicao in self.__refeicoes:
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
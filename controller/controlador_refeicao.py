from view.tela_alimento import TelaAlimento
from exception.alimento_inexistente_exception import AlimentoInexistenteException
from exception.refeicao_existente_exception import RefeicaoExistenteException
from exception.refeicao_inexistente_exception import RefeicaoInexistenteException
from model.refeicao import Refeicao
from view.tela_refeicao import TelaRefeicao
from exception.plano_inexistente_exception import PlanoInexistenteException


class ControladorRefeicao:
    def __init__(self, controlador_alimento, controlador_sistema):
        self.__controlador_alimento = controlador_alimento
        self.__controlador_sistema = controlador_sistema
        self.__tela_refeicao = TelaRefeicao()
        self.__tela_alimento = TelaAlimento()
        self.__refeicoes = []

    def incluir_refeicao(self):
        dados_refeicao = self.__tela_refeicao.pega_dados_refeicao()
        alimentos = []
        try:
            refeicao = self.busca_refeicao_por_nome(dados_refeicao["nome"])
            if refeicao:
                raise RefeicaoExistenteException

            self.__refeicoes.append(Refeicao(dados_refeicao["nome"], alimentos, dados_refeicao["tipo"]))

            return self.__tela_refeicao.mostra_mensagem(f"Refeicao incluida com sucesso!")
        except RefeicaoExistenteException:
            return self.__tela_refeicao.mostra_mensagem(f"Refeicao ja existe!")
    def busca_refeicao_por_nome(self, nome):
        for refeicao in self.__refeicoes:
            if refeicao.nome == nome:
                return refeicao
        return None

    def remover_refeicao(self):
        cpf_cliente = self.__tela_plano_alimentar.seleciona_plano_por_cliente()
        try:
            plano = self.busca_plano_por_cliente(cpf_cliente)
            
            nome_refeicao = self.__tela_refeicao.seleciona_refeicao()
            refeicao_encontrada = None
            for refeicao in plano.refeicoes:
                if refeicao.nome == nome_refeicao:
                    refeicao_encontrada = refeicao
                    break
            
            if refeicao_encontrada:
                plano.refeicoes.remove(refeicao_encontrada)
                self.__tela_plano_alimentar.mostra_mensagem(f"Refeição '{nome_refeicao}' removida do plano alimentar!")
            else:
                raise RefeicaoInexistenteException

        except PlanoInexistenteException:
            self.__tela_plano_alimentar.mostra_mensagem(f"Erro: Não foi encontrado um plano alimentar para o CPF {cpf_cliente}.")
        except RefeicaoInexistenteException:
            self.__tela_plano_alimentar.mostra_mensagem(f"Erro: A refeição '{nome_refeicao}' não foi encontrada neste plano.")


    def excluir_alimento_da_refeicao(self):
        nome = self.__tela_refeicao.seleciona_refeicao()
        nome_alimento = self.__tela_alimento.seleciona_alimento()
        refeicao = self.busca_refeicao_por_nome(nome)

        try:
            if not refeicao:
                raise RefeicaoInexistenteException

            for alimento in refeicao.alimentos:
                if alimento.nome == nome_alimento:
                    refeicao.alimentos.remove(alimento)
                    return self.__tela_refeicao.mostra_mensagem(
                        f"Alimento {nome_alimento} removido da refeicao {nome} com sucesso!")
                else:
                    return self.__tela_refeicao.mostra_mensagem(f"Alimento {nome_alimento} nao encontrado na refeicao {nome}")
        except RefeicaoInexistenteException:
            return self.__tela_refeicao.mostra_mensagem(f"Refeicao {nome} nao existe!")

        return None

    def incluir_alimento_na_refeicao(self):
        nome = self.__tela_refeicao.seleciona_refeicao()
        refeicao = self.busca_refeicao_por_nome(nome)
        try:
            if not refeicao:
                raise RefeicaoInexistenteException
        except RefeicaoInexistenteException:
            return self.__tela_refeicao.mostra_mensagem(f"Refeicao {nome} nao existe!")

        nome_alimento = self.__tela_alimento.seleciona_alimento()

        try:
            alimento = self.__controlador_alimento.busca_alimento_por_nome(nome_alimento)

            if not alimento:
                raise AlimentoInexistenteException

            refeicao.adicionar_alimento(alimento)

            return self.__tela_refeicao.mostra_mensagem(f"Alimento {nome_alimento} incluido na refeicao {nome} com sucesso!")
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
                    "nome": refeicao.nome,
                    "horario": refeicao.horario,
                    "tipo": refeicao.tipo_refeicao.value,
                    "calorias_total": refeicao.calcular_calorias_total(),
                    "alimentos": alimentos_da_refeicao
                })
            self.__tela_refeicao.mostra_refeicao(dados_para_tela)

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_refeicao, 2: self.listar_refeicoes, 3: self.incluir_alimento_na_refeicao,
                        4: self.excluir_alimento_da_refeicao, 5: self.excluir_refeicao, 0: self.retornar}

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
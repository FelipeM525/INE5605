from plano.plano_alimentar import PlanoAlimentar
from refeicoes.tela_refeicao import TelaRefeicao


class TelaPlanoAlimentar:

    def __init__(self):
        self.__tela_refeicao = TelaRefeicao()

    def mostra_tela(self):
        print('-------Plano Alimentar-------')
        print("1 - Adicionar Plano Alimentar")
        print("2 - Listar Planos Alimentares")
        print("3 - Adicionar Refeicao ao plano")
        print("4 - Remover Refeicao do plano")
        print("5 - Remover Plano Alimentar")
        print("6 - Sair")
        return int(input("Escolha uma opcao: "))

    def pegar_dados_plano(self):
        print("------- DADOS PLANO ALIMENTAR -------")
        cpf_cliente = input("Digite o cpf do cliente: ")
        cpf_nutricionista = input("Digite o cpf do nutricionista: ")


        return {"cpf_cliente": cpf_cliente, "cpf_nutricionista": cpf_nutricionista}

    def mostra_plano(self, plano: PlanoAlimentar):
        print("Informacoes do plano alimentar:")
        print(plano.__str__())

    def seleciona_plano_por_cliente(self):
        return input("Cpf do cliente pertencente ao plano: ")

    def mostra_mensagem(self, msg):
        print(msg)
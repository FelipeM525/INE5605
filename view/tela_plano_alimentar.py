from model.plano_alimentar import PlanoAlimentar
from view.tela_refeicao import TelaRefeicao


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
        print("0 - Sair")

        while True:
            try:
                opcao = int(input("Escolha uma opcao: "))
                return opcao
            except ValueError:
                self.mostra_mensagem("Opção inválida. Por favor, digite um número.")

    def pegar_dados_plano(self):
        print("------- DADOS PLANO ALIMENTAR -------")
        while True:
            cpf_cliente = input("Digite o CPF do cliente (apenas números): ").strip()
            if cpf_cliente.isdigit() and len(cpf_cliente) == 11:
                break
            self.mostra_mensagem("CPF do cliente inválido. Deve conter 11 dígitos numéricos.")

        while True:
            cpf_nutricionista = input("Digite o CPF do nutricionista (apenas números): ").strip()
            if cpf_nutricionista.isdigit() and len(cpf_nutricionista) == 11:
                break
            self.mostra_mensagem("CPF do nutricionista inválido. Deve conter 11 dígitos numéricos.")
        
        return {"cpf_cliente": cpf_cliente, "cpf_nutricionista": cpf_nutricionista}

    def mostra_plano(self, dados_planos):
        print("---------- LISTA DE PLANOS ALIMENTARES ----------")
        if not dados_planos:
            print("Nenhum plano para mostrar.")
            return

        for plano in dados_planos:
            print(f"Código do Plano (CPF do Cliente): {plano['codigo']}")
            print(f"Cliente: {plano['cliente_nome']}")
            print(f"Nutricionista: {plano['nutricionista_nome']}")
            print("Refeições:")
            if plano['refeicoes']:
                for refeicao in plano['refeicoes']:
                    print(f"- {refeicao}")
            else:
                print("- Nenhuma refeição associada a este plano.")
            print("-" * 30)

    def seleciona_plano_por_cliente(self):
        while True:
            cpf = input("Digite o CPF do cliente pertencente ao plano (apenas números): ").strip()
            if cpf.isdigit() and len(cpf) == 11:
                return cpf
            self.mostra_mensagem("CPF inválido. Deve conter 11 dígitos numéricos.")

    def mostra_mensagem(self, msg):
        print(msg)
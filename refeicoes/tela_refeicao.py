from refeicoes.refeicao import Refeicao
from refeicoes.tipo_refeicao import TipoRefeicao


class TelaRefeicao:
    def mostrar_menu(self):
        print("---------- REFEIÇÕES ------------")
        print("Opcoes:")
        print("1 - Criar refeição")
        print("2 - Listar refeições")
        print("3 - Adicionar alimento à refeição")
        print("4 - Remover alimento da refeição")
        print("5 - Excluir refeição")
        print("0 - Sair")

        while True:
            try:
                opcao = int(input("Escolha uma opcao: "))
                return opcao
            except ValueError:
                self.mostra_mensagem("Opção inválida. Por favor, digite um número.")

    def pega_dados_refeicao(self):
        print("------- DADOS REFEIÇÃO -------")
        print("\nTipos de refeição disponíveis:")
        tipo_refeicao = self.mostra_menu_tipo_refeicao()

        nomes_alimento = []
        while True:
            try:
                quantidade = int(input("Digite a quantidade de alimentos para adicionar: "))
                if quantidade >= 0:
                    break
                else:
                    self.mostra_mensagem("A quantidade não pode ser um número negativo.")
            except ValueError:
                self.mostra_mensagem("Por favor, digite um número válido.")

        for i in range(quantidade):
            while True:
                nome_alimento = input(f"Insira o nome do alimento {i + 1}: ").strip()
                if nome_alimento:
                    nomes_alimento.append(nome_alimento)
                    break
                else:
                    self.mostra_mensagem("O nome do alimento não pode ser vazio.")
        
        while True:
            nome = input("Digite um nome para a refeição: ").strip()
            if nome:
                break
            else:
                self.mostra_mensagem("O nome da refeição não pode ser vazio.")

        return {
            "nome": nome,
            "tipo": tipo_refeicao,
            "nomes_alimento": nomes_alimento
        }

    def mostra_refeicao(self, refeicao: Refeicao):
        print("\n----- INFORMAÇÕES DA REFEIÇÃO -----")
        print(refeicao.__str__())

    def seleciona_refeicao(self):
        while True:
            nome = input("Digite o nome da refeicao: ").strip()
            if nome:
                return nome
            else:
                self.mostra_mensagem("O nome da refeição não pode ser vazio.")

    def mostra_menu_tipo_refeicao(self):
        for i, tipo in enumerate(TipoRefeicao, 1):
            print(f"{i} - {tipo.value}")

        while True:
            try:
                opcao = int(input("\nEscolha o tipo de refeição: "))
                if 1 <= opcao <= len(TipoRefeicao):
                    tipo_refeicao = list(TipoRefeicao)[opcao - 1].value
                    break
                print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Por favor, digite um número válido.")
        return tipo_refeicao

    def mostra_mensagem(self, msg):
        print(msg)
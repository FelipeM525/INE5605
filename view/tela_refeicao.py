from model.TipoRefeicao import TipoRefeicao


class TelaRefeicao:
    def mostrar_menu(self):
        print("---------- REFEIÇÕES ------------")
        print("Opcoes:")
        print("1 - Criar refeição")
        print("2 - Listar refeições")
        print("3 - Adicionar alimento à refeição")
        print("4 - Remover alimento da refeição")
        print("5 - Excluir refeição")
        print("6 - Sair")
        return int(input("Escolha uma opcao: "))

    def pega_dados_refeicao(self):
        print("------- DADOS REFEIÇÃO -------")
        print("\nTipos de refeição disponíveis:")
        tipo_refeicao = self.mostra_menu_tipo_refeicao()

        nomes_alimento = []
        try:
            quantidade = int(input("Digite uma quantidade de alimentos par adicionar: "))

            for i in range(quantidade):
                nomes_alimento.append(input("insira o nome do alimento:"))
        except ValueError:
            print("Por favor, digite um número válido.")


        return {
            "tipo": tipo_refeicao,
            "nomes_alimento": nomes_alimento
        }


    def mostra_refeicao(self, dados_refeicao):
        print("\n----- INFORMAÇÕES DA REFEIÇÃO -----")
        for  key, value in dados_refeicao.items():
            print(f"{key}: {value}")


    def excluir_refeicao(self):
        print("Escolha uma refeicao para excluir: ")

        return self.mostra_menu_tipo_refeicao()

    def excluir_alimento_refeicao(self):
        print("Escolha uma refeicao para excluir: ")
        tipo_refeicao = self.mostra_menu_tipo_refeicao()

        nome_alimento = input("digite o nome do alimento a ser excluido:")

        return {"tipo_refeicao": tipo_refeicao, "nome_alimento": nome_alimento}

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



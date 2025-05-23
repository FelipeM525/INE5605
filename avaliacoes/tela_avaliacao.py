class TelaAvaliacao:
    def mostrar_menu(self):
        print("---------- AVALIACAO ------------")
        print("Opcoes:")
        print("1 - Cadastrar avaliacao")
        print("2 - Listar avaliacoes")
        print("3 - Excluir avaliacao")
        print("3 - Sair")
        return int(input("Escolha uma opcao: "))

    def pega_dados_avaliacao(self):
        print("------- DADOS AVALIACAO -------")
        cpf_cliente = input("Digite o cpf do cliente: ")
        cpf_nutricionista = input("Digite o cpf do nutricionista: ")
        data = input("Digite a data da avaliacao: ")
        imc = float(input("Digite o IMC: "))
        tmb = int(input("Digite a tmb: "))

        return {"cpf_cliente": cpf_cliente, "cpf_nutricionista": cpf_nutricionista, "data": data, "imc": imc, "tmb": tmb}


    def mostra_avaliacao(self, dados_avaliacao):
        print("Informacaoes da avaliacao:")
        for key, value in dados_avaliacao.items():
            print(f"{key}: {value}")

    def excluir_avaliacao(self):
        return input("Digite o cpf do cliente a ser excluido: ")

    def mostra_mensagem(self, msg):
        print(msg)


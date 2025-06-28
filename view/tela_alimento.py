class TelaAlimento():

    def tela_opcoes(self):
        print("---------- Alimentos ----------")
        print("Escolha a opcao")
        print("1 - Incluir Alimento")
        print("2 - Alterar Alimento")
        print("3 - Listar Alimentos")
        print("4 - Excluir Alimento")
        print("0 - Retornar")

        while True:
            try:
                opcao = int(input("Escolha a opcao: "))
                if opcao in [0, 1, 2, 3, 4]:
                    return opcao
                else:
                    print("Opção inválida. Digite um número entre 0 e 4.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

    def pega_dados_alimento(self):
        print("---------- DADOS ALIMENTO ----------")
        while True:
            nome = input("Nome: ").strip()
            if nome:
                break
            else:
                print("O nome não pode ser vazio.")

        while True:
            try:
                calorias = float(input("Calorias: "))
                carboidratos = float(input("Carboidratos (g): "))
                proteinas = float(input("Proteínas (g): "))
                gorduras = float(input("Gorduras (g): "))
                return {"nome": nome, "calorias": calorias, "carboidratos": carboidratos, "proteinas": proteinas,
                        "gorduras": gorduras}
            except ValueError:
                print("Entrada inválida. Certifique-se de que os valores numéricos estão corretos.")

    def mostra_alimento(self, dados_alimentos):
        print("---------- LISTA DE ALIMENTOS ----------")
        if not dados_alimentos:
            print("Nenhum alimento para mostrar.")
            return

        for alimento in dados_alimentos:
            print(f"Nome: {alimento['nome']}")
            print(f"Calorias: {alimento['calorias']} kcal")
            print(f"Carboidratos: {alimento['carboidratos']}g")
            print(f"Proteínas: {alimento['proteinas']}g")
            print(f"Gorduras: {alimento['gorduras']}g")
            print("-" * 20)

    def seleciona_alimento(self):
        while True:
            nome = input("Nome do alimento que deseja selecionar: ").strip()
            if nome:
                return nome
            else:
                print("O nome do alimento não pode ser vazio.")

    def mostra_mensagem(self, msg):
        print(msg)
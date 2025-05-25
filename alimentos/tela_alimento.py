from alimentos.alimento import Alimento


class TelaAlimento:
    def mostrar_menu(self):
        print("---------- ALIMENTOS ------------")
        print("Opcoes:")
        print("1 - Cadastrar alimento")
        print("2 - Listar alimentos")
        print("3 - Sair")

        while True:
            try:
                opcao = int(input("Escolha uma opcao: "))
                return opcao
            except ValueError:
                self.mostra_mensagem("Opção inválida. Por favor, digite um número.")

    def pega_dados_alimento(self):
        print("------- DADOS ALIMENTO -------")

        while True:
            nome = input("Digite o nome do alimento: ").strip()
            if nome:
                break
            else:
                self.mostra_mensagem("O nome do alimento não pode ser vazio.")
        
        while True:
            try:
                calorias = float(input("Digite as calorias (kcal): "))
                carboidratos = float(input("Digite os carboidratos (g): "))
                gorduras = float(input("Digite as gorduras (g): "))
                proteinas = float(input("Digite as proteinas (g): "))
                
                if all(valor >= 0 for valor in [calorias, carboidratos, gorduras, proteinas]):
                    break
                else:
                    print("Os valores nutricionais não podem ser negativos. Tente novamente.")
            except ValueError:
                print("Por favor, digite valores numéricos válidos.")

        return {
            "nome": nome,
            "calorias": calorias,
            "carboidratos": carboidratos,
            "gorduras": gorduras,
            "proteinas": proteinas
        }

    def mostra_alimento(self, alimento: Alimento):
        print("\n----- INFORMAÇÕES DO ALIMENTO -----")
        print(alimento.__str__())


    def mostra_mensagem(self, msg):
        print(msg)

    def seleciona_alimento(self):
        while True:
            nome = input("Digite o nome do alimento: ").strip()
            if nome:
                return nome
            else:
                self.mostra_mensagem("O nome do alimento não pode ser vazio.")
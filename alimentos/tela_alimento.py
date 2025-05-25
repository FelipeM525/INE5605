from alimentos.alimento import Alimento


class TelaAlimento:
    def mostrar_menu(self):
        print("---------- ALIMENTOS ------------")
        print("Opcoes:")
        print("1 - Cadastrar alimento")
        print("2 - Listar alimentos")
        print("3 - Sair")
        return int(input("Escolha uma opcao: "))

    def pega_dados_alimento(self):
        print("------- DADOS ALIMENTO -------")
        nome = input("Digite o nome do alimento: ")
        
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
        return input("Digite o nome do alimento: ")

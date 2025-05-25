from avaliacoes.avaliacao import Avaliacao


class TelaAvaliacao:
    def mostrar_menu(self):
        print("---------- AVALIACAO ------------")
        print("Opcoes:")
        print("1 - Cadastrar avaliacao")
        print("2 - Listar avaliacoes")
        print("3 - Excluir avaliacao")
        print("4 - Sair")
        return int(input("Escolha uma opcao: "))

    def pega_dados_avaliacao(self):
        print("------- DADOS AVALIACAO -------")
        cpf_cliente = input("Digite o cpf do cliente: ")
        cpf_nutricionista = input("Digite o cpf do nutricionista: ")
        data = input("Digite a data da avaliacao: ")
        imc = float(input("Digite o IMC: "))
        tmb = int(input("Digite a tmb: "))

        return {"cpf_cliente": cpf_cliente, "cpf_nutricionista": cpf_nutricionista, "data": data, "imc": imc, "tmb": tmb}


    def mostra_avaliacao(self, avaliacao: Avaliacao):
        print("Informacaoes da avaliacao:")
        print(avaliacao.__str__())

    def seleciona_avaliacao(self):
        return input("Digite o cpf do cliente cuja avaliacao sera excluida: ")

    def mostra_mensagem(self, msg):
        print(msg)
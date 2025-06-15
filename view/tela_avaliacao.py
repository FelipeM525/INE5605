from model.avaliacao import Avaliacao


class TelaAvaliacao:
    def mostrar_menu(self):
        print("---------- AVALIACAO ------------")
        print("Opcoes:")
        print("1 - Cadastrar avaliacao")
        print("2 - Listar avaliacoes")
        print("3 - Alterar avaliacao")
        print("4 - Excluir avaliacao")
        print("0 - Sair")

        while True:
            try:
                opcao = int(input("Escolha uma opcao: "))
                return opcao
            except ValueError:
                self.mostra_mensagem("Opção inválida. Por favor, digite um número.")

    def pega_dados_avaliacao(self):
        print("------- DADOS AVALIACAO -------")

        while True:
            nome = input("Digite um nome para a avaliação (ex: Avaliação Inicial): ").strip()
            if nome:
                break
            self.mostra_mensagem("O nome não pode ser vazio.")

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

        while True:
            data = input("Digite a data da avaliacao (ex: DD/MM/AAAA): ").strip()
            if data:  # Validação simples para não ser vazio
                break
            self.mostra_mensagem("A data não pode ser vazia.")

        while True:
            try:
                imc = float(input("Digite o IMC: "))
                if imc > 0:
                    break
                self.mostra_mensagem("O IMC deve ser um número positivo.")
            except ValueError:
                self.mostra_mensagem("Entrada inválida. Por favor, digite um número para o IMC.")

        while True:
            try:
                tmb = int(input("Digite a TMB (Taxa Metabólica Basal): "))
                if tmb > 0:
                    break
                self.mostra_mensagem("A TMB deve ser um número positivo.")
            except ValueError:
                self.mostra_mensagem("Entrada inválida. Por favor, digite um número inteiro para a TMB.")

        return {"nome": nome, "cpf_cliente": cpf_cliente, "cpf_nutricionista": cpf_nutricionista, "data": data, "imc": imc, "tmb": tmb}


    def mostra_avaliacao(self, avaliacao: Avaliacao):
        print("----Informacoes da avaliação:----")
        print(avaliacao)

    def seleciona_avaliacao(self):
        while True:
            nome = input("Digite o NOME da avaliação: ").strip()
            if nome:
                return nome
            else:
                self.mostra_mensagem("O nome não pode ser vazio.")

    def mostra_mensagem(self, msg):
        print(msg)
from model.avaliacao import Avaliacao


class TelaAvaliacao:
    def mostrar_menu(self):
        print("---------- AVALIACAO ------------")
        print("Opcoes:")
        print("1 - Cadastrar avaliacao")
        print("2 - Listar avaliacoes")
        print("3 - Alterar avaliacao")
        print("4 - Excluir avaliacao")
        print("5 - Relatorio de avaliacao")
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
            codigo = input("Digite um codigo para a avaliação (ex: 123): ").strip()
            if codigo:
                break
            self.mostra_mensagem("O codigo não pode ser vazio.")

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

        return {"codigo": codigo, "cpf_cliente": cpf_cliente, "cpf_nutricionista": cpf_nutricionista, "data": data, "imc": imc, "tmb": tmb}

    def mostra_avaliacao(self, dados_avaliacoes):
        print("---------- LISTA DE AVALIACOES ----------")
        for dados in dados_avaliacoes:
            print(f"Codigo: {dados['codigo']}")
            print(f"Cliente: {dados['cliente_nome']}")
            print(f"Nutricionista: {dados['nutricionista_nome']}")
            print(f"Data: {dados['data']}")
#            print(f"Massa Magra: {dados['massa_magra']:.2f}%")
#            print(f"Gordura Corporal: {dados['taxa_gordura']:.2f}%")
            print("-" * 20)

    def mostra_relatorio_gordura(self, dados_relatorio):
        print("---------- RELATORIO DE GORDURA CORPORAL ----------")
        for dados in dados_relatorio:
            print(
                f"Cliente: {dados['cliente_nome']}, Gordura Corporal: {dados['taxa_gordura']:.2f}%, Data: {dados['data']}")

    def mostra_relatorio_massa(self, dados_relatorio):
        print("---------- RELATORIO DE MASSA MAGRA ----------")
        for dados in dados_relatorio:
            print(f"Cliente: {dados['cliente_nome']}, Massa Magra: {dados['massa_magra']:.2f}%, Data: {dados['data']}")


    def seleciona_avaliacao(self):
        while True:
            codigo = input("Digite o CÓDIGO da avaliação: ").strip()
            if codigo:
                return codigo
            else:
                self.mostra_mensagem("O código não pode ser vazio.")

    def seleciona_tipo_de_relatorio(self):
        print("----Selecione o Tipo de Relatório----")
        print("1 - Por cliente")
        print("2 - Por nutricionista")
        print("0 - Sair")
    
        while True:
            try:
                opcao = int(input("Escolha uma opcao: "))
                return opcao
            except ValueError:
                self.mostra_mensagem("Opção inválida. Por favor, digite um número.")

    def selecionar_cliente_cpf(self):
        while True:
            cpf = input("Digite o CPF do cliente: ").strip()
            if cpf:
                return cpf
            else:
                self.mostrar_mensagem("O CPF não pode ser vazio.")

    def selecionar_nutricionista_cpf(self):
           while True:
            cpf = input("Digite o CPF do nutricionista: ").strip()
            if cpf:
                return cpf
            else:
                self.mostrar_mensagem("O CPF não pode ser vazio.")

    def mostra_mensagem(self, msg):
        print(msg)
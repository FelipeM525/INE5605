from model.nutricionista import Nutricionista

class TelaNutricionista:

    def mostrar_menu(self):
        print("1 - Cadastrar Nutricionista")
        print("2 - Mostrar Dados do Nutricionista")
        print("3 - Listar Nutricionistas")
        print("4 - Remover Nutricionista")
        print("0 - Sair")

        while True:
            try:
                opcao = int(input("Escolha uma opção: "))
                return opcao
            except ValueError:
                self.mostrar_mensagem("Opção inválida. Por favor, digite um número.")        
    
    def cadastrar_nutricionista(self):
        while True:
            nome = input("Nome: ").strip()
            if nome:
                break
            self.mostrar_mensagem("O nome não pode ser vazio.")

        while True:
            email = input("Email: ").strip()
            if "@" in email and "." in email:
                break
            self.mostrar_mensagem("Formato de e-mail inválido. Tente novamente.")

        while True:
            senha = input("Senha: ").strip()
            if senha:
                break
            self.mostrar_mensagem("A senha não pode ser vazia.")

        while True:
            cpf = input("CPF (apenas números): ").strip()
            if cpf.isdigit() and len(cpf) == 11:
                break
            self.mostrar_mensagem("CPF inválido. Deve conter 11 dígitos numéricos.")

        while True:
            crn = input("CRN: ").strip()
            if crn:
                break
            self.mostrar_mensagem("O CRN não pode ser vazio.")

        while True:
            clinica = input("Clínica: ").strip()
            if clinica:
                break
            self.mostrar_mensagem("O nome da clínica não pode ser vazio.")

        return Nutricionista(nome, email, senha, cpf, clinica, crn)

    def pegar_dados_nutricionista(self, nutricionista: Nutricionista):
        if nutricionista:
            print(f"Nome: {nutricionista.nome}")
            print(f"Email: {nutricionista.email}")
            print(f"CPF: {nutricionista.cpf}")
            print(f"CRN: {nutricionista.crn}")
            print(f"Clinica: {nutricionista.clinica}")

    def listar_nutricionistas(self, dados_nutricionistas):
        print("---------- LISTA DE NUTRICIONISTAS ----------")
        if not dados_nutricionistas:
            print("Nenhum nutricionista cadastrado.")
            return

        for nutri in dados_nutricionistas:
            print(f"Nome: {nutri['nome']}, CPF: {nutri['cpf']}")

    def mostrar_mensagem(self, msg: str):
        print(msg)

    def selecionar_nutricionista_cpf(self):
           while True:
            cpf = input("Digite o CPF do nutricionista: ").strip()
            if cpf:
                return cpf
            else:
                self.mostrar_mensagem("O CPF deve conter 11 dígitos numericos")
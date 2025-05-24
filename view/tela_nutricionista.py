from model.nutricionista import Nutricionista

class TelaNutricionista:

    def mostrar_menu(self):
        print("1 - Cadastrar Nutricionista")
        print("2 - Mostrar Dados do Nutricionista")
        print("3 - Listar Nutricionistas")
        print("4 - Remover Nutricionista")
        print("0 - Sair")
    
    def cadastrar_nutricionista(self):
        nome = input("Nome: ")
        email = input("Email: ")
        senha = input("Senha: ")
        cpf = input("CPF: ")
        crn = input("CRN: ")
        clinica = input("Clinica: ")

        return Nutricionista(nome, email, senha, cpf, crn, clinica)

    def mostrar_dados_do_nutricionista(self, nutricionista: Nutricionista):
        if nutricionista:
            print(f"Nome: {nutricionista.nome}")
            print(f"Email: {nutricionista.email}")
            print(f"CPF: {nutricionista.cpf}")
            print(f"CRN: {nutricionista.crn}")
            print(f"Clinica: {nutricionista.clinica}")

    def listar_nutricionistas(self, nutricionistas: list):
        if not nutricionistas:
            self.mostrar_mensagem("Nenhum nutricionista cadastrado")
            return

        for nutri in nutricionistas:
            print(f"Nome: {nutri.nome}, CRN: {nutri.crn}, CPF: {nutri.cpf}, Clinica: {nutri.clinica}")

    def mostrar_mensagem(self, msg: str):
        print(msg)

    def selecionar_nutricionista_cpf(self):
        return input("Digite o CPF do nutricionista: ")
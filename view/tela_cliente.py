from model.cliente import Cliente
from model.objetivo import Objetivo

class TelaCliente:

    def mostrar_menu(self):
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Remover cliente")
        print("4 - Mostrar Dados do Cliente")
        print("5 - Alterar Dados do Cliente")
        print("0 - Voltar")

        while True:
            try:
                opcao = int(input("Escolha uma opção: "))
                return opcao
            except ValueError:
                self.mostrar_mensagem("Opção inválida. Por favor, digite um número.")

    def selecionar_meta_objetivo(self) -> str | None:
        print("Escolha a Meta do Objetivo")
        metas = {
            "1": "Ganho de Peso",
            "2": "Perda de Peso",
            "3": "Melhorar Alimentação"
        }
        for key, value in metas.items():
            print(f"[{key}] - {value}")
        print("[0] - Nenhuma das opções / Cancelar")

        while True:
            escolha = input("Digite o número da meta desejada: ")
            if escolha == "0":
                return None
            if escolha in metas:
                return metas[escolha]
            else:
                self.mostrar_mensagem("Opção de meta inválida. Tente novamente.")

    def pegar_dados_cliente(self):
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
            try:
                idade = int(input("Idade: "))
                if idade > 0:
                    break
                self.mostrar_mensagem("A idade deve ser um número positivo.")
            except ValueError:
                self.mostrar_mensagem("Entrada inválida. Por favor, digite um número inteiro para a idade.")

        while True:
            genero = input("Gênero ('masculino' ou 'feminino'): ").lower().strip()
            if genero in ['masculino', 'feminino']:
                break
            self.mostrar_mensagem("Gênero inválido. Por favor, digite 'masculino' ou 'feminino'.")

        while True:
            try:
                peso = float(input("Peso (kg): "))
                if peso > 0:
                    break
                self.mostrar_mensagem("O peso deve ser um número positivo.")
            except ValueError:
                self.mostrar_mensagem("Entrada inválida. Por favor, digite um número para o peso (ex: 75.5).")

        while True:
            try:
                altura = float(input("Altura (m): "))
                if altura > 0:
                    break
                self.mostrar_mensagem("A altura deve ser um número positivo.")
            except ValueError:
                self.mostrar_mensagem("Entrada inválida. Por favor, digite um número para a altura (ex: 1.75).")

        dados_cliente = {
            "nome": nome, "email": email, "senha": senha, "cpf": cpf,
            "idade": idade, "genero": genero, "peso": peso, "altura": altura
        }

        meta_selecionada = self.selecionar_meta_objetivo()

        if not meta_selecionada:
            self.mostrar_mensagem("Nenhuma meta específica para o objetivo")
            dados_cliente["meta_objetivo"] = "Não definido"
            dados_cliente["qtd_objetivo"] = 0
            dados_cliente["tempo_objetivo"] = 0

        else:
            while True:
                try:
                    quantidade = int(input(f"Meta de kg: "))
                    if quantidade >= 0: # Permite 0 para "manter peso"
                        break
                    self.mostrar_mensagem("A meta de kg deve ser um número positivo ou zero.")
                except ValueError:
                    self.mostrar_mensagem("Entrada inválida. Por favor, digite um número inteiro.")

            while True:
                try:
                    tempo = int(input(f"Tempo para alcançar (em meses): "))
                    if tempo > 0:
                        break
                    self.mostrar_mensagem("O tempo deve ser um número positivo.")
                except ValueError:
                    self.mostrar_mensagem("Entrada inválida. Por favor, digite um número inteiro.")
            
            dados_cliente["meta_objetivo"] = meta_selecionada
            dados_cliente["qtd_objetivo"] = quantidade
            dados_cliente["tempo_objetivo"] = tempo
        
        return dados_cliente

    def listar_clientes(self, dados_clientes: list):
        if not dados_clientes:
            self.mostrar_mensagem("Nenhum cliente cadastrado")
            return

        for c in dados_clientes:
            print(f"Nome: {c['nome']}, CPF: {c['cpf']}, Idade: {c['idade']}")

    def mostrar_dados_do_cliente(self, dados_cliente: dict): # Recebe um dicionário
        if dados_cliente:
            print(f"Nome: {dados_cliente['nome']}")
            print(f"Idade: {dados_cliente['idade']}")
            print(f"Gênero: {dados_cliente['genero']}")
            print(f"Peso: {dados_cliente['peso']}")
            print(f"Altura: {dados_cliente['altura']}")
            print(f"IMC: {dados_cliente['imc']}")
            print(f"TMB: {dados_cliente['tmb']}")
            if dados_cliente.get('objetivo_meta'):
                print(f"Objetivo: {dados_cliente['objetivo_meta']} - {dados_cliente['objetivo_qtd']}kg em {dados_cliente['objetivo_tempo']} meses")
            else:
                print("Objetivo não definido")

    def selecionar_cliente_cpf(self):
        while True:
            cpf = input("Digite o CPF do cliente: ").strip()
            if cpf:
                return cpf
            else:
                self.mostrar_mensagem("O CPF não pode ser vazio.")

    def mostrar_mensagem(self, msg: str):
        print(msg)
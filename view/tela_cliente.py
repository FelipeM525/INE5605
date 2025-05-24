from model.cliente import Cliente
from model.objetivo import Objetivo

class TelaCliente:
    def mostrar_menu(self):
        print("1 - Cadastrar cliente")
        print("2 - Mostrar Dados do Cliente")
        print("3 - Listar clientes")
        print("4 - Sair")
        return int(input("Escolha uma opção"))
    
    def cadastrar_cliente(self):
        nome = input("Nome: ")
        email = input("Email: ")
        senha = input("Senha: ")
        cpf = input("CPF: ")
        idade = int(input("Idade: "))
        genero = input("Genero: ")
        peso = float(input("Peso: "))
        altura = float(input("Altura: "))
        meta = input("Meta: ")
        quantidade = int(input("Quantidade (kg): "))
        tempo = int(input("Tempo(meses): "))
        objetivo = Objetivo(meta, quantidade, tempo)
        
        return Cliente(nome, email, senha, cpf, idade, genero, peso, altura, objetivo)
    
    def mostrar_menu_alteracao(self):
        print("\n--- Qual campo deseja alterar? ---")
        print("1 - Nome")
        print("2 - Email")
        print("3 - Senha")
        print("4 - Idade")
        print("5 - Gênero")
        print("6 - Peso")
        print("7 - Altura")
        print("8 - Objetivo")
        print("0 - Concluir Alterações")
        return input("Escolha uma opção: ")

    def pegar_dados_valor_alteracao(self, campo:str):
        return input(f"Digite novo(a) {campo}")

    def selecionar_cliente_cpf(self):
        return input("Digite o CPF do cliente: ")
    
    def pegar_dados_novo_objetivo(self):
        print("Digite os novos dados do objetivo: ")
        meta  = input("Nova meta: ")
        quantidade = int(input("Novo peso(kg): "))
        tempo = int(input("Noo tempo(meses): "))
        return {"meta": meta, "quantidade": quantidade, "tempo": tempo}

    def mostrar_dados_do_cliente(self, cliente: Cliente):
        if cliente:
            print(f"Nome: {cliente.nome}")
            print(f"Idade: {cliente.idade}")
            print(f"Gênero: {cliente.genero}")
            print(f"Peso: {cliente.peso}")
            print(f"Altura: {cliente.altura}")
            print(f"IMC: {cliente.calcular_imc()}")
            print(f"TMB: {cliente.calcular_tmb()}")
            obj = cliente.objetivo
            print(f"Objetivo: {obj.meta} - {obj.quantidade}kg - {obj.tempo} meses")
        else:
            print("Cliente não encontrado")

    def mostrar_mensagem(self, msg: str):
        print(msg)
    
    

    def listar_clientes(self, clientes):
        for c in clientes:
            print(f"{c.nome} - CPF: {c.cpf}")
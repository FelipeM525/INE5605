from model.cliente import Cliente
from model.objetivo import Objetivo

class TelaCliente:
    def mostrar_menu(self):
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Mostrar Dados do Cliente")
        print("4 - Alterar Dados do Cliente")
        print("5 - Sair")
        return int(input("Escolha uma opção"))

    def pegar_dados_cliente(self):
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

        obj_cliente = Objetivo(meta, quantidade, tempo)

        return Cliente(nome, email, senha, cpf, idade, genero, peso, altura, obj_cliente)

    def listar_clientes(self, clientes: list):
        if not clientes:
            self.mostrar_mensagem("Nenhum cliente cadastrado")
            return

        for c in clientes:
            print(f"Nome: {c.nome}, CPF: {c.cpf}, Idade: {c.idade}")

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

    def selecionar_cliente_cpf(self):
        return input("Digite o CPF do cliente: ")

    def mostrar_mensagem(self, msg: str):
        print(msg)
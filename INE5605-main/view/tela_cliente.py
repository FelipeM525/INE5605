from model.cliente import Cliente
from model.objetivo import Objetivo
from controller.controlador_cliente import ControladorCliente
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
        cpf = input("CPF: ")
        email = input("Email: ")
        senha = input("Senha ")
        idade = int(input("Idade: "))
        genero = input("Genero: ")
        peso = int(input("Peso: "))
        altura = float(input("Altura: "))
        meta = input("Meta: ")
        quantidade = int(input("Quantidade (kg): "))
        tempo = int(input("Tempo(meses): "))
        objetivo = Objetivo(meta, quantidade, tempo)
        
        return Cliente(nome, cpf, email, senha, idade, genero, peso, altura, objetivo)
    
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

    def listar_clientes(self, clientes):
        for c in clientes:
            print(f"{c.nome} - CPF: {c.cpf}")

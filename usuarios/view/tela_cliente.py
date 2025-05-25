from usuarios.model.cliente import Cliente

from core.objetivo import Objetivo

class TelaCliente:

    def mostrar_menu(self):
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Remover cliente")
        print("4 - Mostrar Dados do Cliente")
        print("5 - Alterar Dados do Cliente")
        print("6 - Voltar")
        return int(input("Escolha uma opção"))

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
        nome = input("Nome: ")
        email = input("Email: ")
        senha = input("Senha: ")
        cpf = input("CPF: ")
        idade = int(input("Idade: "))
        genero = input("Genero: ")
        peso = float(input("Peso: "))
        altura = float(input("Altura: "))
        meta_selecionada = self.selecionar_meta_objetivo()

        if not meta_selecionada:
            self.mostrar_mensagem("Nenhuma meta específica para o objetivo")
            obj_cliente = Objetivo(meta="Não definido", quantidade=0, tempo=0)

        else:
            quantidade = int(input(f"Meta de kg: "))
            tempo = int(input(f"Tempo para alcançar: "))
            obj_cliente = Objetivo(meta_selecionada, quantidade, tempo)
        
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
            if cliente.objetivo:
                obj = cliente.objetivo
                print(f"Objetivo: {obj.meta} - {obj.quantidade}kg em {obj.tempo} meses")
            else:
                print("Objetivo não definido")

    def selecionar_cliente_cpf(self):
        return input("Digite o CPF do cliente: ")

    def mostrar_mensagem(self, msg: str):
        print(msg)
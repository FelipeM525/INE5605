import tkinter as tk
from tkinter import simpledialog, messagebox, Toplevel

class TelaClienteTk:
    def __init__(self, master, controlador_cliente):
        self.__master = master
        self.__controlador_cliente = controlador_cliente
        self.__master.title("Menu Cliente")
        self.__master.geometry("400x350")

        self.frame = tk.Frame(self.__master)
        self.frame.pack(pady=10, padx=10, fill="both", expand=True)

        tk.Label(self.frame, text="MENU CLIENTE", font=("Arial", 12, "bold")).pack(pady=10)

        tk.Button(self.frame, text="Cadastrar Cliente", command=self.__controlador_cliente.incluir_cliente).pack(fill="x", pady=5)
        tk.Button(self.frame, text="Listar Clientes", command=self.__controlador_cliente.listar_clientes).pack(fill="x", pady=5)
        tk.Button(self.frame, text="Remover Cliente", command=self.__controlador_cliente.remover_cliente).pack(fill="x", pady=5)
        tk.Button(self.frame, text="Mostrar Dados do Cliente", command=self.__controlador_cliente.mostrar_dados_cliente).pack(fill="x", pady=5)
        tk.Button(self.frame, text="Alterar Dados do Cliente", command=self.__controlador_cliente.alterar_cliente).pack(fill="x", pady=5)
        tk.Button(self.frame, text="Voltar", command=self.__controlador_cliente.retornar).pack(fill="x", pady=5)

    def pegar_dados_cliente(self, cliente_existente=None):
        dados = {}
        top = Toplevel(self.__master)
        top.geometry("300x400")

        if cliente_existente:
            top.title("Alterar Dados do Cliente")
        else:
            top.title("Cadastrar Novo Cliente")

        tk.Label(top, text="Nome:").pack()
        nome_entry = tk.Entry(top)
        nome_entry.pack()

        tk.Label(top, text="Email:").pack()
        email_entry = tk.Entry(top)
        email_entry.pack()

        senha_label_text = "Senha (deixe em branco para não alterar):" if cliente_existente else "Senha:"
        tk.Label(top, text=senha_label_text).pack()
        senha_entry = tk.Entry(top, show="*")
        senha_entry.pack()

        tk.Label(top, text="CPF (só números):").pack()
        cpf_entry = tk.Entry(top)
        cpf_entry.pack()

        tk.Label(top, text="Idade:").pack()
        idade_entry = tk.Entry(top)
        idade_entry.pack()

        tk.Label(top, text="Gênero (masculino/feminino):").pack()
        genero_entry = tk.Entry(top)
        genero_entry.pack()

        tk.Label(top, text="Peso (kg):").pack()
        peso_entry = tk.Entry(top)
        peso_entry.pack()

        tk.Label(top, text="Altura (m):").pack()
        altura_entry = tk.Entry(top)
        altura_entry.pack()

        if cliente_existente:
            nome_entry.insert(0, cliente_existente.nome)
            email_entry.insert(0, cliente_existente.email)
            cpf_entry.insert(0, cliente_existente.cpf)
            idade_entry.insert(0, str(cliente_existente.idade))
            genero_entry.insert(0, cliente_existente.genero)
            peso_entry.insert(0, str(cliente_existente.peso))
            altura_entry.insert(0, str(cliente_existente.altura))

        def on_submit():
            try:
                dados["nome"] = nome_entry.get()
                dados["email"] = email_entry.get()
                dados["senha"] = senha_entry.get()
                dados["cpf"] = cpf_entry.get()
                dados["idade"] = int(idade_entry.get())
                dados["genero"] = genero_entry.get()
                dados["peso"] = float(peso_entry.get().replace(',', '.'))
                dados["altura"] = float(altura_entry.get().replace(',', '.'))
                top.destroy()
            except ValueError:
                messagebox.showerror("Erro de Entrada", "Por favor, verifique se os valores numéricos estão corretos.", parent=top)

        tk.Button(top, text="Próximo", command=on_submit).pack(pady=10)
        top.transient(self.__master)
        top.grab_set()
        self.__master.wait_window(top)
        return dados

    def listar_clientes(self, dados_clientes):
        top = Toplevel(self.__master)
        top.title("Lista de Clientes")
        top.geometry("400x300")
        text = tk.Text(top, wrap="word")
        text.pack(pady=10, padx=10, fill="both", expand=True)

        if not dados_clientes:
            text.insert("1.0", "Nenhum cliente cadastrado.")
        else:
            for c in dados_clientes:
                text.insert(tk.END, f"Nome: {c['nome']}, CPF: {c['cpf']}, Idade: {c['idade']}\n")
        text.config(state="disabled")

    def selecionar_cliente_cpf(self):
        return simpledialog.askstring("Selecionar Cliente", "Digite o CPF do cliente:", parent=self.__master)

    def mostrar_dados_do_cliente(self, dados_cliente):
        if dados_cliente:
            info = (f"DADOS PESSOAIS\n"
                    f"--------------------------\n"
                    f"Nome: {dados_cliente['nome']}\n"
                    f"Idade: {dados_cliente['idade']}\n"
                    f"Gênero: {dados_cliente['genero']}\n"
                    f"Peso: {dados_cliente['peso']} kg\n"
                    f"Altura: {dados_cliente['altura']} m\n"
                    f"IMC: {dados_cliente['imc']:.2f}\n"
                    f"TMB: {dados_cliente['tmb']:.2f} kcal\n\n"
                    f"--------------------------\n"
                    f"OBJETIVO\n"
                    f"Meta: {dados_cliente['meta_objetivo']}\n"
                    f"Alvo: {dados_cliente['qtd_objetivo']} kg\n"
                    f"Prazo: {dados_cliente['tempo_objetivo']} meses")
            messagebox.showinfo("Dados do Cliente", info, parent=self.__master)
        else:
            self.mostrar_mensagem("Erro", "Cliente não encontrado.")

    def mostrar_mensagem(self, titulo, msg):
        messagebox.showinfo(titulo, msg, parent=self.__master)
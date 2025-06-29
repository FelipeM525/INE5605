import tkinter as tk
from tkinter import simpledialog, messagebox, Toplevel

class TelaNutricionistaTk:
    def __init__(self, master, controlador_nutricionista):
        self.__master = master
        self.__controlador_nutricionista = controlador_nutricionista
        self.__master.title("Menu Nutricionista")
        self.__master.geometry("300x250")

        self.frame = tk.Frame(self.__master)
        self.frame.pack(pady=10, padx=10, fill="both", expand=True)

        tk.Label(self.frame, text="MENU NUTRICIONISTA", font=("Arial", 12, "bold")).pack(pady=10)

        tk.Button(self.frame, text="Cadastrar Nutricionista", command=self.__controlador_nutricionista.incluir_nutricionista).pack(fill="x", pady=5)
        tk.Button(self.frame, text="Mostrar Dados do Nutricionista", command=self.__controlador_nutricionista.mostrar_dados_nutricionista).pack(fill="x", pady=5)
        tk.Button(self.frame, text="Listar Nutricionistas", command=self.__controlador_nutricionista.listar_nutricionistas).pack(fill="x", pady=5)
        tk.Button(self.frame, text="Remover Nutricionista", command=self.__controlador_nutricionista.remover_nutricionista).pack(fill="x", pady=5)
        tk.Button(self.frame, text="Voltar", command=self.__controlador_nutricionista.retornar).pack(fill="x", pady=5)

    def cadastrar_nutricionista(self):
        dados = {}
        top = Toplevel(self.__master)
        top.title("Dados do Nutricionista")
        top.geometry("300x300")

        tk.Label(top, text="Nome:").pack()
        nome_entry = tk.Entry(top)
        nome_entry.pack()

        tk.Label(top, text="Email:").pack()
        email_entry = tk.Entry(top)
        email_entry.pack()

        tk.Label(top, text="Senha:").pack()
        senha_entry = tk.Entry(top, show="*")
        senha_entry.pack()

        tk.Label(top, text="CPF (só números):").pack()
        cpf_entry = tk.Entry(top)
        cpf_entry.pack()

        tk.Label(top, text="CRN:").pack()
        crn_entry = tk.Entry(top)
        crn_entry.pack()

        tk.Label(top, text="Clínica:").pack()
        clinica_entry = tk.Entry(top)
        clinica_entry.pack()

        def on_submit():
            dados["nome"] = nome_entry.get()
            dados["email"] = email_entry.get()
            dados["senha"] = senha_entry.get()
            dados["cpf"] = cpf_entry.get()
            dados["crn"] = crn_entry.get()
            dados["clinica"] = clinica_entry.get()
            top.destroy()

        tk.Button(top, text="Salvar", command=on_submit).pack(pady=10)
        self.__master.wait_window(top)
        return dados

    def pegar_dados_nutricionista(self, nutricionista):
         if nutricionista:
            info = (f"Nome: {nutricionista.nome}\n"
                    f"Email: {nutricionista.email}\n"
                    f"CPF: {nutricionista.cpf}\n"
                    f"CRN: {nutricionista.crn}\n"
                    f"Clínica: {nutricionista.clinica}")
            messagebox.showinfo("Dados do Nutricionista", info, parent=self.__master)

    def listar_nutricionistas(self, dados_nutricionistas):
        top = Toplevel(self.__master)
        top.title("Lista de Nutricionistas")
        top.geometry("400x300")
        text = tk.Text(top, wrap="word")
        text.pack(pady=10, padx=10, fill="both", expand=True)

        if not dados_nutricionistas:
            text.insert("1.0", "Nenhum nutricionista cadastrado.")
        else:
            for nutri in dados_nutricionistas:
                text.insert(tk.END, f"Nome: {nutri['nome']}, CPF: {nutri['cpf']}\n")
        text.config(state="disabled")

    def mostrar_mensagem(self, titulo, msg):
        messagebox.showinfo(titulo, msg, parent=self.__master)

    def selecionar_nutricionista_cpf(self):
        return simpledialog.askstring("Selecionar Nutricionista", "Digite o CPF do nutricionista:", parent=self.__master)
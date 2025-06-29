import tkinter as tk
from tkinter import simpledialog, messagebox, Toplevel, Scrollbar


class TelaPlanoAlimentarTk:
    def __init__(self, master, controlador_plano):
        self.__master = master
        self.__controlador_plano = controlador_plano
        self.__master.title("Menu Plano Alimentar")
        self.__master.geometry("400x350")

        self.frame = tk.Frame(self.__master)
        self.frame.pack(pady=10, padx=10, fill="both", expand=True)

        tk.Label(self.frame, text="MENU PLANO ALIMENTAR", font=("Arial", 12, "bold")).pack(pady=10)

        tk.Button(self.frame, text="Incluir Plano", command=self.__controlador_plano.incluir_plano_alimentar).pack(
            fill="x", pady=5)
        tk.Button(self.frame, text="Listar Planos", command=self.__controlador_plano.listar_planos).pack(fill="x",
                                                                                                         pady=5)
        tk.Button(self.frame, text="Incluir Refeição no Plano",
                  command=self.__controlador_plano.inclui_refeicao_no_plano).pack(fill="x", pady=5)
        tk.Button(self.frame, text="Remover Refeição do Plano", command=self.__controlador_plano.remover_refeicao).pack(
            fill="x", pady=5)
        tk.Button(self.frame, text="Remover Plano", command=self.__controlador_plano.remover_plano).pack(fill="x",
                                                                                                         pady=5)
        tk.Button(self.frame, text="Voltar", command=self.__controlador_plano.retornar).pack(fill="x", pady=5)

    def pegar_dados_plano(self):
        top = Toplevel(self.__master)
        top.title("Dados do Plano Alimentar")
        top.geometry("300x200")
        dados = {}

        tk.Label(top, text="CPF do Cliente:").pack(padx=10, pady=5, anchor='w')
        cpf_cliente_entry = tk.Entry(top)
        cpf_cliente_entry.pack(padx=10, pady=5, fill='x')

        tk.Label(top, text="CPF do Nutricionista:").pack(padx=10, pady=5, anchor='w')
        cpf_nutri_entry = tk.Entry(top)
        cpf_nutri_entry.pack(padx=10, pady=5, fill='x')

        def on_submit():
            cpf_cliente = cpf_cliente_entry.get()
            cpf_nutri = cpf_nutri_entry.get()
            if not cpf_cliente or not cpf_nutri:
                messagebox.showerror("Erro", "Ambos os CPFs são obrigatórios.", parent=top)
                return
            dados["cpf_cliente"] = cpf_cliente
            dados["cpf_nutricionista"] = cpf_nutri
            top.destroy()

        tk.Button(top, text="Salvar", command=on_submit).pack(pady=20)
        self.__master.wait_window(top)
        return dados

    def mostra_plano(self, dados_planos):
        top = Toplevel(self.__master)
        top.title("Lista de Planos Alimentares")
        top.geometry("500x400")
        text = tk.Text(top, wrap="word")
        scroll = Scrollbar(top, command=text.yview)
        text.configure(yscrollcommand=scroll.set)
        text.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        scroll.pack(side="right", fill="y")

        if not dados_planos:
            text.insert("1.0", "Nenhum plano alimentar cadastrado.")
        else:
            for plano in dados_planos:
                refeicoes_str = "\n".join([f"- {cod}" for cod in plano['refeicoes']]) if plano[
                    'refeicoes'] else "- Nenhuma refeição."
                info = (f"Cliente: {plano['cliente_nome']} (CPF: {plano['codigo']})\n"
                        f"Nutricionista: {plano['nutricionista_nome']}\n"
                        f"Refeições:\n{refeicoes_str}\n"
                        f"------------------------------------\n")
                text.insert(tk.END, info)
        text.config(state="disabled")

    def seleciona_plano_por_cliente(self):
        return simpledialog.askstring("Selecionar Plano", "Digite o CPF do cliente:", parent=self.__master)

    def seleciona_refeicao_cod(self):
        return simpledialog.askstring("Selecionar Refeição", "Digite o código da refeição:", parent=self.__master)

    def mostra_mensagem(self, titulo, msg):
        messagebox.showinfo(titulo, msg, parent=self.__master)
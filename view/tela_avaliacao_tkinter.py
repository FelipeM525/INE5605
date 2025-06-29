import tkinter as tk
from tkinter import simpledialog, messagebox, Toplevel

class TelaAvaliacaoTk:
    def __init__(self, master, controlador_avaliacao):
        self.__master = master
        self.__controlador_avaliacao = controlador_avaliacao
        self.__master.title("Menu Avaliação")
        self.__master.geometry("300x300")

        self.frame = tk.Frame(self.__master)
        self.frame.pack(pady=10, padx=10, fill="both", expand=True)

        tk.Label(self.frame, text="MENU AVALIAÇÃO", font=("Arial", 12, "bold")).pack(pady=10)

        tk.Button(self.frame, text="Cadastrar Avaliação", command=self.__controlador_avaliacao.incluir_avaliacao).pack(fill="x", pady=5)
        tk.Button(self.frame, text="Listar Avaliações", command=self.__controlador_avaliacao.lista_avaliacao).pack(fill="x", pady=5)
        tk.Button(self.frame, text="Alterar Avaliação", command=self.__controlador_avaliacao.alterar_avaliacao).pack(fill="x", pady=5)
        tk.Button(self.frame, text="Excluir Avaliação", command=self.__controlador_avaliacao.remover_avaliacao).pack(fill="x", pady=5)
        tk.Button(self.frame, text="Relatório de Avaliações", command=self.__controlador_avaliacao.relatorio_de_avaliacoes).pack(fill="x", pady=5)
        tk.Button(self.frame, text="Voltar", command=self.__controlador_avaliacao.retornar).pack(fill="x", pady=5)

    def pega_dados_avaliacao(self):
        top = Toplevel(self.__master)
        top.title("Dados da Avaliação")
        top.geometry("300x350")

        dados = {}

        tk.Label(top, text="Código:").pack()
        codigo_entry = tk.Entry(top)
        codigo_entry.pack()

        tk.Label(top, text="CPF do Cliente (só números):").pack()
        cpf_cliente_entry = tk.Entry(top)
        cpf_cliente_entry.pack()

        tk.Label(top, text="CPF do Nutricionista (só números):").pack()
        cpf_nutri_entry = tk.Entry(top)
        cpf_nutri_entry.pack()

        tk.Label(top, text="Data (DD/MM/AAAA):").pack()
        data_entry = tk.Entry(top)
        data_entry.pack()

        tk.Label(top, text="IMC:").pack()
        imc_entry = tk.Entry(top)
        imc_entry.pack()

        tk.Label(top, text="TMB (Taxa Metabólica Basal):").pack()
        tmb_entry = tk.Entry(top)
        tmb_entry.pack()

        def on_submit():
            try:
                dados["codigo"] = codigo_entry.get()
                dados["cpf_cliente"] = cpf_cliente_entry.get()
                dados["cpf_nutricionista"] = cpf_nutri_entry.get()
                dados["data"] = data_entry.get()
                dados["imc"] = float(imc_entry.get().replace(',', '.'))
                dados["tmb"] = int(tmb_entry.get())
                top.destroy()
            except ValueError:
                messagebox.showerror("Erro de Entrada", "Por favor, verifique os valores numéricos.", parent=top)

        tk.Button(top, text="Salvar", command=on_submit).pack(pady=10)
        self.__master.wait_window(top)
        return dados

    def mostra_avaliacao(self, dados_avaliacoes):
        top = Toplevel(self.__master)
        top.title("Lista de Avaliações")
        top.geometry("500x400") # Aumentei a altura para caber os novos dados
        text = tk.Text(top, wrap="word")
        text.pack(pady=10, padx=10, fill="both", expand=True)

        if not dados_avaliacoes:
            text.insert("1.0", "Nenhuma avaliação cadastrada.")
        else:
            for dados in dados_avaliacoes:
                info = (f"Código: {dados['codigo']}\n"
                        f"Cliente: {dados['cliente_nome']}\n"
                        f"Nutricionista: {dados['nutricionista_nome']}\n"
                        f"Data: {dados['data']}\n"
                        f"IMC: {dados['imc']:.2f}\n"              # <-- ADICIONADO
                        f"TMB: {dados['tmb']} kcal\n"          # <-- ADICIONADO
                        f"------------------------------------\n")
                text.insert(tk.END, info)
        text.config(state="disabled")

    def seleciona_avaliacao(self):
        return simpledialog.askstring("Selecionar Avaliação", "Digite o CÓDIGO da avaliação:", parent=self.__master)

    def seleciona_tipo_de_relatorio(self):
        top = Toplevel(self.__master)
        top.title("Tipo de Relatório")
        top.geometry("250x150")

        result = tk.StringVar(value="")

        tk.Label(top, text="Selecione o tipo de relatório:").pack(pady=10)
        tk.Button(top, text="Por Cliente", command=lambda: [result.set("cliente"), top.destroy()]).pack(fill="x", padx=20, pady=5)
        tk.Button(top, text="Por Nutricionista", command=lambda: [result.set("nutricionista"), top.destroy()]).pack(fill="x", padx=20, pady=5)

        self.__master.wait_window(top)
        return result.get()

    def selecionar_cliente_cpf(self):
        return simpledialog.askstring("Selecionar Cliente", "Digite o CPF do cliente:", parent=self.__master)

    def selecionar_nutricionista_cpf(self):
        return simpledialog.askstring("Selecionar Nutricionista", "Digite o CPF do nutricionista:", parent=self.__master)

    def mostra_mensagem(self, titulo, msg):
        messagebox.showinfo(titulo, msg, parent=self.__master)
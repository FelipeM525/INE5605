import tkinter as tk
from tkinter import simpledialog, messagebox, Toplevel, Listbox, Scrollbar, ttk
from model.tipo_refeicao import TipoRefeicao


class TelaRefeicaoTk:
    def __init__(self, master, controlador_refeicao):
        self.__master = master
        self.__controlador_refeicao = controlador_refeicao
        self.__master.title("Menu Refeição")
        self.__master.geometry("400x350")

        self.frame = tk.Frame(self.__master)
        self.frame.pack(pady=10, padx=10, fill="both", expand=True)

        tk.Label(self.frame, text="MENU REFEIÇÃO", font=("Arial", 12, "bold")).pack(pady=10)

        tk.Button(self.frame, text="Criar Refeição", command=self.__controlador_refeicao.incluir_refeicao).pack(
            fill="x", pady=5)
        tk.Button(self.frame, text="Listar Refeições", command=self.__controlador_refeicao.listar_refeicoes).pack(
            fill="x", pady=5)
        tk.Button(self.frame, text="Adicionar Alimento à Refeição",
                  command=self.__controlador_refeicao.incluir_alimento_na_refeicao).pack(fill="x", pady=5)
        tk.Button(self.frame, text="Remover Alimento da Refeição",
                  command=self.__controlador_refeicao.excluir_alimento_da_refeicao).pack(fill="x", pady=5)
        tk.Button(self.frame, text="Excluir Refeição", command=self.__controlador_refeicao.remover_refeicao).pack(
            fill="x", pady=5)
        tk.Button(self.frame, text="Voltar", command=self.__controlador_refeicao.retornar).pack(fill="x", pady=5)

    def pega_dados_refeicao(self):
        top = Toplevel(self.__master)
        top.title("Dados da Refeição")
        top.geometry("300x200")
        dados = {}

        tk.Label(top, text="Código:").pack(padx=10, pady=5, anchor='w')
        codigo_entry = tk.Entry(top)
        codigo_entry.pack(padx=10, pady=5, fill='x')

        tk.Label(top, text="Tipo de Refeição:").pack(padx=10, pady=5, anchor='w')
        tipos = [tipo.value for tipo in TipoRefeicao]
        tipo_combobox = ttk.Combobox(top, values=tipos, state="readonly")
        tipo_combobox.pack(padx=10, pady=5, fill='x')
        if tipos:
            tipo_combobox.current(0)

        def on_submit():
            codigo = codigo_entry.get()
            tipo = tipo_combobox.get()
            if not codigo or not tipo:
                messagebox.showerror("Erro de Entrada", "Todos os campos são obrigatórios.", parent=top)
                return
            dados["codigo"] = codigo
            dados["tipo"] = tipo
            top.destroy()

        tk.Button(top, text="Salvar", command=on_submit).pack(pady=20)
        self.__master.wait_window(top)
        return dados

    def mostra_refeicao(self, dados_refeicoes):
        top = Toplevel(self.__master)
        top.title("Lista de Refeições")
        top.geometry("500x400")
        text = tk.Text(top, wrap="word")
        scroll = Scrollbar(top, command=text.yview)
        text.configure(yscrollcommand=scroll.set)
        text.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        scroll.pack(side="right", fill="y")

        if not dados_refeicoes:
            text.insert("1.0", "Nenhuma refeição cadastrada.")
        else:
            for refeicao in dados_refeicoes:
                alimentos_str = "\n".join([f"- {alimento}" for alimento in refeicao['alimentos']]) if refeicao[
                    'alimentos'] else "- Nenhum alimento."
                info = (f"Código: {refeicao['codigo']}\n"
                        f"Tipo: {refeicao['tipo']}\n"
                        f"Calorias Totais: {refeicao['calorias_total']:.2f} kcal\n"
                        f"Alimentos:\n{alimentos_str}\n"
                        f"------------------------------------\n")
                text.insert(tk.END, info)
        text.config(state="disabled")

    def seleciona_refeicao(self):
        return simpledialog.askstring("Selecionar Refeição", "Digite o código da refeição:", parent=self.__master)

    def seleciona_alimento(self):
        return simpledialog.askstring("Selecionar Alimento", "Digite o nome do alimento a ser adicionado/removido:",
                                      parent=self.__master)

    def mostra_mensagem(self, titulo, msg):
        messagebox.showinfo(titulo, msg, parent=self.__master)
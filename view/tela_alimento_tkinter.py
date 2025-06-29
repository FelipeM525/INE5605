import tkinter as tk
from tkinter import simpledialog, messagebox, Toplevel, Listbox, Scrollbar

class TelaAlimentoTk:
    def __init__(self, master, controlador_alimento):
        self.__master = master
        self.__controlador_alimento = controlador_alimento
        self.__master.title("Menu Alimento")
        # Aumentando a largura da janela de 300 para 400 pixels
        self.__master.geometry("400x300")

        self.frame = tk.Frame(self.__master)
        self.frame.pack(pady=10, padx=10, fill="both", expand=True)

        tk.Label(self.frame, text="MENU ALIMENTO", font=("Arial", 12, "bold")).pack(pady=10)

        tk.Button(self.frame, text="Incluir Alimento", command=self.__controlador_alimento.incluir_alimento).pack(fill="x", pady=5)
        tk.Button(self.frame, text="Listar Alimentos", command=self.__controlador_alimento.listar_alimento).pack(fill="x", pady=5)
        tk.Button(self.frame, text="Alterar Alimento", command=self.__controlador_alimento.alterar_alimento).pack(fill="x", pady=5)
        tk.Button(self.frame, text="Excluir Alimento", command=self.__controlador_alimento.excluir_alimento).pack(fill="x", pady=5)
        tk.Button(self.frame, text="Voltar", command=self.__controlador_alimento.retornar).pack(fill="x", pady=5)

    def pega_dados_alimento(self, alimento_existente=None):
        top = Toplevel(self.__master)
        top.title("Dados do Alimento")
        top.geometry("300x500")
        dados = {}

        tk.Label(top, text="Nome:").pack(padx=10, pady=5, anchor='w')
        nome_entry = tk.Entry(top)
        nome_entry.pack(padx=10, pady=5, fill='x')

        tk.Label(top, text="Calorias (kcal):").pack(padx=10, pady=5, anchor='w')
        calorias_entry = tk.Entry(top)
        calorias_entry.pack(padx=10, pady=5, fill='x')

        tk.Label(top, text="Carboidratos (g):").pack(padx=10, pady=5, anchor='w')
        carboidratos_entry = tk.Entry(top)
        carboidratos_entry.pack(padx=10, pady=5, fill='x')

        tk.Label(top, text="Proteínas (g):").pack(padx=10, pady=5, anchor='w')
        proteinas_entry = tk.Entry(top)
        proteinas_entry.pack(padx=10, pady=5, fill='x')

        tk.Label(top, text="Gorduras (g):").pack(padx=10, pady=5, anchor='w')
        gorduras_entry = tk.Entry(top)
        gorduras_entry.pack(padx=10, pady=5, fill='x')

        if alimento_existente:
            nome_entry.insert(0, alimento_existente.nome)
            calorias_entry.insert(0, str(alimento_existente.calorias))
            carboidratos_entry.insert(0, str(alimento_existente.carboidratos))
            proteinas_entry.insert(0, str(alimento_existente.proteinas))
            gorduras_entry.insert(0, str(alimento_existente.gorduras))
            if alimento_existente.nome:
                 nome_entry.config(state='readonly')


        def on_submit():
            try:
                dados["nome"] = nome_entry.get()
                dados["calorias"] = float(calorias_entry.get())
                dados["carboidratos"] = float(carboidratos_entry.get())
                dados["proteinas"] = float(proteinas_entry.get())
                dados["gorduras"] = float(gorduras_entry.get())
                top.destroy()
            except ValueError:
                messagebox.showerror("Erro de Entrada", "Por favor, insira valores numéricos válidos.", parent=top)

        tk.Button(top, text="Salvar", command=on_submit).pack(pady=20)
        self.__master.wait_window(top)
        return dados

    def mostra_alimento(self, dados_alimentos):
        top = Toplevel(self.__master)
        top.title("Lista de Alimentos")
        top.geometry("400x300")
        text = tk.Text(top, wrap="word")
        text.pack(pady=10, padx=10, fill="both", expand=True)

        if not dados_alimentos:
            text.insert("1.0", "Nenhum alimento cadastrado.")
        else:
            for alimento in dados_alimentos:
                info = (f"Nome: {alimento['nome']}\n"
                        f"Calorias: {alimento['calorias']:.2f} kcal\n"
                        f"Carboidratos: {alimento['carboidratos']:.2f}g\n"
                        f"Proteínas: {alimento['proteinas']:.2f}g\n"
                        f"Gorduras: {alimento['gorduras']:.2f}g\n"
                        f"------------------------------------\n")
                text.insert(tk.END, info)
        text.config(state="disabled")

    def seleciona_alimento(self):
        return simpledialog.askstring("Selecionar Alimento", "Digite o nome do alimento:", parent=self.__master)

    def mostra_mensagem(self, titulo, msg):
        messagebox.showinfo(titulo, msg, parent=self.__master)
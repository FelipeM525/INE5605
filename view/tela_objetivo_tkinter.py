import tkinter as tk
from tkinter import messagebox, Toplevel, ttk

class TelaObjetivoTk:
    def __init__(self, master, objetivo_existente=None):
        self.__master = master
        self.__master.title("Definir Objetivo do Cliente")
        self.__master.geometry("400x300")
        self.__dados_objetivo = {}

        self.frame = tk.Frame(self.__master)
        self.frame.pack(pady=10, padx=10, fill="both", expand=True)

        tk.Label(self.frame, text="DEFINIR OBJETIVO", font=("Arial", 12, "bold")).pack(pady=10)

        #Objetivo:
        tk.Label(self.frame, text="Meta:").pack(anchor='w')
        self.meta_options = ['Perda de gordura', 'Melhoria na Alimentação', 'Ganho de massa magra']
        self.meta_var = tk.StringVar(self.frame)
        meta_dropdown = ttk.Combobox(self.frame, textvariable=self.meta_var, values=self.meta_options, state="readonly")
        meta_dropdown.pack(fill="x", pady=2)

        #Quantidade:
        tk.Label(self.frame, text="Quantidade (em kg):").pack(anchor='w')
        self.qtd_entry = tk.Entry(self.frame)
        self.qtd_entry.pack(fill="x", pady=2)

        #Tempo:
        tk.Label(self.frame, text="Tempo (em meses):").pack(anchor='w')
        self.tempo_entry = tk.Entry(self.frame)
        self.tempo_entry.pack(fill="x", pady=2)

        if objetivo_existente:
            self.meta_var.set(objetivo_existente.get("meta_objetivo", self.meta_options[0]))
            self.qtd_entry.insert(0, str(objetivo_existente.get("qtd_objetivo", "")))
            self.tempo_entry.insert(0, str(objetivo_existente.get("tempo_objetivo", "")))
        else:
            self.meta_var.set(self.meta_options[0])

        tk.Button(self.frame, text="Salvar Objetivo", command=self.on_submit).pack(pady=15)


    def on_submit(self):
        try:
            meta = self.meta_var.get()
            qtd = float(self.qtd_entry.get().replace(',', '.'))
            tempo = int(self.tempo_entry.get())

            if not meta or qtd <= 0 or tempo <= 0:
                messagebox.showerror("Erro de Validação", "Todos os campos são obrigatórios e os valores devem ser positivos.", parent=self.__master)
                return

            self.__dados_objetivo = {
                "meta_objetivo": meta,
                "qtd_objetivo": qtd,
                "tempo_objetivo": tempo
            }
            self.__master.destroy()

        except (ValueError, TypeError):
            messagebox.showerror("Erro de Entrada", "Verifique se 'Quantidade' e 'Tempo' são números válidos.", parent=self.__master)

    def pegar_dados_objetivo(self):
        self.__master.transient(self.__master.master)
        self.__master.grab_set()
        self.__master.wait_window(self.__master)
        return self.__dados_objetivo
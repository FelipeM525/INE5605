import tkinter as tk
from tkinter import messagebox


class TelaSistemaTk:
    def __init__(self, master, controlador_sistema):
        self.__master = master
        self.__controlador_sistema = controlador_sistema
        self.__master.title("Sistema de Nutrição")
        self.__master.geometry("300x400")  # Aumentado para caber os botões
        self.frame = tk.Frame(self.__master)
        self.frame.pack(pady=10, padx=10, fill="both", expand=True)

        tk.Label(self.frame, text="Nutr-In-Sight", font=("Arial", 14, "bold")).pack(pady=10)

        tk.Button(self.frame, text="Menu Clientes", command=self.__controlador_sistema.chama_controlador_cliente).pack(
            fill="x", pady=5)
        tk.Button(self.frame, text="Menu Nutricionistas",
                  command=self.__controlador_sistema.chama_controlador_nutricionista).pack(fill="x", pady=5)
        tk.Button(self.frame, text="Menu Alimentos",
                  command=self.__controlador_sistema.chama_controlador_alimento).pack(fill="x", pady=5)
        tk.Button(self.frame, text="Menu Refeições",
                  command=self.__controlador_sistema.chama_controlador_refeicao).pack(fill="x", pady=5)
        tk.Button(self.frame, text="Menu Plano Alimentar",
                  command=self.__controlador_sistema.chama_controlador_plano_alimentar).pack(fill="x", pady=5)
        tk.Button(self.frame, text="Menu Avaliações",
                  command=self.__controlador_sistema.chama_controlador_avaliacao).pack(fill="x", pady=5)

        tk.Button(self.frame, text="Finalizar Sistema", command=self.__master.quit).pack(fill="x", pady=20)

    def mostra_mensagem(self, titulo, msg):
        messagebox.showinfo(titulo, msg)
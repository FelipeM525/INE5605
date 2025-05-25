class TelaSistema:
    def le_num_inteiro(self, mensagem= " ", ints_validos=None):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_int = int(valor_lido)
                if ints_validos and valor_int not in ints_validos:
                    raise ValueError
                return valor_int
            except ValueError:
                print("Valor incorreto!")
                if ints_validos:
                    print("As opções válidas são: ", ints_validos)
    
    def tela_opcoes(self):
        print("----SISTEMA PARA NUTRICIONISTAS")
        print("  1 - Menu Clientes")
        print("  2 - Menu Nutricionistas")
        print("  3 - Menu Alimentos")
        print("  4 - Menu Avaliações")
        print("  5 - Menu Refeições")
        print("  6 - Menu Plano Alimentar")
        print("  0 - Finalizar Sistema")

        opcao = self.le_num_inteiro("Digite a opção: ", [0, 1, 2, 3, 4, 5, 6])
        return opcao
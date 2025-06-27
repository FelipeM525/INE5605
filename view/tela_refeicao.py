from model.refeicao import Refeicao
from model.tipo_refeicao import TipoRefeicao


class TelaRefeicao:
    def mostrar_menu(self):
        print("---------- REFEIÇÕES ------------")
        print("Opcoes:")
        print("1 - Criar refeição")
        print("2 - Listar refeições")
        print("3 - Adicionar alimento à refeição")
        print("4 - Remover alimento da refeição")
        print("5 - Excluir refeição")
        print("0 - Sair")

        while True:
            try:
                opcao = int(input("Escolha uma opcao: "))
                return opcao
            except ValueError:
                self.mostra_mensagem("Opção inválida. Por favor, digite um número.")

    def pega_dados_refeicao(self):
        print("------- DADOS REFEIÇÃO -------")
        print("\nTipos de refeição disponíveis:")
        tipo_refeicao = self.mostra_menu_tipo_refeicao()

        while True:
            codigo = input("Digite um codigo para a refeição: ").strip()
            if codigo:
                break
            else:
                self.mostra_mensagem("O codigo da refeição não pode ser vazio.")

        return {
            "codigo": codigo,
            "tipo": tipo_refeicao,
        }

    def mostra_refeicao(self, dados_refeicoes):
        print("---------- LISTA DE REFEICOES ----------")
        if not dados_refeicoes:
            print("Nenhuma refeição para mostrar.")
            return

        for refeicao in dados_refeicoes:
            print(f"codigo da Refeição: {refeicao['codigp']}")
            print(f"Horário: {refeicao['horario']}")
            print(f"Tipo: {refeicao['tipo']}")
            print(f"Calorias Totais: {refeicao['calorias_total']:.2f} kcal")
            print("Alimentos:")
            if refeicao['alimentos']:
                for alimento in refeicao['alimentos']:
                    print(f"- {alimento}")
            else:
                print("- Nenhum alimento nesta refeição.")
            print("-" * 20)

    def seleciona_refeicao(self):
        while True:
            codigo = input("Digite o codigo (identificador) da refeicao: ").strip()
            if codigo:
                return codigo
            else:
                self.mostra_mensagem("O codigo da refeição não pode ser vazio.")

    def mostra_menu_tipo_refeicao(self):
        for i, tipo in enumerate(TipoRefeicao, 1):
            print(f"{i} - {tipo.value}")

        while True:
            try:
                opcao = int(input("\nEscolha o tipo de refeição: "))
                if 1 <= opcao <= len(TipoRefeicao):
                    tipo_refeicao = list(TipoRefeicao)[opcao - 1].value
                    break
                print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Por favor, digite um número válido.")
        return tipo_refeicao

    def mostra_mensagem(self, msg):
        print(msg)
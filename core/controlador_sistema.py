from core.tela_sistema import TelaSistema
from usuarios.controller.controlador_cliente import ControladorCliente
from usuarios.controller.controlador_nutricionista import ControladorNutricionista
from alimentos.controlador_alimento import ControladorAlimento
from avaliacoes.controlador_avaliacao import ControladorAvaliacao
from refeicoes.controlador_refeicao import ControladorRefeicao
from plano.controlador_plano_alimentar import ControladorPlanoAlimentar

from usuarios.model.cliente import Cliente
from usuarios.model.nutricionista import Nutricionista
from alimentos.alimento import Alimento
from core.objetivo import Objetivo
from refeicoes.refeicao import Refeicao
from refeicoes.tipo_refeicao import TipoRefeicao
from plano.plano_alimentar import PlanoAlimentar
from avaliacoes.avaliacao import Avaliacao


class ControladorSistema:

    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_cliente = ControladorCliente(self)
        self.__controlador_nutricionista = ControladorNutricionista(self)
        self.__controlador_avaliacao = ControladorAvaliacao(self, self.__controlador_cliente,
                                                            self.__controlador_nutricionista)
        self.__controlador_alimento = ControladorAlimento(self)
        self.__controlador_refeicao = ControladorRefeicao(self.__controlador_alimento, self)
        self.__controlador_plano_alimentar = ControladorPlanoAlimentar(self.__controlador_cliente,
                                                                       self.__controlador_nutricionista,
                                                                       self.__controlador_refeicao, self)

        self.gerar_dados()

    def gerar_dados(self):
        alimento1 = Alimento(nome="Maçã", calorias=52, carboidratos=14, gorduras=0.2, proteinas=0.3)
        alimento2 = Alimento(nome="Frango Grelhado", calorias=165, carboidratos=0, gorduras=3.6, proteinas=31)
        alimento3 = Alimento(nome="Arroz Integral Cozido", calorias=111, carboidratos=23, gorduras=0.9,
                             proteinas=2.6)  #
        alimento4 = Alimento(nome="Brócolis Cozido", calorias=35, carboidratos=7, gorduras=0.4, proteinas=2.4)
        alimento5 = Alimento(nome="Ovo Cozido", calorias=78, carboidratos=0.6, gorduras=5, proteinas=6)

        self.__controlador_alimento._ControladorAlimento__alimentos.extend(
            [alimento1, alimento2, alimento3, alimento4, alimento5])

        nutri1 = Nutricionista(nome="Dr. Carlos Silva", email="carlos.silva@nutri.com", senha="senha123",
                               cpf="11122233344", clinica="NutriVida", crn="CRN1-12345")
        nutri2 = Nutricionista(nome="Dra. Ana Souza", email="ana.souza@nutri.com", senha="senha456", cpf="55566677788",
                               clinica="BemEstar", crn="CRN2-54321")

        self.__controlador_nutricionista._ControladorNutricionista__nutricionistas.extend([nutri1, nutri2])

        objetivo_cliente1 = Objetivo(meta="Perda de Peso", quantidade=5, tempo=3)
        cliente1 = Cliente(nome="João Pereira", email="joao.pereira@email.com", senha="cliente1", cpf="12345678901",
                           idade=30, genero="masculino", peso=85.0, altura=1.75, objetivo=objetivo_cliente1)

        objetivo_cliente2 = Objetivo(meta="Ganho de Peso", quantidade=3, tempo=2)
        cliente2 = Cliente(nome="Maria Oliveira", email="maria.oliveira@email.com", senha="cliente2", cpf="09876543210",
                           idade=25, genero="feminino", peso=50.0, altura=1.60, objetivo=objetivo_cliente2)

        self.__controlador_cliente._ControladorCliente__clientes.extend([cliente1, cliente2])

        refeicao_cafe = Refeicao(nome="Café da Manhã Fit", alimentos=[alimento5, alimento1],
                                 tipo=TipoRefeicao.CAFE_MANHA.value)
        refeicao_almoco = Refeicao(nome="Almoço Balanceado", alimentos=[alimento2, alimento3, alimento4],
                                   tipo=TipoRefeicao.ALMOCO.value)

        self.__controlador_refeicao._ControladorRefeicao__refeicoes.extend([refeicao_cafe, refeicao_almoco])

        imc_cliente1 = cliente1.calcular_imc()
        tmb_cliente1 = cliente1.calcular_tmb()
        avaliacao1 = Avaliacao(nome= "avaliacao1", cliente=cliente1, nutricionista=nutri1, data="20/05/2024", imc=imc_cliente1,
                               taxa_mb=int(tmb_cliente1))

        self.__controlador_avaliacao._ControladorAvaliacao__avaliacoes.append(avaliacao1)
        nutri1.adicionar_avaliacao(avaliacao1)

        plano_joao = PlanoAlimentar(refeicoes=[refeicao_cafe, refeicao_almoco], nutricionista=nutri1,
                                    cliente=cliente1)
        cliente1.add_plano_alimentar(plano_joao)

        self.__controlador_plano_alimentar._ControladorPlanoAlimentar__planos.append(plano_joao)

    def inicializa_sistema(self):
        while True:
            opcao = self.__tela_sistema.tela_opcoes()

            if opcao == 1:
                self.__controlador_cliente.abre_tela()
            elif opcao == 2:
                self.__controlador_nutricionista.abre_tela()
            elif opcao == 3:
                self.__controlador_alimento.abre_tela()
            elif opcao == 4:
                self.__controlador_avaliacao.abre_tela()
            elif opcao == 5:
                self.__controlador_refeicao.abre_tela()
            elif opcao == 6:
                self.__controlador_plano_alimentar.abre_tela()
            elif opcao == 0:
                print("Encerrando o sistema")
                break
            else:
                print("Opção inválida. Selecione uma das opções disponíveis")

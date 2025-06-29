from tkinter import Toplevel
from view.tela_cliente_tkinter import TelaClienteTk
from view.tela_objetivo_tkinter import TelaObjetivoTk
from exception.cliente_inexistente_exception import ClienteInexistenteException
from model.cliente import Cliente
from exception.jahCadastradoException import JahCadastradoException
from exception.cadastroInexistenteException import CadastroInexistenteException
from dao.cliente_dao import ClienteDAO


class ControladorCliente:

    def __init__(self, controlador_sistema):
        self.__cliente_dao = ClienteDAO()
        self.__tela_cliente = None
        self.__controlador_sistema = controlador_sistema
        self.__top_level = None

    def abre_tela(self):
        self.__top_level = Toplevel(self.__controlador_sistema.root)
        self.__tela_cliente = TelaClienteTk(self.__top_level, self)
        self.__top_level.protocol("WM_DELETE_WINDOW", self.retornar)

    def buscar_cliente_por_cpf(self, cpf: str):
        return self.__cliente_dao.get(cpf)

    def incluir_cliente(self):
        dados_cliente = self.__tela_cliente.pegar_dados_cliente()
        if not dados_cliente.get("cpf"):
            self.__tela_cliente.mostrar_mensagem("Cancelado", "Operação de inclusão cancelada.")
            return

        try:
            if self.buscar_cliente_por_cpf(dados_cliente["cpf"]):
                raise JahCadastradoException()

            dados_objetivo = self.definir_objetivo_cliente()
            if not dados_objetivo:
                self.__tela_cliente.mostrar_mensagem("Cancelado",
                                                     "É necessário definir um objetivo para cadastrar o cliente.")
                return

            novo_cliente = Cliente(
                nome=dados_cliente["nome"],
                email=dados_cliente["email"],
                senha=dados_cliente["senha"],
                cpf=dados_cliente["cpf"],
                idade=dados_cliente["idade"],
                genero=dados_cliente["genero"],
                peso=dados_cliente["peso"],
                altura=dados_cliente["altura"],
                # Corrigido para usar dados_objetivo
                meta_objetivo=dados_objetivo["meta_objetivo"],
                qtd_objetivo=dados_objetivo["qtd_objetivo"],
                tempo_objetivo=dados_objetivo["tempo_objetivo"]
            )

            self.__cliente_dao.add(novo_cliente)
            self.__tela_cliente.mostrar_mensagem("Sucesso", "Cliente incluído com sucesso!")

        except JahCadastradoException:
            self.__tela_cliente.mostrar_mensagem("Erro", f"Cliente com CPF {dados_cliente['cpf']} já existe!")
        except Exception as e:
            self.__tela_cliente.mostrar_mensagem("Erro", f"Ocorreu um erro inesperado: {e}")

    def definir_objetivo_cliente(self, objetivo_existente=None):
        top_objetivo = Toplevel(self.__top_level)
        tela_objetivo = TelaObjetivoTk(top_objetivo, objetivo_existente=objetivo_existente)
        dados = tela_objetivo.pegar_dados_objetivo()
        return dados

    def remover_cliente(self):
        cpf = self.__tela_cliente.selecionar_cliente_cpf()
        if not cpf:
            return

        cliente = self.buscar_cliente_por_cpf(cpf)

        try:
            if cliente:
                self.__cliente_dao.remove(cpf)
                self.__tela_cliente.mostrar_mensagem("Sucesso", f"Cliente com CPF {cpf} removido com sucesso!")
            else:
                raise CadastroInexistenteException()
        except CadastroInexistenteException:
            self.__tela_cliente.mostrar_mensagem("Erro", f"Cliente com CPF {cpf} não existe!")

    def listar_clientes(self):
        clientes = self.__cliente_dao.get_all()

        if not clientes:
            self.__tela_cliente.mostrar_mensagem("Info", "Não há clientes cadastrados.")
            return

        dados_clientes = []
        for cliente in clientes:
            dados_clientes.append({
                "nome": cliente.nome,
                "cpf": cliente.cpf,
                "idade": cliente.idade
            })

        self.__tela_cliente.listar_clientes(dados_clientes)

    def alterar_cliente(self):
        cpf_antigo = self.__tela_cliente.selecionar_cliente_cpf()
        if not cpf_antigo: return

        cliente = self.buscar_cliente_por_cpf(cpf_antigo)

        try:
            if cliente:
                dados_novos = self.__tela_cliente.pegar_dados_cliente(cliente_existente=cliente)
                if not dados_novos.get("cpf"):
                    self.__tela_cliente.mostrar_mensagem("Cancelado", "Alteração cancelada.")
                    return

                objetivo_existente = {
                    "meta_objetivo": cliente.meta_objetivo,
                    "qtd_objetivo": cliente.qtd_objetivo,
                    "tempo_objetivo": cliente.tempo_objetivo
                }
                dados_objetivo_novos = self.definir_objetivo_cliente(objetivo_existente=objetivo_existente)
                if not dados_objetivo_novos:
                    self.__tela_cliente.mostrar_mensagem("Cancelado",
                                                         "A alteração do objetivo é necessária para continuar.")
                    return

                if cpf_antigo != dados_novos["cpf"] and self.buscar_cliente_por_cpf(dados_novos["cpf"]):
                    self.__tela_cliente.mostrar_mensagem("Erro",
                                                         f"Já existe um cliente com o CPF {dados_novos['cpf']}.")
                    return

                cliente.nome = dados_novos["nome"]
                cliente.email = dados_novos["email"]
                if dados_novos["senha"]:
                    cliente.senha = dados_novos["senha"]
                cliente.cpf = dados_novos["cpf"]
                cliente.idade = dados_novos["idade"]
                cliente.genero = dados_novos["genero"]
                cliente.peso = dados_novos["peso"]
                cliente.altura = dados_novos["altura"]
                cliente.meta_objetivo = dados_objetivo_novos["meta_objetivo"]
                cliente.qtd_objetivo = dados_objetivo_novos["qtd_objetivo"]
                cliente.tempo_objetivo = dados_objetivo_novos["tempo_objetivo"]

                self.__cliente_dao.update(cliente)
                self.__tela_cliente.mostrar_mensagem("Sucesso", "Cliente alterado com sucesso!")

            else:
                raise CadastroInexistenteException()
        except CadastroInexistenteException:
            self.__tela_cliente.mostrar_mensagem("Erro", f"Cliente com CPF {cpf_antigo} não existe!")
        except Exception as e:
            self.__tela_cliente.mostrar_mensagem("Erro", f"Ocorreu um erro inesperado: {e}")

    def mostrar_dados_cliente(self):
        cpf = self.__tela_cliente.selecionar_cliente_cpf()
        if not cpf: return
        cliente = self.buscar_cliente_por_cpf(cpf)
        try:
            if cliente:
                dados_cliente = {
                    "nome": cliente.nome,
                    "idade": cliente.idade,
                    "genero": cliente.genero,
                    "peso": cliente.peso,
                    "altura": cliente.altura,
                    "imc": cliente.calcular_imc(),
                    "tmb": cliente.calcular_tmb(),
                    "meta_objetivo": cliente.meta_objetivo,
                    "qtd_objetivo": cliente.qtd_objetivo,
                    "tempo_objetivo": cliente.tempo_objetivo,
                }
                self.__tela_cliente.mostrar_dados_do_cliente(dados_cliente)
            else:
                raise CadastroInexistenteException()
        except CadastroInexistenteException:
            self.__tela_cliente.mostrar_mensagem("Erro", f"Cliente com CPF {cpf} não existe!")

    def retornar(self):
        self.__top_level.destroy()
        self.__controlador_sistema.reabre_tela_principal()
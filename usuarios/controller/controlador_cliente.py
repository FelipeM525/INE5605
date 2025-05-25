from core.controlador_sistema import ControladorSistema
from exception.cliente_inexistente_exception import ClienteInexistenteException
from usuarios.model.cliente import Cliente
from exception.jahCadastradoException import JahCadastradoException
from exception.cadastroInexistenteException import CadastroInexistenteException
from usuarios.view.tela_cliente import TelaCliente

class ControladorCliente:

    def __init__(self, controlador_sistema: ControladorSistema):
        self.__clientes = []
        self.__tela_cliente = TelaCliente()
        self.__controlador_sistema = controlador_sistema

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_cliente,
            2: self.listar_clientes,
            3: self.remover_cliente,
            4: self.mostrar_dados_cliente,
            5: self.alterar_cliente,
            6: self.retornar
        }

        while True:
            opcao = self.__tela_cliente.mostrar_menu()

            if opcao == 6:
                self.retornar()
                break

            funcao_escolhida = lista_opcoes.get(opcao)

            if funcao_escolhida:
                funcao_escolhida()
            else:
                self.__tela_cliente.mostrar_mensagem("Opcao invalida!")

    def buscar_cliente_por_cpf(self, cpf: str):
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                return cliente
            
        return None

    def incluir_cliente(self):
        novo_cliente = self.__tela_cliente.pegar_dados_cliente()

        if not isinstance(novo_cliente, Cliente):
            raise ValueError("Valores inválidos")
        try:
            if self.buscar_cliente_por_cpf(novo_cliente.cpf):
                raise JahCadastradoException()

            else:
                self.__clientes.append(novo_cliente)
                self.__tela_cliente.mostrar_mensagem("Cliente incluido com sucesso!")

        except JahCadastradoException:
            self.__tela_cliente.mostrar_mensagem(f"Cliente com cpf {novo_cliente.cpf} ja existe!")

    def remover_cliente(self):
        cpf = self.__tela_cliente.selecionar_cliente_cpf()
        cliente = self.buscar_cliente_por_cpf(cpf)

        try:
            if cliente:
                self.__clientes.remove(cliente)
                self.__tela_cliente.mostrar_mensagem(f"Cliente com cpf {cpf} removido com sucesso!")
            else:
                raise CadastroInexistenteException()
        except CadastroInexistenteException:
            self.__tela_cliente.mostrar_mensagem(f"Cliente com cpf {cpf} nao existe!")
    
    def listar_clientes(self):
        lista_de_clientes = self.__clientes

        if len(lista_de_clientes) == 0:
            self.__tela_cliente.mostrar_mensagem("Nao ha clientes cadastrados!")
        else:
            self.__tela_cliente.listar_clientes(lista_de_clientes)

    def alterar_cliente(self):
        cpf = self.__tela_cliente.selecionar_cliente_cpf()
        cliente = self.buscar_cliente_por_cpf(cpf)

        try:
            if cliente:
                self.__tela_cliente.mostrar_mensagem("Digite os novos dados para o cliente")

                cliente_com_novos_dados = self.__tela_cliente.pegar_dados_cliente()

                cliente.nome = cliente_com_novos_dados.nome
                cliente.email = cliente_com_novos_dados.email
                cliente.senha = cliente_com_novos_dados.senha
                cliente.idade = cliente_com_novos_dados.idade
                cliente.genero = cliente_com_novos_dados.genero
                cliente.peso = cliente_com_novos_dados.peso
                cliente.altura = cliente_com_novos_dados.altura

                cliente.objetivo = cliente_com_novos_dados.objetivo

                self.__tela_cliente.mostrar_mensagem("Cliente alterado com sucesso!")
                self.__tela_cliente.mostrar_dados_do_cliente(cliente)

            else:
                raise CadastroInexistenteException()
        except CadastroInexistenteException:
            self.__tela_cliente.mostrar_mensagem(f"Cliente com cpf {cpf} nao existe!")

    def atualizar_cliente(self, cliente_att: Cliente):

        try:
            for cliente in self.__clientes:
                if cliente_att.cpf == cliente.cpf:
                    self.__clientes.remove(cliente)
                    self.__clientes.append(cliente_att)
                    return self.__tela_cliente.mostrar_mensagem("Cliente atualizado com sucesso!")
            raise ClienteInexistenteException
        except ClienteInexistenteException:
            return self.__tela_cliente.mostrar_mensagem("Cliente inexistente!")

    def retornar(self):
        pass
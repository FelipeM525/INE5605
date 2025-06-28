from exception.cliente_inexistente_exception import ClienteInexistenteException
from model.cliente import Cliente
from exception.jahCadastradoException import JahCadastradoException
from exception.cadastroInexistenteException import CadastroInexistenteException
from view.tela_cliente import TelaCliente

class ControladorCliente:

    def __init__(self, controlador_sistema):
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
            0: self.retornar
        }

        while True:
            opcao = self.__tela_cliente.mostrar_menu()

            if opcao == 0:
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
        dados_cliente = self.__tela_cliente.pegar_dados_cliente()

        try:
            if self.buscar_cliente_por_cpf(dados_cliente["cpf"]):
                raise JahCadastradoException()

            else:
                novo_cliente = Cliente(
                    nome=dados_cliente["nome"],
                    email=dados_cliente["email"],
                    senha=dados_cliente["senha"],
                    cpf=dados_cliente["cpf"],
                    idade=dados_cliente["idade"],
                    genero=dados_cliente["genero"],
                    peso=dados_cliente["peso"],
                    altura=dados_cliente["altura"],
                    meta_objetivo=dados_cliente["meta_objetivo"],
                    qtd_objetivo=dados_cliente["qtd_objetivo"],
                    tempo_objetivo=dados_cliente["tempo_objetivo"]
                )
                self.__clientes.append(novo_cliente)
                self.__tela_cliente.mostrar_mensagem("Cliente incluido com sucesso!")

        except JahCadastradoException:
            self.__tela_cliente.mostrar_mensagem(f"Cliente com cpf {dados_cliente['cpf']} ja existe!")

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
        if not self.__clientes:
            self.__tela_cliente.mostrar_mensagem("Nao ha clientes cadastrados!")
        else:
            dados_clientes = []
            for cliente in self.__clientes:
                dados_clientes.append({
                    "nome": cliente.codigo,
                    "cpf": cliente.cpf,
                    "idade": cliente.idade
                })
            self.__tela_cliente.listar_clientes(dados_clientes)

    def alterar_cliente(self):
        cpf = self.__tela_cliente.selecionar_cliente_cpf()
        cliente = self.buscar_cliente_por_cpf(cpf)

        try:
            if cliente:
                self.__tela_cliente.mostrar_mensagem("Digite os novos dados para o cliente")

                dados_novos = self.__tela_cliente.pegar_dados_cliente()

                cliente.nome = dados_novos["nome"]
                cliente.email = dados_novos["email"]
                cliente.senha = dados_novos["senha"]
                cliente.idade = dados_novos["idade"]
                cliente.genero = dados_novos["genero"]
                cliente.peso = dados_novos["peso"]
                cliente.altura = dados_novos["altura"]

                novos_dados_do_objetivo = {
                    "meta": dados_novos["meta_objetivo"],
                    "quantidade": dados_novos["qtd_objetivo"],
                    "tempo": dados_novos["tempo_objetivo"]
                }

                cliente.objetivo = novos_dados_do_objetivo
                
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

    def mostrar_dados_cliente(self):
        cpf = self.__tela_cliente.selecionar_cliente_cpf()
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
                    "objetivo_meta": cliente.objetivo.meta,
                    "objetivo_qtd": cliente.objetivo.quantidade,
                    "objetivo_tempo": cliente.objetivo.tempo
                }
                self.__tela_cliente.mostrar_dados_do_cliente(dados_cliente)
            else:
                raise CadastroInexistenteException()
        except CadastroInexistenteException:
            self.__tela_cliente.mostrar_mensagem(f"Cliente com cpf {cpf} nao existe!")

    def retornar(self):
        pass
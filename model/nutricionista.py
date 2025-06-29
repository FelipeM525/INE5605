from model.usuario import Usuario


class Nutricionista(Usuario):
    def __init__(self, nome: str, email: str, senha: str, cpf: str, crn: str, clinica: str):
        super().__init__(nome, email, senha, cpf)
        if isinstance(crn, str):
            self.__crn = crn
        if isinstance(clinica, str):
            self.__clinica = clinica
        self.__avaliacoes = []

    @property
    def crn(self):
        return self.__crn

    @crn.setter
    def crn(self, crn: str):
        if isinstance(crn, str):
            self.__crn = crn

    @property
    def clinica(self):
        return self.__clinica

    @clinica.setter
    def clinica(self, clinica: str):
        if isinstance(clinica, str):
            self.__clinica = clinica

    def adicionar_avaliacao(self, avaliacao):
        from model.avaliacao import Avaliacao

        if isinstance(avaliacao, Avaliacao):
            self.__avaliacoes.append(avaliacao)

    def cadastrar(self):
        print(f"Nutricionista {self.nome} sendo instanciado/cadastrado.")
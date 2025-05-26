from usuarios.model.usuario import Usuario


class Nutricionista(Usuario):
    def __init__(self, nome: str, email: str, senha: str, cpf: str, clinica: str, crn: str):
        super().__init__(nome, email, senha, cpf)
        self.__clinica = clinica
        self.__crn = crn
        self.__avaliacoes = []

    @property
    def clinica(self):
        return self.__clinica

    @clinica.setter
    def clinica(self, clinica: str):
        self.__clinica = clinica

    @property
    def crn(self):
        return self.__crn

    @crn.setter
    def crn(self, crn):
        self.__crn = crn

    @property
    def avaliacoes(self):
        return self.__avaliacoes

    def adicionar_avaliacao(self, avaliacao):
        from avaliacoes.avaliacao import Avaliacao

        if isinstance(avaliacao, Avaliacao):
            self.__avaliacoes.append(avaliacao)

    def cadastrar(self):
        print(f"Nutricionista {self.nome} cadastrado com sucesso.")

    def __str__(self):
        return f"{self.nome} (CRN: {self.crn})"
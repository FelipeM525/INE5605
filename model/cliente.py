from model.usuario import Usuario

class Cliente(Usuario):
    def __init__(self, nome: str, email: str, senha: str, cpf: str, idade: int, genero: str,
                 peso: float, altura: float, meta_objetivo: str, qtd_objetivo: float, tempo_objetivo: int,
                 plano_alimentar = None):
        super().__init__(nome, email, senha, cpf)
        if isinstance(idade, int): self.__idade = idade
        if isinstance(genero, str): self.__genero = genero
        if isinstance(peso, (float, int)): self.__peso = float(peso)
        if isinstance(altura, (float, int)): self.__altura = float(altura)
        if isinstance(meta_objetivo, str): self.__meta_objetivo = meta_objetivo
        if isinstance(qtd_objetivo, (float, int)): self.__qtd_objetivo = float(qtd_objetivo)
        if isinstance(tempo_objetivo, int): self.__tempo_objetivo = tempo_objetivo
        self.__plano_alimentar = plano_alimentar

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade: int):
        self.__idade = idade

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, peso: float):
        self.__peso = peso

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura: float):
        self.__altura = altura

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, genero: str):
        self.__genero = genero

    @property
    def meta_objetivo(self):
        return self.__meta_objetivo

    @meta_objetivo.setter
    def meta_objetivo(self, meta_objetivo: str):
        self.__meta_objetivo = meta_objetivo

    @property
    def qtd_objetivo(self):
        return self.__qtd_objetivo

    @qtd_objetivo.setter
    def qtd_objetivo(self, qtd_objetivo: float):
        self.__qtd_objetivo = float(qtd_objetivo)

    @property
    def tempo_objetivo(self):
        return self.__tempo_objetivo

    @tempo_objetivo.setter
    def tempo_objetivo(self, tempo_objetivo: int):
        self.__tempo_objetivo = tempo_objetivo

    @property
    def plano_alimentar(self):
        return self.__plano_alimentar

    @plano_alimentar.setter
    def plano_alimentar(self, plano_alimentar):
        from model.plano_alimentar import PlanoAlimentar
        if isinstance(plano_alimentar, PlanoAlimentar) or plano_alimentar is None:
            self.__plano_alimentar = plano_alimentar

    def add_plano_alimentar(self, plano_alimentar):
        from model.plano_alimentar import PlanoAlimentar
        if isinstance(plano_alimentar, PlanoAlimentar):
            self.__plano_alimentar = plano_alimentar

    def calcular_imc(self):
        if self.altura <= 0: return 0
        return self.peso / (self.altura ** 2)

    def calcular_tmb(self):
        if self.genero.lower() == 'masculino':
            return 88.362 + (13.397 * self.peso) + (4.799 * self.altura * 100) - (5.677 * self.idade)
        elif self.genero.lower() == 'feminino':
            return 447.593 + (9.247 * self.peso) + (3.098 * self.altura * 100) - (4.330 * self.idade)
        return 0

    def cadastrar(self):
        print(f"Cliente {self.nome} sendo instanciado/cadastrado.")
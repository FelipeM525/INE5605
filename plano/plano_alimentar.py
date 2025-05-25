from refeicoes.refeicao import Refeicao

class PlanoAlimentar:
    def __init__(self, refeicoes: list[Refeicao], nutricionista, cliente):
        self.__refeicoes = refeicoes
        self.__nutricionista = nutricionista
        self.__cliente = cliente
    
    @property
    def refeicoes(self):
        return self.__refeicoes
    
    @property
    def nutricionista(self):
        return self.__nutricionista

    @nutricionista.setter
    def nutricionista(self, nutricionista):
        from usuarios.model.nutricionista import Nutricionista

        if isinstance(nutricionista, Nutricionista):
            self.__nutricionista = nutricionista
        
    @property
    def cliente(self):
        return self.__cliente
    
    @cliente.setter
    def cliente(self, cliente):
        from usuarios.model.cliente import Cliente
        if isinstance(cliente, Cliente):
            self.__cliente = cliente

    def adicionar_refeicao(self, refeicao: Refeicao):
        if isinstance(refeicao, Refeicao):
            self.__refeicoes.append(refeicao)

    def __str__(self):
        refeicoes_str = "\n".join([str(refeicao) for refeicao in self.__refeicoes])
        return (
            f"Plano Alimentar:\n"
            f"Cliente: {self.__cliente}\n"
            f"Nutricionista: {self.__nutricionista}\n"
            f"Refeições:\n{refeicoes_str}"
        )
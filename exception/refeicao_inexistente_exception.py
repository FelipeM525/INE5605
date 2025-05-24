class RefeicaoInexistenteException(Exception):
    def __init__(self):
        super().__init__("Refeicao Inexistente")
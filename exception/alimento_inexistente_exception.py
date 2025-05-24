class AlimentoInexistenteException(Exception):
    def __init__(self):
        super().__init__("Alimento Inexistente")
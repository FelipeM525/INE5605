class PlanoInexistenteException(Exception):
    def __init__(self):
        super().__init__("Plano inexistente")
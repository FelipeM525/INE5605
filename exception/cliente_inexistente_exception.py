class ClienteInexistenteException(Exception):
    def __init__(self):
        super().__init__("Cliente Inexistente")
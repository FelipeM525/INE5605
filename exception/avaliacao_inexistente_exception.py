class AvaliacaoInexistenteException(Exception):
    def __init__(self):
        super().__init__("Avaliacao inexistente!")
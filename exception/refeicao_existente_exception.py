class RefeicaoExistenteException(Exception):
    def __init__(self):
        super().__init__("Refeicao com esse nome Ja existe!")
class PlanoJaCadastradoException(Exception):
    def __init__(self):
        super().__init__("Plano Alimentar inexsitente")
from model.nutricionista import Nutricionista
from exception.jahCadastradoException import JahCadastradoException

class ControladorNutricionista:
    def __init__(self):
        self.__nutricionistas = []
    
    def buscar_cliente_por_cpf(self, cpf: str):
        for nutricionista in self.__nutricionistas:
            if nutricionista.cpf == cpf:
                return nutricionista
        
        return None

    def incluir_nutricionista(self):
        novo_nutricionista = self.tela_nutricionista.cadastrar_nutricionista()

        if not isinstance(novo_nutricionista, Nutricionista):
            raise ValueError("Valores inválidos")
        
        if self.buscar_nutricionista_por_cpf(novo_nutricionista.cpf):
            raise JahCadastradoException()
        
        else:
            self.__nutricionistas.append(novo_nutricionista)
            
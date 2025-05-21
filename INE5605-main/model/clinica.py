from model.nutricionista import Nutricionista
from exception.cadastroInexistenteException import CadastroInexistenteException
from exception.jahCadastradoException import JahCadastradoException

class Clinica:
    def __init__(self, nome: str, email: str, cnpj: str):
        self.__nome = nome
        self.__email = email
        self.__cnpj = cnpj
        self.__nutricionistas = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome 

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email
    
    @property
    def cnpj(self):
        return self.__cnpj
    
    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj

    @property
    def nutricionistas(self):
        return self.__nutricionistas

    def cadastrar_nutricionista(self, nutricionista: Nutricionista):
        if not isinstance(nutricionista, Nutricionista):
            raise TypeError()
        
        if nutricionista in self.__nutricionistas:
            raise JahCadastradoException()
        
        self.__nutricionistas.append(nutricionista)
        print("Cadastro efetuado")

    def remover_nutricionista(self, nutricionista: Nutricionista):
        if not isinstance(nutricionista, Nutricionista) or nutricionista not in self.__nutricionistas:
            raise CadastroInexistenteException()

        self.__nutricionistas.remove(nutricionista)
        print("Nutricionista removido")
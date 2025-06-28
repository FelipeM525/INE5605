from dao.dao import DAO
from model.cliente import Cliente

class ClienteDAO(DAO):
    def __init__(self):
        super().__init__('clientes.pkl')

    def add(self, cliente: Cliente):
        if cliente is not None and isinstance(cliente, Cliente) and isinstance(cliente.cpf, str):
            super().add(cliente.cpf, cliente)

    def update(self, cliente: Cliente):
        if cliente is not None and isinstance(cliente, Cliente) and isinstance(cliente.cpf, str):
            super().update(cliente.cpf, cliente)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
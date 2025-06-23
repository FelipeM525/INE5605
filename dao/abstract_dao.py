import pickle
from abc import ABC, abstractmethod

class DAO(ABC):
    @abstractmethod
    def __init__(self, datasource=''):
        self.__datasource = datasource
        self.__cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        with open(self.__datasource, 'wb') as f:
            pickle.dump(self.__cache, f)

    def __load(self):
        with open(self.__datasource, 'rb') as f:
            self.__cache = pickle.load(f)

    def add(self, key, obj):
        self.__cache[key] = obj
        self.__dump()

    def get(self, key):
        return self.__cache.get(key)

    def remove(self, key):
        if key in self.__cache:
            del self.__cache[key]
            self.__dump()

    def get_all(self):
        return list(self.__cache.values())
"""
Autor: Lucas de Lima Bica
Exercicio 18 Tema 3
"""


class Pessoa:
    def __init__(self, nome, morada, telefone):
        self.__nome = nome
        self.__morada = morada
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def morada(self):
        return self.__morada

    @morada.setter
    def morada(self, morada):
        self.__morada = morada

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @classmethod  # Instancia a seguinte pessoa:
    def cria_anonimo(cls):
        return cls("John Doe", "Unknown", "Unknown")

    def __str__(self) -> str:
        return f"Nome: {self.nome}\nMorada: {self.morada}\nTelemóvel: {self.telefone}"

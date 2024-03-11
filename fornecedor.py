"""
Autor: Lucas de Lima Bica
Exercicio 18 Tema 3
"""

from pessoa import Pessoa


class Fornecedor(Pessoa):
    def __init__(self, nome, morada, telefone, valor_credito, valor_divida):
        super().__init__(nome=nome, morada=morada, telefone=telefone)
        self.__valor_credito = valor_credito
        self.__valor_divida = valor_divida

    @property
    def valor_credito(
        self,
    ):  # Correspondente ao crédito máximo atribuído/admitido pelo fornecedor
        return self.__valor_credito

    @valor_credito.setter
    def valor_credito(self, novo_valor_credito: float):
        self.__valor_credito = novo_valor_credito

    @property
    def valor_divida(self):  # Montante em dívida para com o fornecedor
        return self.__valor_divida

    @valor_divida.setter
    def valor_divida(self, novo_valor_divida: float):
        self.__valor_divida = novo_valor_divida

    def obter_saldo(self):
        return self.__valor_credito - self.__valor_divida

    def __str__(self) -> str:
        return f"{super().__str__()}\nCrédito: ${self.valor_credito:.2f}\nDívida: ${self.valor_divida:.2f}\nSaldo: ${self.obter_saldo():.2f}"

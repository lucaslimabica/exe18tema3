"""
Autor: Lucas de Lima Bica
Exercicio 18 Tema 3
May The Force Be With You
"""

from pessoa import Pessoa


class Empregado(Pessoa):
    def __init__(self, nome, morada, telefone, codigo_setor, salario_base, imposto):
        super().__init__(nome, morada, telefone)
        self.__codigo_setor = codigo_setor
        self.__salario_base = salario_base
        self.__imposto = imposto

    @property
    def codigo_setor(self):
        return self.__codigo_setor

    @codigo_setor.setter
    def codigo_setor(self, codigo_setor):
        self.__codigo_setor = codigo_setor

    @property
    def salario_base(self):
        return self.__salario_base

    @salario_base.setter
    def salario_base(self, salario_base):
        self.__salario_base = salario_base

    @property
    def imposto(self):
        return self.__imposto

    @imposto.setter
    def imposto(self, imposto):
        self.__imposto = imposto

    def calcular_salario(self):
        salario_liquido = self.__salario_base - (
            self.__salario_base * (self.__imposto / 100)
        )  # Se for 10% será 0.1
        return salario_liquido

    def __str__(self) -> str:
        return f"{super().__str__()}\nSalário Base: ${self.salario_base:.2f}\nImposto: {self.imposto}%\nSalário Líquido: ${self.calcular_salario():.2f}"

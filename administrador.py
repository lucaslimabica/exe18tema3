"""
Autor: Lucas de Lima Bica
Exercicio 18 Tema 3
May The Force Be With You
"""

from empregado import Empregado


class Administrador(Empregado):
    def __init__(
        self,
        nome,
        morada,
        telefone,
        codigo_setor,
        salario_base,
        imposto,
        ajuda_de_custos,
    ):
        super().__init__(nome, morada, telefone, codigo_setor, salario_base, imposto)
        self.__ajuda_de_custos = ajuda_de_custos

    @property
    def ajuda_de_custos(self):
        return self.__ajuda_de_custos

    @ajuda_de_custos.setter
    def ajuda_de_custos(self, novo_ajuda_de_custos: float):
        self.__ajuda_de_custos = novo_ajuda_de_custos

    def calcular_salario(self):
        salario_liquido = super().calcular_salario() + self.__ajuda_de_custos
        return salario_liquido

"""
Autor: Lucas de Lima Bica
Exercicio 18 Tema 3
May The Force Be With You
"""

from empregado import Empregado


class Vendedor(Empregado):
    def __init__(
        self,
        nome,
        morada,
        telefone,
        codigo_setor,
        salario_base,
        imposto,
        valor_vendas,
        comissao,
    ):
        super().__init__(nome, morada, telefone, codigo_setor, salario_base, imposto)
        self.__valor_vendas = valor_vendas
        self.__comissao = comissao

    @property
    def valor_vendas(self):
        return self.__valor_vendas

    @valor_vendas.setter
    def valor_vendas(self, novo_valor_vendas):
        self.__valor_vendas = novo_valor_vendas

    @property
    def comissao(self):
        return self.__comissao

    @comissao.setter
    def comissao(self, novo_comissao):
        self.__comissao = novo_comissao

    def calcular_salario(self):
        return super().calcular_salario() + (
            self.__valor_vendas * (self.__comissao / 100)
        )

    def __str__(self) -> str:
        return f"{super().__str__()}\nValor de Vendas: ${self.valor_vendas:.2f}\nComissão: {self.comissao}%"
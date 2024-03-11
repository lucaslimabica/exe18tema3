"""
Autor: Lucas de Lima Bica
Exercicio 18 Tema 3
May The Force Be With You
"""

from empregado import Empregado


def main():
    empregado1 = Empregado(
        nome="Lucas",
        morada="Faro",
        telefone="928",
        codigo_setor="3",
        salario_base=800,
        imposto=12,
    )
    print(f"Ficha do funcionário {empregado1.nome}")
    print(f"morador de {empregado1.morada}")
    print(f"com o contacto: {empregado1.telefone}")
    print(f"tem o salaráio de $ {float(empregado1.calcular_salario())}")
    print(empregado1)


main()

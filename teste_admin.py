"""
Autor: Lucas de Lima Bica
Exercicio 18 Tema 3
May The Force Be With You
"""

from administrador import Administrador


def main():
    empregado1 = Administrador(
        nome="Lucas",
        morada="Faro",
        telefone="928",
        codigo_setor="3",
        salario_base=800,
        imposto=12,
        ajuda_de_custos=300,
    )
    print(f"Ficha do Administrador {empregado1.nome}")
    print(f"morador de {empregado1.morada}")
    print(f"com o contacto: {empregado1.telefone}")
    print(f"tem o salário de ${empregado1.calcular_salario():.2f}")


main()

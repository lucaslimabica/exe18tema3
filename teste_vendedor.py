"""
Autor: Lucas de Lima Bica
Exercicio 18 Tema 3
May The Force Be With You
"""

from vendedor import Vendedor


def main():
    empregado1 = Vendedor(
        nome="Lucas",
        morada="Faro",
        telefone="928",
        codigo_setor="3",
        salario_base=800,
        imposto=12,
        valor_vendas=5000,
        comissao=5
    )
    print(f"Ficha do Vendedor {empregado1.nome}")
    print(f"Morada: {empregado1.morada}")
    print(f"Contacto: {empregado1.telefone}")
    print(f"Vendas: ${empregado1.valor_vendas:.2f}")
    print(f"Comissão: {empregado1.comissao}%")
    print(f"Salário: ${empregado1.calcular_salario():.2f}")
    print(empregado1)


main()

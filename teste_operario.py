"""
Autor: Lucas de Lima Bica
Exercicio 18 Tema 3
May The Force Be With You
"""

from operario import Operario


def main():
    empregado1 = Operario(
        nome="Lucas",
        morada="Faro",
        telefone="928",
        codigo_setor="3",
        salario_base=800,
        imposto=12,
        valor_producao=10000,
        comissao=1,
    )
    print(f"Operario {empregado1.nome}")
    print(f"Morada: {empregado1.morada}")
    print(f"Contacto: {empregado1.telefone}")
    print(f"Produção: ${empregado1.valor_producao:.2f}")
    print(f"Comissão: {empregado1.comissao}%")
    print(f"Salário: ${empregado1.calcular_salario():.2f}")
    print(empregado1)


main()

"""
Autor: Lucas de Lima Bica
Numa Galáxia Muito Distante
Exe 18 Tema 3
"""

from pyfiglet import figlet_format
from pessoa import Pessoa
from fornecedor import Fornecedor
from administrador import Administrador
from operario import Operario
from vendedor import Vendedor


def main():
    cliente = Pessoa("Arthur", "Saint Dennis", "123")
    fornecedor = Fornecedor("Susan", "Loulé", "150", 8000, 3800)
    gerente = Administrador("José", "Alcobaça", "129", 2, 720, 5, 200)
    producao = Operario("Lee", "Dalian", "333", "S2", 400, 9, 8000, 1)
    atendente = Vendedor("Lucas", "Faro", "928", "Vendas", 800, 13, 7000, 10)

    titulo = figlet_format("Enseada Clemens\n")
    print(titulo)
    print("Relatório Mensal")
    print("-" * 30)
    print(
        f"Principal Cliente: {cliente.nome} / Loja Preferida: Loja de {cliente.morada}"
    )
    print(
        f"Fornecedor: {fornecedor.nome} / Sede: {fornecedor.morada} / Saldo Actual: ${fornecedor.obter_saldo():.2f}"
    )
    print(
        f"Administração de Loja: {gerente.nome} / Morada: {gerente.morada} / Salário Líquido: ${gerente.calcular_salario():.2f}"
    )
    print(
        f"Funcionário do Mês: {producao.nome} / Morada: {producao.morada} / Salário Líquido: ${producao.calcular_salario():.2f} / Produção: ${producao.valor_producao:.2f}"
    )
    print(
        f"Vendedor Principal: {atendente.nome} / Morada: {atendente.morada} / Salário Líquido: ${atendente.calcular_salario():.2f} / Vendas: ${atendente.valor_vendas:.2f}"
    )
    print("-" * 30)

    escolha = input("Queres um relatório avançado individual de cada?(S/N)")
    if escolha.lower() == "s":
        print("---| Relatório Avançado |---")
        print(f"Cliente:\n{cliente}")
        print("---")
        print(f"Fornecedor:\n{fornecedor}")
        print("---")
        print(f"Administrador:\n{gerente}")
        print("---")
        print(f"Operário:\n{producao}")
        print("---")
        print(f"Vendedor:\n{atendente}")


if __name__ == "__main__":
    main()

"""
Autor: Lucas de Lima Bica
Exercicio 18 Tema 3
"""

from pessoa import Pessoa
from fornecedor import Fornecedor


def main():
    pessoa1 = Pessoa(nome="Lucas", morada="Faro", telefone="928")
    fornecedor1 = Fornecedor(
        valor_credito=1000,
        valor_divida=500,
        nome="João",
        morada="Tailândia",
        telefone="150",
    )
    pessoa2 = Pessoa.cria_anonimo()

    # Testes
    print(
        f"Meu nome é {pessoa1.nome}, moro em {pessoa1.morada} e meu telefone é: {pessoa1.telefone}"
    )
    print(
        f"Pretendo comprar uma camisola do {fornecedor1.nome}, que vive na {fornecedor1.morada} com o contacto: {fornecedor1.telefone}"
    )
    print(f"O meu saldo com o fornecedor é: $ {float(fornecedor1.obter_saldo())}")
    print(
        f"{fornecedor1.nome} tem outro cliente também, seu nome é: {pessoa2.nome}, que vive em {pessoa2.morada} com o número: {pessoa2.telefone}"
    )
    print(fornecedor1)


main()

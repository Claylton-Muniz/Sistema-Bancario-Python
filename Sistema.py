import os

saldo = 0
LIMITE_SAQUE = 3
saque = 0
extrato = ""

id_ext = 0
menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=>
"""

while True:

    op = int(input(f"\n{menu.strip()} "))

    if op == 1:

        val = float(input("Valor de depósito: R$"))

        if val >= 0:

            saldo += val
            print("Valor depositado com sucesso!")

            id_ext += 1
            extrato += f"{id_ext} - Houve um deposito de R${val:.2f} na sua conta. Agora seu saldo é de R${saldo:.2f}\n"

        else:
            print("Valor inválido para depósito!")

        input("Pressione Enter para continuar...")

    elif op == 2:

        val = float(input("Valor do saque: R$"))

        if val <= 500 and saque < LIMITE_SAQUE:

            saldo -= val
            saque += 1
            print("Saque feito com sucesso!")

            id_ext += 1
            extrato += f"{id_ext} - Houve um saque de R${val:.2f} na sua conta. Agora seu saldo é de R${saldo:.2f}\n"

        elif saque == 3:
            print("Número de saques diários excedido!")

        else:
            print("Valor inválido para saque!")

        input("Pressione Enter para continuar...")

    elif op == 3:
        print()
        print(extrato)
        
        input("Pressione Enter para continuar...")

    elif op == 4:
        print("Até a próxima!")
        break

    else:
        print("Valor inválido!")

    os.system("cls") # limpar tela windows

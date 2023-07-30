import os

def criar_user(users):

    user = {}

    user["nome"] = input("Nome: ")
    user["nascimento"] = input("Data de nascimento: ")

    count = 0
    while True:

        cpf = input("CPF: ")

        for verif in users:

            cpf_verif = verif["cpf"]

            if cpf == cpf_verif:
                count = 1

        if count == 0:
            user["cpf"] = cpf
            break

        print("Esse cpf já existe!")
        count = 0

    user["endereço"] = input("Endereço: ")
    user["contas"] = []

    return user


def criar_conta:



def saque(*, saldo, valor, ext, n_saque, LIMITE_SAQUE):

    if valor <= 500 and n_saque < LIMITE_SAQUE:

        saldo -= valor
        n_saque += 1
        print("Saque feito com sucesso!")

        ext += f"- Houve um saque de R${val:.2f} na sua conta. Agora seu saldo é de R${saldo:.2f}\n"

    elif n_saque == 3:
        print("Número de saques diários excedido!")

    else:
        print("Valor inválido para saque!")

    return saldo, ext, n_saque


def deposito(saldo, val, ext, /):

    if val >= 0:

        saldo += val
        print("Valor depositado com sucesso!")

        ext += f"- Houve um deposito de R${val:.2f} na sua conta. Agora seu saldo é de R${saldo:.2f}\n"

    else:
        print("Valor inválido para depósito!")

    return saldo, ext


def extrato(saldo, /, *, extrato):

    print(f"\n{ext}\nSaldo: R${saldo:.2f}\n")

users = []
saldo = 0
LIMITE_SAQUE = 3
n_saque = 0
ext = ""

menu = """

[1] Criar usuário
[2] Criar conta
[3] Depositar
[4] Sacar
[5] Extrato
[6] Sair

=>
"""

while True:

    op = int(input(f"\n{menu.strip()} "))

    if op == 1:

        users.append(criar_user(users))

        print(users)

        input()

    elif op == 2:



    elif op == 3:

        val = float(input("Valor de depósito: R$"))

        saldo, ext = deposito(saldo, val, ext)

        input("Pressione Enter para continuar...")

    elif op == 4:

        val = float(input("Valor do saque: R$"))

        saldo, ext, n_saque = saque(saldo=saldo, valor=val, ext=ext,
                                         n_saque=n_saque, LIMITE_SAQUE=LIMITE_SAQUE)

        input("Pressione Enter para continuar...")

    elif op == 5:

        extrato(saldo, extrato=ext)

        input("Pressione Enter para continuar...")

    elif op == 6:
        print("Até a próxima!")
        break

    else:
        print("Valor inválido!")

    os.system("cls") # limpar tela windows

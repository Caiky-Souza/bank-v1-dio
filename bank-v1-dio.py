import os

menu = """

Bem vindo ao Banco!

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Escolha: """

# Definindo variáveis

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


def depositar(x):
    #TODO
    global saldo
    global extrato

    saldo += x

    x_formatado = f"R$ {x}"
    extrato += f"- Depósito realizado no valor de {x_formatado}\n"
    
    print("Saldo adicionado com sucesso!")

def sacar(x):

    global saldo
    global extrato

    x_formatado = "R$ {}".format(x)

    if x > limite:
        print("O valor informado excede o limite permitido pelo sistema, tente novamente com um valor inferior.")
        return
    
    if numero_saques >= LIMITE_SAQUES:
        print("Você realizou o máximo de operações financeiras por hoje, tente novamente amanhã!")
        return
    
    if saldo < x:
        print("Lamentamos informar que você não possui saldo suficiente para retirar.")
        return
    else:
        saldo -= x
        extrato += f"- Saque realizado no valor de {x_formatado}\n"

        print("Saque realizado com sucesso!")

def main():

    # Mantém o menu
    while True:
        opcao = str(input(menu))
        os.system("clear")
        if opcao == "d":
            valor = int(input("Insira o valor que deseja depositar: "))
            depositar(valor)

        elif opcao == "s":
            valor = int(input("Insira o valor que deseja sacar: "))
            sacar(valor)

        elif opcao == "e":
            print(extrato + f"Saldo atual: {saldo}\n")

        elif opcao == "q":
            print("Agradecemos pela confiança! Esperamos vê-lo novamente.")
            break
        
        else:
            print("Opção inválida, por favor, verifique sua resposta")

main()
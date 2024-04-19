menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Saldo Atual
[5] Sair

"""
saldo = 0
limite = 500
extrato = ""
numeroSaques = 0
LIMITES_SAQUES = 3

while True:
    print(menu)
    opcao = int(input("Digite a opção: "))
    
    if opcao == 1:       
        valorDeposito = int(input("Digite o valor a ser depositado: R$"))
        if valorDeposito > 0:
            saldo += valorDeposito
            print(f"Depósito de R${valorDeposito} realizado com sucesso.")
            extrato += f"\nDepósito R${valorDeposito}"
        else:
            print("Não é possivel depositar valores negativos, Tente novamente!")


    elif opcao == 2:
        if numeroSaques < LIMITES_SAQUES:
            if saldo > 0:
                valorSaque = float(input("Digite o valor do saque: R$"))
                if valorSaque > 0:
                    if valorSaque <= saldo:
                        if valorSaque <= limite:
                            saldo -= valorSaque
                            extrato += f"\nSaque R${valorSaque}"
                            numeroSaques += 1
                            print(f"Saque de R${valorSaque} realizado com sucesso!")
                        else:
                            print(f"O limite de saque é R${limite}, Tente novamente!")
                    else:
                        print("Saldo não disponivel em conta!")
                else:
                    print("O valor do saque tem que ser POSITIVO")
            else:
                print("Você não tem saldo em conta!")    
        else:
            print("Limite de Saque excedido")    
    elif opcao == 3:
        print("-----EXTRATO-----")
        print(extrato)


    elif opcao == 4:
        print(f"Saldo Atual: {saldo}")


    elif opcao == 5:
        break

    
    else:
        print("Opção inválida, Tente novamente!")
print('----- SISTEMA BANCÁRIO -----')
menu = """
MENU:

    [0] Deposito
    [1] Saque
    [2] Extrato
    [3] Sair

=> """
saldo = 0
LIMITES_SAQUES = 3
numero_saque = 0
extrato = ""
limite = 500

while True:

    opcao = input(menu)

    if opcao == "0":
        valor = float(input("Informe o Valor que deseja depositar:  "))

        if valor > 0:
            print(f"Confira o valor: {valor:.2f}\n")
            confirmacao = str(input("O valor está correto?\n[1] Sim  [2] Não: "))

            if confirmacao == "1":
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n "
                print('Valor depositado!')

                voltarmenu = str(input("""\nVocê deseja fazer alguma outra transação?\n[1] Sim  [2] Não: """))
                if voltarmenu == "1":
                    menu
                elif voltarmenu == "2":
                    print("Obrigado!, Volte Sempre")
                    break

            elif confirmacao == "2":
                while True:
                    valor = float(input("\nInforme o Valor que deseja depositar:  "))
                    confirmacao = str(input("O valor está correto?\n[1] Sim  [2] Não: "))

                    if confirmacao == "1":
                        saldo += valor
                        extrato += f"Depósito: R$ {novovalor:.2f}\n "
                        print("Valor depositado!")

                        voltarmenu = str(input("""\nVocê deseja fazer alguma outra transação?\n[1] Sim  [2] Não: """))
                        if voltarmenu == "1":
                            menu
                        elif voltarmenu == "2":
                            print("Obrigado!, Volte Sempre")
                            exit()
                        break
                    elif confirmacao == "2":
                        continue
            else: 
                        print("Tente de novo!, opção não existente.")

    elif opcao == "1":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = valor > numero_saque >= LIMITES_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
            confirmacao = str(input("O valor está correto? [1] Sim  [2] Não: "))
            
            if confirmacao == "1":
                excedeu_saldo
                print("Operação falhou! Você não tem saldo suficiente.")

                novovalor = float(input("Informe o Valor que deseja sacar:  "))
                confirmacao = str(input("O valor está correto? [1] Sim  [2] Não: "))

                if confirmacao == "1":
                    excedeu_saldo
                    print("Operação falhou! Você não tem saldo suficiente.")
                
                    voltarmenu = str(input("""\nVocê deseja fazer alguma outra transação?\n[1] Sim  [2] Não: """))
                    if voltarmenu == "1":
                        menu
                    elif voltarmenu == "2":
                        print("Obrigado!, Volte Sempre")
                        break

            elif confirmacao == "2":
                valor = float(input("\nInforme o Valor que deseja depositar:  "))
                confirmacao = str(input("O valor está correto?\n[1] Sim  [2] Não: "))

                if confirmacao == "1":
                    excedeu_saldo
                    print("Operação falhou! Você não tem saldo suficiente.")

                    voltarmenu = str(input("""\nVocê deseja fazer alguma outra transação?\n[1] Sim  [2] Não: """))
                    if voltarmenu == "1":
                        menu
                    elif voltarmenu == "2":
                        print("Obrigado!, Volte Sempre")
                        exit()

        elif excedeu_limite:
                print("Operação falhou! Você excedeu o limite de saque.")
                voltarmenu = str(input("""\nVocê deseja fazer alguma outra transação?\n[1] Sim  [2] Não: """))
                if voltarmenu == "1":
                    menu
                elif voltarmenu == "2":
                    print("Obrigado!, Volte Sempre")
                    break

        elif excedeu_saques:
                print("Operação falhou! Você excedeu o limite de saque.")
                voltarmenu = str(input("""\nVocê deseja fazer alguma outra transação?\n[1] Sim  [2] Não: """))
                if voltarmenu == "1":
                    menu
                elif voltarmenu == "2":
                    print("Obrigado!, Volte Sempre")
                    exit()

        elif valor > 0:
            print(f"Confira o valor: {valor:.2f}\n")
            confirmacao = str(input("O valor está correto? [1] Sim  [2] Não: "))
            
            if confirmacao == "1":
                saldo -= valor
                extrato += f"\nSaque: R$ {valor:.2f}\n "
                numero_saque += 1
                print('Retire o dinheiro!')

                voltarmenu = str(input("""\nVocê deseja fazer alguma outra transação?\n[1] Sim  [2] Não: """))
                if voltarmenu == "1":
                    menu
                elif voltarmenu == "2":
                    print("Obrigado!, Volte Sempre")
                    break
        
            elif confirmacao == "2":
                valor = float(input("Informe o Valor que deseja depositar:  "))
                saldo -= valor
                extrato += f"\nSaque: R$ {valor:.2f}\n "
                numero_saque += 1
                print("Retire o dinheiro!")

                voltarmenu = str(input("""\nVocê deseja fazer alguma outra transação?\n[1] Sim  [2] Não: """))
                if voltarmenu == "1":
                    menu
                elif voltarmenu == "2":
                    print("Obrigado!, Volte Sempre")
                    break
                   
            else: 
                print("Tente de novo!, opção não existente.")
       
        else:
            print("Operação falhou! O valor informado é inválido")

    elif opcao == "2":
        print('\n========== EXTRATO ==========')
        print('\nNão foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('\n=============================')

    elif opcao == "3":
        print("Obrigado! Volte sempre.")
        break

    else:
        print('Operação falhou! por favor selecione novamente a operação desejada.')
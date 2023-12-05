"""
Criar um sistema implementando depósito, saque e apresentação de extrato

Depósito -> somente valores positivos -> armazenar depósitos em variável

Saque -> Somente 3 saques diários com limite de 500 por saque. -> Caso não tenha limite informar mensagem
-> deve ser armazenado em variável

Extrato -> Deve listar depósitos e saques. -> Deve ser exibido o valor atual da conta. -> Se não for realizado
nenhuma operação: exibir mensagem 'Não foram realizadas movimentações.

-> Deve ser exibidor o valor com duas casas decimais

"""

menu = """
        [d] Depositar
        [s] Saque
        [e] Extrato
        [q] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
numero_deposito = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = float(input('Insira o valor a ser depositado: '))
        if deposito > 0:
            saldo += deposito
            extrato += f'Depósito: R$: {deposito:.2f}\n'
        else:
            print('Valor inválido para operação. Por favor digite válido: ')

    elif opcao == "s":
        saque = float(input('Digite o valor a ser sacado: '))
        if saque > saldo:
            print('Valor não pode ser sacado. Saldo indisponível !')
        elif saque > 500:
            print('Valor sacado deve ser menor que R$ 500.00 !')
        elif saque > 0:
            numero_saques +=1
            if numero_saques > LIMITE_SAQUES:
                print('Saques diários excedidos !')
            else:
                saldo -= saque
                extrato += f'Saque: R$: {saque:.2f}\n'

        else:
            print('Valor inválido para operação')
            
              
        
    elif opcao == "e":
            print('==================EXTRATO======================')
            print('Não foram realizadas operações.' if not extrato else extrato)
            print(f'Saldo: R$ {saldo:.2f}')
            print('===============================================')


    elif opcao == "q":
        break
    
    else:
        print('Operação inválida. Por favor selecione novamente a opção desejada !')




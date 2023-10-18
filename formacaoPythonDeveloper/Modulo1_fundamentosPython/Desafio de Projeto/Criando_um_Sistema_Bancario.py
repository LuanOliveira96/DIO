menu = """ 

Olá!! Seja Bem vindo ao sistema Bancário. Selecione a opção desejada para seguir: 

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

retornar_menu = 0
saldo = 0
extrato = ""
limite_maximo_saque = 500
numero_saques = 0
LIMITE_SAQUES = 2


while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        
        while True:
            
            if retornar_menu == 1:
                retornar_menu = 0
                break
            
            print(" DEPÓSITO ".center(100,"="))
              
            valor = float(input("""
                         
            Realize o depósito desejado.
            (Lembrando: Aceitamos apenas valores inteiros e positivos :) ): 
                     
            *Aperte "0" para Cancelar o depósito e voltar ao MENU principal
                     
            """))
        
            if valor > 0:    
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                   
                while True:
                    decisao = str(input("""
            Valor depositado corretamente. Deseja fazer mais algum depósito? 
            Caso não queira, retornará automáticamente ao menu principal.
                                
            [Y] Fazer mais um depósito
            [N] Retornar ao MENU principal
                                
              """))

                    if decisao == "Y":
                        print("""
            Você escolheu fazer um novo depósito.""")
                        break                        
                    elif decisao == "N":
                        print("""
            ""Você escolheu retornar ao MENU Principal.""")
                        retornar_menu += 1
                        break
                    else:
                        print("""
            Opção inválida. Tente novamente: """)
                        
            elif valor == 0:
                break        
                
            else:
                print("\nDepósito inválido. Lembrando: Aceitamos apenas valores inteiros e positivos. Tente novamente\n")  
                
            print("=".center(100,"="))    
        
    elif opcao == "s":
                
        while True:
            #excedeu_saldo = (valor > saldo)
            #excedeu_limite = (valor > limite_maximo_saque)
            #excedeu_saques = (numero_saques > LIMITE_SAQUES)
            
            if numero_saques > LIMITE_SAQUES:
                print("""
            ""Você excedeu a quantidade de saques diários.
            Irá retornar ao MENU Principal automáticamente.""")
                break        
            
            if retornar_menu == 1:
                retornar_menu = 0
                break
                    
            print(" SAQUE".center(60,"="))
        
            valor = float(input("""
                         
            Realize o Saque desejado.
            (Lembrando: Aceitamos apenas valores positivos :) ): 
                     
            *Aperte "0" para Cancelar o Saque e voltar ao MENU principal
                     
            """))
        
            if valor > saldo:
                print("Operação Inválida. Você não tem saldo suficiente. Tente novamente. ")
            elif valor > limite_maximo_saque:
                print("Operação Inválida. O valor do saque excede o valor do limite. Tente novamente. ")
           # elif numero_saques > LIMITE_SAQUES:
            #    print("Operação Inválida. Você excedeu a quantidade de saques diários. Tente novamente. ")
            elif valor == 0:
                break
            elif valor > 0 and numero_saques <= LIMITE_SAQUES:
                numero_saques += 1
                saldo -= valor
                extrato += f"Saque R$: {valor:.2f}\n"    
            
                while True:
                    decisao = str(input("""
            Valor Sacado corretamente. Deseja fazer mais algum Saque? 
            Caso não queira, retornará automáticamente ao menu principal.
                                
            [Y] Fazer mais um Saque
            [N] Retornar ao MENU principal
                                
              """))

                    if decisao == "Y" and numero_saques <= LIMITE_SAQUES:
                        print("""
            Você escolheu fazer um novo Saque.""")
                        break
                    if decisao == "Y" and numero_saques > LIMITE_SAQUES:
                        print("""
            ""Você excedeu a quantidade de saques diários.
            Irá retornar ao MENU Principal automáticamente.""")
                        retornar_menu += 1
                        break
                                                
                    elif decisao == "N":
                        print("""
            ""Você escolheu retornar ao MENU Principal.""")
                        retornar_menu += 1
                        break
                    else:
                        print("""
            Opção inválida. Tente novamente: """)  
                          
        
        print("=".center(60,"="))
        
    elif opcao == "e":
        print(" EXTRATO ".center(60,"="))
             
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: {saldo:.2f}")      
        
        print("=".center(60,"="))
            
    elif opcao == "q":
        print("\nVocê saiu do sistema do banco. Obrigado por utilizar nossos serviços :) \n")
        break
    
    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada: \n")
        
# Escreva um programa que peça para o usuário informar um número inteiro e verificar se o número informado
# é múltiplo de 2 ou de 5.  Caso seja múltiplo apenas de 2 o programa deve informar " Múltiplo apenas de 2", 
# caso seja múltiplo apenas de 5 deve informar " Múltiplo apenas de 5", caso seja dos dois deve informar " 
# Múltiplo de 2 e 5" e caso não seja múltiplo de nenhum deve informar "Não é múltiplo de 2 nem de 5.". 

numero = int(input("Informe um número inteiro."))

if numero%2==0 and numero%5==0:
    print("É múltiplo de 2 e de 5.")
elif  numero%2==0 and numero%5!=0:
    print("É múltiplo apenas de 2.")
elif numero%2!=0 and numero%5==0:
    print("É múltiplo apenas de 5.")
else:
    print("Não é múltiplo nem de 2 nem de 5.")
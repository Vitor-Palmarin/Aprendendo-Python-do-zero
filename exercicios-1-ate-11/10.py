# Escreva um programa que paça para o usuário informar um número inteiro e verificar se ele é múltiplo de 2. 
# Em caso afirmativo, o programa deve mostrar a mensagem " O número informado é múltiplo de 2", caso contrário 
# deve informar "Não é múltiplo de 2".

numero = int(input("informe um número inteiro."))

if numero%2==0:
    print("O número informado é múltiplo de 2.")
else:
    print("O número informado não é múltiplo de 2.")


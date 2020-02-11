# Escreva um programa que peça para o usuário informar um número inteiro  e verificar se o número informado é primo.
# Em caso afirmativo, o programa deve mostrar a mensagem " O número informado é primo", caso contrário deve informar 
#"Não é primo". 

numero = int(input("Informe um número inteiro."))

# esse range vai começar em 2 e terminar em zero. 
#Lembrando que um número primo é divisível por 1 e por ele mesmo. 
# e para que um número seja divisível por outro, o resto da divisão deve ser zero
cont =0 

for i in range(2,10):
    if numero%i ==0:
        cont = cont +1 
    else:
        cont = cont

if cont > 1:
    print(" O número  não é primo.")
else: 
    print("O número é primo.")
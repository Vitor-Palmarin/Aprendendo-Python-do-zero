# Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do 
# usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao 
# informar o nome ousuário pode digitar letras maiúsculas ou minúsculas.

nome = input("Informe o seu nome")

# Fazendo uma cópia da string com letras maiúsculas 
nomeM = str.upper(nome)

# Escrevendo de trás prara frente 
print("String de trás para frente e maiúscula:", nomeM[::-1])
#Obs: [::-1] signigica [do começo:até o fim: no passo -1]
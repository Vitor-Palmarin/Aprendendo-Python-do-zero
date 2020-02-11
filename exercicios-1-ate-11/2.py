# Faça um programa que peça para que o usuario informe dois números e print as seguintes 
# informações sobre eles: 1) soma 2) subtração 3) produto 

print("Informe o que é pedido:")
# o print() vazio deixa um espaço
print()  

# Obs: lembre-se que a função input() lê a entrada como string, logo é preciso converter os tipos
numero1 = int(input("Informe o primeiro número inteiro:"))
print()
numero2 = int(input("Informe o segundo número inteiro:"))

soma = numero1 + numero2 
sub = numero1 - numero2 
mult = numero1 * numero2 

# Saídas 
print("Soma: ", soma) 
print()
print("Subtração: ", sub) 
print()
print("Multiplicação: ", mult) 


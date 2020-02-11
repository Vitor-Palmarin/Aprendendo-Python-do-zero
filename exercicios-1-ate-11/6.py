# Dado uma string com uma frase informada pelo usuário
# (incluindo espaços em branco), conte os espaços em branco presentes nela. 

frase = input("Informe uma frase." )

# Função para identificar os ' ' em branco 
qtd = frase.count(' ')
print("O número de espaços em branco na frase informada é:", qtd)
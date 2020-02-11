# Peça para que o usuário informe um número inteiro n > 0 e as notas finais de n alunos, determinar quantos alunos 
# ficaram de recuperação. Um aluno está de recuperação se sua nota final está entre 3.0 e 5.0 A nota máxima é 10.

n = int( input("Informe a quantidade de aluno"))

i = 0 

while i <= n:
    nota = float(input("Informe a nota final"))
    if nota>3.0 and nota <5.0:
        print("O aluno ficou de reuperação.")
    else:
        print(" O aluno não ficou de recuperação.")
    i = i+1 


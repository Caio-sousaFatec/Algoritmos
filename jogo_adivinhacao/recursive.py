import random;

def recursive_adivinhacao(n, contador_chances=0):
    if contador_chances == 5:
        print("infelizmente acabaram suas chances, você é muito burro")
        return
    guess = int(input("adivinhe qual número estou pensando "))
    if guess == n:
        print("parabéns, você acertou ")
        return
    else:
        print("infelizmente você errou ")
        if guess> n:
            print("o número que pensei é menor, tente novamente ")
        elif guess< n:
            print("o número que pensei é maior, tente novamente ")
        contador_chances+= 1
        recursive_adivinhacao(n, contador_chances)

n = int(random.randint(1, 10))
recursive_adivinhacao(n)

#passo 1 = é estabelecido os parâmetros de número adivinhado e contador de chances, com valor em 0
#passo 2 = é realizada uma comparação. se o contador for igual a 5, é interrompido o processo. 
#passo 3 = é realizada a coleta de um prompt inserido pelo usuario
#passo 4 = é realizado a comparação do prompt e do número, que é gerado aleatóriamente pela máquina, em função fora do laço
# caso comparação seja positiva, finaliza processo.
#passo 5 = caso comparação falsa, é informado que está errado, e é informado se é maior ou menor
# passo 6 = é realizada a soma do número de chances + 1
# passo 7 = é reutilizada a função, reemitindo o contador.

#teste de mesa, utilizando como variaveis n=1
#passo 1 = é estabelecido os parâmetros de número adivinhado e contador de chances, com valor em 0
#passo 2 = é realizada uma comparação. se o contador for igual a 5, é interrompido o processo. 
#passo 3 = é realizada a coleta de um prompt inserido pelo usuario(prompt = 4)
#passo 4 = é realizado a comparação do prompt e do número.
#passo 5 = a comparação é falsa, é dada a mensagem de que "infelizmente você errou"
#passo 6 = é realizada a validação que n é menor que guess e realizado o print "o número que pensei é menor, tente novamente "
#passo 7 = é realizado o acréscimo de +1 no contador de chances, totalizando 1 tentativa
#passo 8 = é utilizada a função novamente, utilizando como parâmetros (n = 1{em random} e contador_chances=1)
#passo 9 = é realizada uma comparação. se o contador for igual a 5, é interrompido o processo, no caso, contador!=5 
#passo 10 = é realizada a coleta de um prompt inserido pelo usuario(prompt = 2)
#passo 11 = é realizado a comparação do prompt e do número.
#passo 12 = a comparação é falsa, é dada a mensagem de que "infelizmente você errou"
#passo 13 = é realizada a validação que n é menor que guess e realizado o print "o número que pensei é menor, tente novamente "
#passo 14 = é realizado o acréscimo de +1 no contador de chances, totalizando 2 tentativas
#passo 15 = é utilizada a função novamente e dado +1 de profundidade na recursão
#passo 16 = é utilizada a função novamente, utilizando como parâmetros (n = 1{em random} e contador_chances=2)
#passo 17 = é realizada uma comparação. se o contador for igual a 5, é interrompido o processo, no caso, contador!=5 
#passo 18 = é realizada a coleta de um prompt inserido pelo usuario(prompt = 1)
#passo 19 = é realizado a comparação do prompt e n. n == prompt
#passo 20 = é dada o print "parabéns, você acertou "
#passo 21 = é dado o return, e finalizada a função 


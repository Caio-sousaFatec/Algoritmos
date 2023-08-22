import random;

def adivinhacao():
    n = int(random.randint(1, 10))
    for i in range(5):
        guessN = int(input("insira o número que desejar para adivinhar "))
        if guessN != n:
            print(" não, você errou")
            if guessN>n:
                print('pensei em um número menor')
            elif guessN<n:
                print("pensei em um número maior")
        elif guessN == n:
            print("parabéns, você acertou!!")
            return guessN
    if i == 4:
        print('suas chances acabaram, sinto muito')

adivinhacao();
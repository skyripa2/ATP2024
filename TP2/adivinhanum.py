print("Bem-vindo ao Adivinha o numero!")
print("se queres ser tu a pensar num número e ser eu a adivinhar, escreve 1. Se queres ser tu a adivinhar um número em que eu pensei, escreve 2")
answer = input("1 ou 2?")

while answer != "1" and answer != "2":
    print("resposta inválida")
    answer = input("1 ou 2?")

if answer == "1":
    import random
    numero_a_adivinhar = random.randrange(0, 101)
    tentativas = 0
    guess = int(input("Tenta adivinhar o número de 0-100!"))
    if guess == numero_a_adivinhar:
        tentativas = tentativas + 1
        print("Sim!")
    while guess != numero_a_adivinhar:
        tentativas = tentativas + 1
        if guess > numero_a_adivinhar:
            print("O número que pensei é Menor")
            guess = int(input("tenta outra vez"))
        elif guess < numero_a_adivinhar:
            print("O número que pensei é Maior")
            guess = int(input("tenta outra vez"))
    print(f"Acertou o número em {tentativas} tentativas")

elif answer == "2":
    tentativa1 = 1
    min = 0
    max = 100
    med = 50

    print(f"O número é {(min + max)//2}?")
    resposta = input("Se acertei diga sim, se o número escolhido for maior diga maior, se for menor diga menor")

    while resposta != "sim" and resposta != "maior" and resposta != "menor":
            print("resposta inválida")
            resposta = input("Se acertei diga sim, se o número escolhido for maior diga maior, se for menor diga menor")
    if resposta == "sim":
        print("Let's go, acertei em 1 tentativa!")
    while resposta == "menor" or resposta == "maior":
        tentativa1 = tentativa1 + 1
        if resposta == "maior":
            min = med + 1
            med = (min + max)//2
        elif resposta  == "menor": 
            max = med - 1
            med = (min + max)//2
        print(f"o número escolhido é {med}?")
        resposta = input("Se acertei diga sim, se o número escolhido for maior diga maior, se for menor diga menor")
        while resposta != "sim" and resposta != "maior" and resposta != "menor":
            print("resposta inválida")
            resposta = input("Se acertei diga sim, se o número escolhido for maior diga maior, se for menor diga menor")
    print (f"Let's go! Acertei em apenas {tentativa1} tentativas!")

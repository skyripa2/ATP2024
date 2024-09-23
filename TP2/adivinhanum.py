print("Bem-vindo ao Adivinha o numero!")
print("Se queres ser tu a adivinhar um número em que eu pensei, escreve modo2, se queres ser tu a pensar num número e ser eu a adivinhar, escreve modo1")
answer = input("modo1 ou modo2?")

while answer != "modo1" and answer != "modo2":
    print("resposta inválida")
    answer = input("modo1 ou modo2?")

if answer == "modo1":
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
elif answer == "modo2":
    tentativa1 = 1
    min = 0
    max = 100
    med = 50

    print(f"O número é {(min + max)//2}?")
    resposta = input("Se acertei diga sim, se o número escolhido for maior diga maior, se for menor diga menor")

    if resposta == "sim":
        print(f"Let's go, acertei em 1 tentativa!")
    while resposta == "menor" or resposta == "maior":
        tentativa1 = tentativa1 + 1
        if resposta == "maior":
            min = med + 1
            print(f"o número escolhido é {(min + max)//2}?")
            resposta = input("Se acertei diga sim, se o número escolhido for maior diga maior, se for menor diga menor")
        elif resposta  == "menor": 
            max = med - 1
            print(f"o número escolhido é {(min + max)//2}?")
            resposta = input("Se acertei diga sim, se o número escolhido for maior diga maior, se for menor diga menor")
    while resposta != "sim" or resposta != "maior" or resposta != "menor":
        print("resposta inválida")
        resposta = input("Se acertei diga sim, se o número escolhido for maior diga maior, se for menor diga menor")
    print (f"Let's go! Acertei em apenas {tentativa1} tentativas!")

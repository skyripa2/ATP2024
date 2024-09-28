modo = int(input("Olá! Se queres ser tu a começar primeiro, digita 1. Mas se quiseres que eu (PC) comece primeiro, digita 2"))

fosforos = 21

while modo != 1 and modo !=2:
    print("Resposta inválida. Tente novamente")
    modo = int(input("Olá! \nSe queres ser tu a começar primeiro, digita 1. \nMas se quiseres que eu comece primeiro, digita 2"))

if modo == 1:
    jogada1 = int(input("Escolhe o número de fósforos que queres retirar (1 a 4)."))

    while jogada1 > 4 or jogada1 < 1:
        print("Resposta inválida. Tente novamente")
        jogada1 = int(input("Escolhe o número de fósforos que queres retirar (1 a 4)."))

    fosforos = fosforos - jogada1
    print(f"Retiraste {jogada1} fósforos! Ficamos com {fosforos} fósforos.")

    while fosforos > 1:
        if fosforos >= 17 and fosforos <= 20:
            jogada2 = fosforos - 16
            fosforos = fosforos - jogada2
            print(f"Eu removi {jogada2} fósforos! Ficamos com {fosforos} fósforos.")
            jogada3 = int(input("Escolhe o número de fósforos que queres retirar (1 a 4)."))
            while jogada3 > 4 or jogada3 < 1:
                print("Resposta inválida. Tente novamente")
                jogada3 = int(input("Escolhe o número de fósforos que queres retirar (1 a 4)."))
            fosforos = fosforos - jogada3
            print(f"Retiraste {jogada3} fósforos! Ficamos com {fosforos} fósforos.")
        elif fosforos >= 12 and fosforos <= 15:
            jogada2 = fosforos - 11
            fosforos = fosforos - jogada2
            print(f"Eu removi {jogada2} fósforos! Ficamos com {fosforos} fósforos.")
            jogada3 = int(input("Escolhe o número de fósforos que queres retirar (1 a 4)."))
            while jogada3 > 4 or jogada3 < 1:
                print("Resposta inválida. Tente novamente")
                jogada3 = int(input("Escolhe o número de fósforos que queres retirar (1 a 4)."))
            fosforos = fosforos - jogada3
            print(f"Retiraste {jogada3} fósforos! Ficamos com {fosforos} fósforos.")
        elif fosforos >= 7 and fosforos <= 10:
            jogada2 = fosforos - 6
            fosforos = fosforos - jogada2
            print(f"Eu removi {jogada2} fósforos! Ficamos com {fosforos} fósforos.")
            jogada3 = int(input("Escolhe o número de fósforos que queres retirar (1 a 4)."))
            while jogada3 > 4 or jogada3 < 1:
                print("Resposta inválida. Tente novamente")
                jogada3 = int(input("Escolhe o número de fósforos que queres retirar (1 a 4)."))
            fosforos = fosforos - jogada3
            print(f"Retiraste {jogada3} fósforos! Ficamos com {fosforos} fósforos.")
        elif fosforos >= 2 and fosforos <= 5:
            jogada2 = fosforos -1
            fosforos = fosforos - jogada2
            print(f"Eu removi {jogada2} fósforos! Ficamos com {fosforos} fósforos.")
            jogada3 = int(input("Escolhe o número de fósforos que queres retirar (1 a 4)."))
            while jogada3 > fosforos:
                print("Resposta inválida. Tente novamente")
                jogada3 = int(input("Escolhe o número de fósforos que queres retirar (1 a 4)."))
            while jogada3 > 4 or jogada3 < 1:
                print("Resposta inválida. Tente novamente")
                jogada3 = int(input("Escolhe o número de fósforos que queres retirar (1 a 4)."))
            fosforos = fosforos - jogada3
            print(f"Retiraste {jogada3} fósforos! Ficamos com {fosforos} fósforos.")
        elif fosforos == 16 or fosforos == 11 or fosforos == 6:
            import random
            jogada2 = random.randint(1,4)
            fosforos = fosforos - jogada2
            print(f"Eu removi {jogada2} fósforos! Ficamos com {fosforos} fósforos.")
            jogada3 = int(input("Escolhe o número de fósforos que queres retirar (1 a 4)."))
            while jogada3 > 4 or jogada3 < 1:
                print("Resposta inválida. Tente novamente")
                jogada3 = int(input("Escolhe o número de fósforos que queres retirar (1 a 4)."))
            fosforos = fosforos - jogada3
            print(f"Retiraste {jogada3} fósforos! Ficamos com {fosforos} fósforos.")
    if fosforos == 0:
        print("Eu ganhei! Tiraste o último fósforo!")

if modo == 2:
    while fosforos > 1:
        if fosforos >= 17 and fosforos <= 20:
            jogada2 = fosforos - 16
            fosforos = fosforos - jogada2
            print(f"Eu removi {jogada2} fósforos! Ficamos com {fosforos} fósforos.")
            jogada3 = int(input("Escolhe o número de fósforos que queres retirar (1 a 4)."))
            while jogada3 > 4 or jogada3 < 1:
                print("Resposta inválida. Tente novamente")
                jogada3 = int(input("Escolhe o número de fósforos que queres retirar (1 a 4)."))
            fosforos = fosforos - jogada3
            print(f"Retiraste {jogada3} fósforos! Ficamos com {fosforos} fósforos.")
        elif fosforos >= 12 and fosforos <= 15:
            jogada2 = fosforos - 11
            fosforos = fosforos - jogada2
            print(f"Eu removi {jogada2} fósforos! Ficamos com {fosforos} fósforos.")
            jogada3 = int(input("Escolhe o número de fósforos que queres retirar (1 a 4)."))
            while jogada3 > 4 or jogada3 < 1:
                print("Resposta inválida. Tente novamente")
                jogada3 = int(input("Escolhe o número de fósforos que queres retirar (1 a 4)."))
            fosforos = fosforos - jogada3
            print(f"Retiraste {jogada3} fósforos! Ficamos com {fosforos} fósforos.")
        elif fosforos >= 7 and fosforos <= 10:
            jogada2 = fosforos - 6
            fosforos = fosforos - jogada2
            print(f"Eu removi {jogada2} fósforos! Ficamos com {fosforos} fósforos.")
            jogada3 = int(input("Escolhe o número de fósforos que queres retirar (1 a 4)."))
            while jogada3 > 4 or jogada3 < 1:
                print("Resposta inválida. Tente novamente")
                jogada3 = int(input("Escolhe o número de fósforos que queres retirar (1 a 4)."))
            fosforos = fosforos - jogada3
            print(f"Retiraste {jogada3} fósforos! Ficamos com {fosforos} fósforos.")
        elif fosforos >= 2 and fosforos <= 5:
            jogada2 = fosforos -1
            fosforos = fosforos - jogada2
            print(f"Eu removi {jogada2} fósforos! Ficamos com {fosforos} fósforos.")
            jogada3 = int(input("Escolhe o número de fósforos que queres retirar (1 a 4)."))
            while jogada3 > fosforos:
                print("Resposta inválida. Tente novamente")
                jogada3 = int(input("Escolhe o número de fósforos que queres retirar (1 a 4)."))
            while jogada3 > 4 or jogada3 < 1:
                print("Resposta inválida. Tente novamente")
                jogada3 = int(input("Escolhe o número de fósforos que queres retirar (1 a 4)."))
            fosforos = fosforos - jogada3
            print(f"Retiraste {jogada3} fósforos! Ficamos com {fosforos} fósforos.")
        elif fosforos == 16 or fosforos == 11 or fosforos == 6 or fosforos == 21:
            import random
            jogada2 = random.randint(1,4)
            fosforos = fosforos - jogada2
            print(f"Eu removi {jogada2} fósforos! Ficamos com {fosforos} fósforos.")
            jogada3 = int(input("Escolhe o número de fósforos que queres retirar (1 a 4)."))
            while jogada3 > 4 or jogada3 < 1:
                print("Resposta inválida. Tente novamente")
                jogada3 = int(input("Escolhe o número de fósforos que queres retirar (1 a 4)."))
            fosforos = fosforos - jogada3
            print(f"Retiraste {jogada3} fósforos! Ficamos com {fosforos} fósforos.")
    if fosforos == 0:
        print("Eu ganhei! Tiraste o último fósforo!")
    if fosforos == 1:
        print("Parabéns! Retirei o último fósforo, ganhaste-me!")

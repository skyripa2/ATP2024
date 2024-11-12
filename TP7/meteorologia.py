tabMeteo1 = [((2022,1,20), 2, 16, 0),((2022,1,21), 1, 13, 0.2), ((2022,1,22), 7, 17, 0.01)]

def menu ():
    print("-------------------------------Menu----------------------------------")
    print("1 - Temperatura média de cada dia")
    print("2 - Guardar tabela meteorológica")
    print("3 - Carregar tabela meteorológica")
    print("4 - Dia com temperatura mínima mais baixa")
    print("5 - Amplitude térmica em cada dia")
    print("6 - Dia com precipitação máxima")
    print("7 - Dia com precipitação superior a um valor'p'")
    print("8 - Maior número consecutivo de dias com precipitação abaixo de um valor 'p'")
    print("9 - Gráfico da temperatura mínima, máxima e de pluviosidade")
    print("0 - Sair")

cond = True
while cond == True:
    menu()
    op = input("introduza uma opção")
    while op not in ['1','2','3', '4', '5', '6','7','8','9','0']:
        print(f'A opção: {op} não é válida.')
        op = input("introduza uma opção")
    while op != "0":
        if op == "1":
            print(f'A temperatura média de cada dia foi {medias(tabMeteo1)}')
        elif op == "2":
            fnome = input("introduz o nome do ficheiro")
            guardaTabMeteo(tabMeteo1, fnome)
            print("Ficheiro guardado!")
        elif op == "3":
            fnome = input("introduz o nome do ficheiro que queres carregar")
            carregaTabMeteo(tabMeteo1)
            print("Ficheiro carregado!")
        elif op == "4":
            print(f' A temperatura mínima mais baixa foi {minMin(tabMeteo1)}.')
        elif op == "5":
            print(f'A amplitude térmica em cada dia foi {amplTerm(tabMeteo1)}')
        elif op == "6":
            print(f' O dia com precipitação máxima foi {maxChuva(tabMeteo1)}.')
        elif op == "7":
            p = float(input("introduz o valor de pluviosidade mínima desejado"))
            print(f' Os dias com precipitação superior ao valor p foram: {diasChuvosos(tabMeteo1, p)}.')
        elif op == "8":
            p = float(input("introduz o valor de pluviosidade desejado"))
            print(f' O maior número consecutivo de dias com precipitação abaixo de {p} foi {maxPeriodoCalor(tabMeteo1, p)}.')
        elif op == "9":
            grafTabMeteo(tabMeteo1)
        elif op == "0":
            cond = False
        else:
            print(f'A opção {op} não é valida.')
            op = input("introduza uma opção")
print("Obrigado e volte sempre bestie!")

def medias(tabMeteo):
    res = []
    for i in tabMeteo:
        media = (i[1] + i[2])/2
        data = i[0]
        res.append((data,media))
    return res

def guardaTabMeteo(t, fnome):
    file = open(fnome, "w")
    for data,min,max,prec in t:
        ano, mes, dia = data
        data = f'{ano}-{mes}-{dia}'
        registo = f'{data}/{min}/{max}/{prec}\n'
        file.write(registo)

    file.close()
    return

def carregaTabMeteo(fnome):
    res = []
    file = open(fnome, "r")
    for line in file:
        line = line[:-1]
        #line = line.strip()
        campos = line.split("/")
        data, min, max, prec = campos
        ano, mes, dia = data.split("-")
        # ou campos[0] = campos[0].split("-")
        tuplo = ((int(ano),int(mes),int(dia)), float(min), float(max), float(prec))
        res.append(tuplo)
    file.close()
    return res

def minMin(tabMeteo):
    minima = tabMeteo1[0][1]
    for dia in tabMeteo1:
        if dia[1] < minima:
            minima = dia[1]
    return minima

def amplTerm(tabMeteo):
    res = []
    for i in tabMeteo:
        amplitude = i[1] - i[2]
        data = i[0]
        res.append((data,amplitude))
    return res 

def maxChuva(tabMeteo):
    max_prec = tabMeteo[0][3]
    max_data = tabMeteo[0][0]
    for dia in tabMeteo:
        if dia[3] > max_prec and dia[0] != max_data:
            max_prec = dia[3]
            max_data = dia[0]
    return (max_data, max_prec)

def diasChuvosos(tabMeteo, p):
    res = []
    for data, max, min, prec in tabMeteo:
        if prec > p:
            res.append((data, prec))
    return res

def maxPeriodoCalor(tabMeteo, p):
    consecutivos = 0
    consecutivos_global = 0
    for dias in tabMeteo:
        if dias[3] < p:
            consecutivos = consecutivos + 1
        else:
            if consecutivos_global < consecutivos:
                consecutivos_global = consecutivos
            consecutivos = 0

    if consecutivos_global < consecutivos:
        consecutivos_global = consecutivos

    return consecutivos_global

import matplotlib.pyplot as plt

def grafTabMeteo(t):
    # [expressao for elem in lista]
    datas = [f'{data[0]}-{data[1]}-{data[2]}' for data, *_ in t]
    temps_min = [min for data, min, *_ in t]
    temps_max = [max for data, min, max, *_ in t]
    precs = [prec for data, min, max, prec in t]

    plt.plot(datas,temps_min, label ="Temperatura Mínima", color = "b", marker = "o")
    plt.plot(datas,temps_max, label ="Temperatura Máxima", color = "r", marker = "o")
    plt.xlabel("Data")
    plt.ylabel("Temperatura ºC")
    plt.title("Temperatura mínima")
    plt.legend()
    plt.show()

    plt.bar(datas, precs, label = "Precipitação", color ="c")
    plt.xlabel("Data")
    plt.ylabel("Precipitação mm")
    plt.title("Precipitação")
    plt.legend()
    plt.show
    return

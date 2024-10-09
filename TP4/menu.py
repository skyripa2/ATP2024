def menu():
    print("-------------------Menu-------------------")
    print("1 - criar um lista")
    print("2 - ler lista")
    print("3 - calcular a soma do elementos da lista")
    print("4 - calcular a média do elementos da lista")
    print("5 - descobrir o maior elemento da lista")
    print("6 - descobrir o menor elemento da lista")
    print("7 - descobrir se a lista se encontra por ordem crescente")
    print("8 - descobrir se a lista se encontra por ordem decrescente")
    print("9 - procurar um elemento específico na lista")
    print("0 - Sair")

import random

def criaLista(lista):
    lista=[]
    tamanho = int(input("Diga de que tamanho quer a lista."))
    i = 0
    for i in range(tamanho):
        numcomp= random.randint(1,100)
        i = i +1
        lista.append(numcomp)
    return lista


def lerLista(lista):
    lista=[]
    tamanho2 = int(input("Diga de que tamanho quer a lista."))
    i2=0
    for i2 in range(tamanho2):
        numut= int(input("Diga um número para adicionar à lista."))
        i2 =i2 +1
        lista.append(numut)
    return lista


def somaLista(lista):
    res =0
    for i in lista:
        res = res + i
    return res


def mediaLista(lista):
    if len(lista) == 0:
        print(0)
    else:
        res1 =0
        for i in lista:
            res1 = res1 + i
        return res1/len(lista)


def maiorLista(lista):
    c= lista[0]
    for i in lista:
        if i > c:
            c = i
    
    return c


def menorLista(lista):
    c1=lista[0]
    for i in lista:
        if i < c1:
            c1=i
    return c1 


def estaOrdenada(lista):
    cond = True
    for i in range(len(lista)-1):
        if lista[i]>lista[i+1]:
            cond = False
    return cond


def estaOrdenada1(lista):
    cond1 = True
    for i in range(len(lista)-1):
        if lista[i]<lista[i+1]:
            cond1 = False
    return cond1

def procurarLista(lista,elemento):
    posicao= -1
    for i in range(len(lista)):
        if elemento == lista[i]:
            posicao = i
    return posicao


cond2 = True
lista=[]
while cond2:
    menu()
    opcao = input("Introduza uma opção")

    if opcao == "1":
        lista=criaLista(lista)
        print("A lista é:", lista)

    elif opcao== "2":
        lista =lerLista(lista)
        print("A lista é:", lista)

    elif opcao=="3":
        print(f"A soma de todos os elementos da lista é {somaLista(lista)}")
    
    elif opcao=="4":
        print(f"A média dos elementos da lista é {mediaLista(lista)}")
    
    elif opcao=="5":
        print(f"O maior número da lista é {maiorLista(lista)}")

    elif opcao=="6":
        print(f"O menor número da lista é {menorLista(lista)}")

    elif opcao=="7":
        if estaOrdenada(lista) == True:
            print("Alista está por ordem crescente.")
        else :
            print("A lista não está por ordem crescente.")
    
    elif opcao=="8":
        if estaOrdenada1(lista) == True:
            print("Alista está por ordem decrescente.")
        else :
            print("A lista não está por ordem decrescente.")
    
    elif opcao=="9":
        elemento=int(input("Diga o elemento que procura:"))
        posicao = procurarLista(lista,elemento)
        if posicao !=-1:
            print(f"o elemento {elemento} encontra-se na posição {posicao}")
        else :
            print(f"o elemento {elemento} não foi encontrado.")
            
    elif opcao == "0":
        cond2 = False
print("Volte sempre!")

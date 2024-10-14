
def listar(cinema):
    print("----------------------LISTA DE SALAS-------------------------")
    for s in cinema:
        nlugares, vendidos, filme, nome = s
        print(f" Nome: {nome} Filme: {filme}")
    print("---------------------------------------------------------------")
    return

def disponivel(cinema, filmes, lugar):
    cond= False
    for s in cinema:
        nlugares, vendidos, filme, nome = s
        if filme == filmes and lugar <= nlugares:
            if lugar not in vendidos:
                cond = True
    return cond

def vendebilhete(cinema, filmes, lugar):
    if disponivel(cinema, filmes, lugar):
        for s in cinema:
            nlugares, vendidos, filme, nome = s
            if filme == filmes:
                vendidos.append(lugar)
    return cinema

def listardisponibilidades (cinema):
    print("----------------------LISTA DE SALAS-------------------------")
    for s in cinema:
        nlugares, vendidos, filme, nome = s
        print(f" Nome: {nome} Filme: {filme} Lugares disponíveis {nlugares-len(vendidos)}")
    print("---------------------------------------------------------------")
    return

def existesala(cinema, nome):
    cond = False
    for sala in cinema:
        if sala[3] == nome:
            cond = True
    return cond

def devolvebilhete(cinema, filmes, lugar):
    for s in cinema:
        nlugares, vendidos, filme, nome = s
        if lugar in vendidos:
            vendidos.remove(lugar)
    return cinema

def criasala(cinema, filmes, nlugares, nome):
    vendidos = []
    s = (nlugares, vendidos, filmes, nome)
    if not existesala(cinema, nome):
        cinema.append(s)
    return

def retirarsala(cinema, nomes):
    for s in cinema:
        nlugares, vendidos, filme, nome = s
        if nomes == nome:
            cinema.remove(s)
    return cinema

def menu():
    print("-------------------Menu-------------------")
    print("1 - reset")
    print("2 - Criar Sala")
    print("3 - Remover Sala")
    print("4 - Listar Salas")
    print("5 - Disponibilidade de Salas")
    print("6 - Vender bilhetes")
    print("7 - Existe Sala?")
    print("8 - Devolver bilhete")
    print("9 - Disponibilidade de lugar")
    print("0 - Sair")

cond2 = True
cinema = []
while cond2:
    menu()
    opcao = input("Introduza uma opção")

    if opcao == "1":
        cinema.clear()

    elif opcao== "2":
        filmes = input("Introduza o nome do filme")
        nlugares = int(input("Introduza quantos lugares tem a sala"))
        nome = input("Introduza o nome da sala")
        criasala(cinema, filmes, nlugares, nome)

    elif opcao=="3":
        nomes = input("Introduza o nome da sala que quer remover")
        retirarsala(cinema, nomes)
    
    elif opcao=="4":
        listar(cinema)
    
    elif opcao=="5":
        listardisponibilidades (cinema)

    elif opcao=="6":
        filmes = input("Introduza o nome do filme")
        lugar = int(input("Introduza o lugar que quer comprar"))
        vendebilhete(cinema, filmes, lugar)

    elif opcao=="7":
        nome = input("Introduza o nome da sala")
        if existesala(cinema, nome):
            print("Sala existe.")
        else:
            print("Sala não existe.")
    
    elif opcao=="8":
        filmes = input("Introduza o nome do filme")
        lugar = int(input("Introduza o lugar que quer devolver"))
        devolvebilhete(cinema, filmes, lugar)
    
    elif opcao=="9":
        filmes = input("Introduza o nome do filme")
        lugar = int(input("Introduza o número do lugar"))
        if disponivel(cinema, filmes, lugar):
            print("Lugar disponível.")
        else:
            print("Lugar indisponível.")
            
    elif opcao == "0":
        cond2 = False
print("Volte sempre!")

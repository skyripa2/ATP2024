import json
import matplotlib.pyplot as plt

def inserirRegisto(ata):
    title = input("Digite o título (obrigatório): ")
    while not title:  
        print("Título é obrigatório!")
        title = input("Digite o título (obrigatório): ")
    
    cond = True
    while cond:
        nova_data = input(f"Nova data de publicação (formato: AAAA-MM-DD): ").strip()  
                
        partes_data = nova_data.split("-")
        if len(partes_data) == 3:
            ano, mes, dia = partes_data
            if len(ano) == 4 and ano.isdigit() and len(mes) == 2 and mes.isdigit() and len(dia) == 2 and dia.isdigit():
                publish_date = nova_data
                cond =False
            else:
                print("Formato de data inválido. Por favor, insira no formato AAAA-MM-DD.")
        else:
            print("Formato de data inválido. Por favor, insira no formato AAAA-MM-DD.")
    
    authors = []
    author_name = input("Digite o nome do autor (obrigatório): ")
    while not author_name:  
        print("Nome do autor é obrigatório!")
        author_name = input("Digite o nome do autor (obrigatório): ")
    
    author_affiliation = input("Digite a afiliação do autor (opcional): ")
    author_orcid = input("Digite o orcid do autor (opcional): ")
    aut = {'name': author_name, 'affiliation': author_affiliation, 'orcid': author_orcid}
    authors.append(aut)
    
    res = input("Quer adicionar outro autor? (s/n): ")
    while res == "s":  
        author_name = input("Digite o nome do autor (obrigatório): ")
        while not author_name:
            print("Nome do autor é obrigatório!")
            author_name = input("Digite o nome do autor (obrigatório): ")
        
        author_affiliation = input("Digite a afiliação do autor (opcional): ")
        author_orcid = input("Digite o orcid do autor (opcional): ")
        aut = {'name': author_name, 'affiliation': author_affiliation, 'orcid': author_orcid}
        authors.append(aut)
        
        res = input("Quer adicionar outro autor? (s/n): ")
    
    abstract = input("Digite o resumo (opcional): ")
    keywords = input("Digite as palavras-chave (opcional): ")
    doi = input("Digite o DOI (opcional): ")
    pdf = input("Digite o link para o PDF (opcional): ")
    url = input("Digite a URL (opcional): ")
    
    pubn = {
        'abstract': abstract,
        'keywords': keywords,
        'authors': authors,
        'doi': doi,
        'pdf': pdf,
        'publish_date': publish_date,
        'title': title,
        'url': url
    }
    
    ata.append(pubn)
    
    return ata


def carregarFicheiro(fnome):
    f = open("./trabalho/data_bio/"+ fnome, encoding='utf-8')
    ata = json.load(f)
    f.close()
    return ata

def listarAutor(fnome):
    res = []
    for d in fnome:
        for autor in d['authors']:
            if autor['name'] not in res:
                res.append(autor['name'])
    res.sort()
    return res

def postAutor(fnome, autor):
    posts = []
    for d in fnome:
        for aut in d['authors']:
            if aut['name'] == autor:
                posts.append(d['title'])
    return posts

def buscaporTitulo(fnome, titulo):
    i = 0  
    publicacao_encontrada = None 
    while i < len(fnome):
        if 'title' in fnome[i] and fnome[i]['title'] == titulo:  
            publicacao_encontrada = fnome[i]  
        i = i + 1
    
    return publicacao_encontrada if publicacao_encontrada else "Publicação não encontrada."

def postsPorAutor(fnome):
    dis = {}
    for d in fnome:
        for aut in d['authors']:
            if aut['name'] in dis:
                dis[aut['name']] = dis[aut['name']] + 1
            else:
                dis[aut['name']] = 1
    return dis

def ordenaAutor(fnome):
    posts_autor=postsPorAutor(fnome)
    ordena= sorted(posts_autor.items(), key=lambda item: item[1], reverse=True)
    return ordena[:20]

def graficoPostAutor(fnome):

    autores_ordenados=ordenaAutor(fnome)
    nomes= [autor[0] for autor in autores_ordenados]
    contagem = [autor[1] for autor in autores_ordenados]


    plt.bar(nomes, contagem, color="c")
    plt.xticks(rotation=45, ha='right')
    plt.xlabel("Nome dos autores")
    plt.ylabel("Nº de publicações")
    plt.title("Top 20 de autores por número de publicações")
    plt.legend()
    plt.show()
    return

def eliminar(fnome, title):
    inicial = len(fnome)
    fnome[:] = [dicionario for dicionario in fnome if 'title' not in dicionario or dicionario['title'] != title]
    
    if len(fnome) < inicial:
        print(f"Publicação com título '{title}' removida com sucesso.")
    else:
        print(f"Nenhuma publicação encontrada com o título '{title}'.")
    
    return fnome

def ordenarpordata(res):
    return sorted(res, key=lambda pub: pub['publish_date'])

def ordenaportitulo(res):
    return sorted(res, key=lambda pub: pub['title'])


def consultarRegisto_titulo(fnome, titulo):
    res = []
    continuar = True  
    while continuar:
        res = []
        for dicionario in fnome:
            if 'title' in dicionario and dicionario['title'].lower() == titulo.lower():
                res.append(dicionario)
        if res:
            continuar = False 
        else:
            titulo = input("Título inexistente. Insira outro título ou digite 'sair' para encerrar: ").strip()
            if titulo.lower() == 'sair':
                continuar = False  
    if not res:
        print("Pesquisa encerrada sem resultados.")
    return res



def consultarRegisto_palavras(fnome, keywords):
    res = []
    continuar = True  
    while continuar:
        res = []
        for pub in fnome:
            if 'keywords' in pub:
                keyword_lista = pub['keywords'].split(", ")
                keywords_normalizadas = [k.strip().lower() for k in keyword_lista]
                if keywords.lower() in keywords_normalizadas:
                    res.append(pub)
        if res:
            continuar = False 
        else:
            keywords = input("Não foram encontradas publicações com essa palavra-chave. Insira outra palavra-chave ou digite 'sair' para encerrar: ").strip()
            if keywords.lower() == 'sair':
                continuar = False 
    if not res:
        print("Pesquisa encerrada sem resultados.")
    return res

def consultarRegisto_data(fnome, publish_date):
    res = []
    continuar = True  
    while continuar:
        res = []
        for pub in fnome:
            if 'publish_date' in pub and pub['publish_date'] == publish_date:
                res.append(pub)
        if res:
            continuar = False  
        else:
            publish_date = input("Não foram encontradas publicações para essa data. Insira outra data (YYYY-MM-DD) ou digite 'sair' para encerrar: ").strip()
            if publish_date.lower() == 'sair':
                continuar = False 
    if not res:
        print("Pesquisa encerrada sem resultados.")
    return res


def consultarRegisto_autor(fnome, autor):
    res = []
    continuar = True 
    while continuar:
        res = []
        for pub in fnome:
            if 'authors' in pub:
                for aut in pub['authors']:
                    if autor.lower() == aut['name'].lower():
                        res.append(pub)
        if res:
            continuar = False  
        else:
            autor = input("Não foram encontradas publicações com esse autor. Insira outro autor ou digite 'sair' para encerrar: ").strip()
            if autor.lower() == 'sair':
                continuar = False 
    if not res:
        print("Pesquisa encerrada sem resultados.")
    return res


def consultarRegisto_afiliacao(fnome, afiliacao):
    res = []
    continuar = True 
    while continuar:
        res = []
        for pub in fnome:
            if 'authors' in pub:
                for aut in pub['authors']:
                    if 'affiliation' in aut:
                        afiliacoes = aut['affiliation'].strip(".").split(". ")
                        if afiliacao in afiliacoes:
                            res.append(pub)
        if res:
            continuar = False  
        else:
            afiliacao = input("Não foram encontradas publicações com essa afiliação. Insira outra afiliação ou digite 'sair' para encerrar: ").strip()
            if afiliacao.lower() == 'sair':
                continuar = False 
    if not res:
        print("Pesquisa encerrada sem resultados.")
    return res



def ordenaportitulo(res):
    return sorted(res, key=lambda pub: pub['title'])

def listar_Keyw(fnome):
    dic={}
    for d in fnome:
        if 'keywords' in d:
            for keyw in d['keywords'].split(", ")[:-1]:
                if keyw in dic:
                    dic[keyw]=dic[keyw]+1
                else:
                    dic[keyw]=1
    return dic

def ordena_Keyw_ocor(fnome):
    dis_keywords=listar_Keyw(fnome)
    dic_ordenada=sorted(dis_keywords.items(), key=lambda item: item[1])
    return dic_ordenada

def ordena_Keyw_alfa(fnome):
    dis_keywords=listar_Keyw(fnome)
    dic_ordenada=sorted(dis_keywords)
    return dic_ordenada

def post_keyw(fnome, key_w):
    posts = []
    key_w = key_w.lower()  
    for d in fnome:
        if 'keywords' in d:
            for keyw in d['keywords'].split(", ")[:-1]:
                if keyw.lower() == key_w:  
                    posts.append(d['title'])

    return sorted(posts)

def distrib_pub_ano(fnome):
    dic={}
    for d in fnome:
        if 'publish_date' in d :
            ano =d['publish_date'][:4]
            if ano in dic:
                    dic[ano] = dic[ano] + 1
            else:
                    dic[ano]=1
        else:
            if 'sem data' in dic:
                dic['sem data']=dic['sem data']+1
            else:
                dic['sem data']=1
    return dic

def ordena_Ano_pub(fnome):
    dis_pub_ano=distrib_pub_ano(fnome)
    dic_ordenada=sorted(dis_pub_ano.items())
    return dic_ordenada

def graficoPub_Ano(fnome):

    datas_pub=ordena_Ano_pub(fnome)
    data= [ano[0] for ano in datas_pub ]
    contagem = [ano[1] for ano in datas_pub]

    plt.bar(data, contagem, color="c")
    plt.xticks(rotation=45, ha='right')
    plt.xlabel("Anos")
    plt.ylabel("Nº de publicações")
    plt.title("Distribução de publicações por ano")
    plt.show()
    return

def ordena_Keyw_ocor_top20(fnome):
    dis_keywords=listar_Keyw(fnome)
    dic_ordenada=sorted(dis_keywords.items(), key=lambda item: item[1], reverse=True)
    return dic_ordenada[:20]

def graficoFreq_keyw(fnome):

    freq_keyw=ordena_Keyw_ocor_top20(fnome)
    keyw= [keyw[0] for keyw in freq_keyw ]
    contagem = [keyw[1] for keyw in freq_keyw]

    plt.bar(keyw, contagem, color="c")
    plt.xticks(rotation=45, ha='right')
    plt.xlabel("Palavras-chave")
    plt.ylabel("Frequência de aparição")
    plt.title("Distribução do top20 de palavras-chave pela sua frequência")
    plt.show()
    return

def salvar_dados(fnome, ata):
    f = open(fnome, 'w', encoding='utf-8')
    json.dump(ata, f, ensure_ascii= False, indent=4)
    f.close()

def distrib_keyw_ano(fnome, ano):
    dic={}
    for pub in fnome:
        if 'publish_date' in pub:
            if pub['publish_date'].split('-')[0]==ano:
                if 'keywords' in pub:
                    for keyw in pub['keywords'].split(", ")[:-1]:
                        if keyw in dic:
                            dic[keyw]=dic[keyw]+1
                        else:
                            dic[keyw]=1
    return dic

def ordena_Keyw_ocor_ano_top20(fnome, ano):
    dis_keywords=distrib_keyw_ano(fnome, ano)
    dic_ordenada=sorted(dis_keywords.items(), key=lambda item: item[1], reverse=True)
    return dic_ordenada[:20]

def graficoFreq_keyw_ano(fnome,ano):

    freq_keyw=ordena_Keyw_ocor_ano_top20(fnome,ano)
    keyw= [keyw[0] for keyw in freq_keyw ]
    contagem = [keyw[1] for keyw in freq_keyw]

    plt.bar(keyw, contagem, color="c")
    plt.xticks(rotation=45, ha='right')
    plt.xlabel("Palavras-chave")
    plt.ylabel("Frequência de aparição")
    plt.title(f"Distribução de palavras-chave pela sua frequência em {ano}")
    plt.show()
    return

def exportar(resultados, nome_arquivo):                 
    resposta = input("Deseja exportar dados? (s/n)").strip().lower()
    if resposta == "s":
        nome_arquivo = input("Coloque o nome do ficheiro que quer: ").strip()
        file = open(nome_arquivo, "w", encoding="utf-8")
        json.dump(resultados, file, ensure_ascii= False, indent = 4)
        file.close()
        print(f"Resultados exportados com sucesso para {nome_arquivo}.")
    elif resposta == "n":
        menu()
    elif resposta != "n" and resposta != "s":
        print("Resposta inválida, tente novamente.")
    if not resultados:
        print("Nenhum resultado para exportar.")
        return
    
def import_dados(fnome, ata):
    f = open("./trabalho/data_bio/" + fnome, encoding='utf-8')
    novos_dados= json.load(f)
    ata.append(novos_dados)
    f.close()
    return ata
    
def atualizarPublicacao(fnome):
    titulo = input("Digite o título da publicação que deseja atualizar: ")
    publicacao_encontrada = False
    
    for d in fnome:
        if 'title' in d and d['title'] == titulo:
            publicacao_encontrada = True
            
            print(f"Atualizando a publicação: {titulo}")
            cond = True
            while cond:
                nova_data = input(f"Nova data de publicação (formato: AAAA-MM-DD, deixe em branco para não alterar): ").strip()
                if nova_data == "":
                    cond = False  
                
                partes_data = nova_data.split("-")
                if len(partes_data) == 3:
                    ano, mes, dia = partes_data
                    if len(ano) == 4 and ano.isdigit() and len(mes) == 2 and mes.isdigit() and len(dia) == 2 and dia.isdigit():
                        d['publish_date'] = nova_data
                        cond =False
                    else:
                        print("Formato de data inválido. Por favor, insira no formato AAAA-MM-DD.")
                else:
                    print("Formato de data inválido. Por favor, insira no formato AAAA-MM-DD.")


            novo_resumo = input(f"Novo resumo (deixe em branco para não alterar): ")
            if novo_resumo:
                d['abstract'] = novo_resumo

            novas_palavras_chave = input(f"Novas palavras-chave (separadas por vírgula e espaço, deixe em branco para não alterar): ")
            if novas_palavras_chave:
                d['keywords'] = novas_palavras_chave

            novo_doi = input(f"Novo DOI (deixe em branco para não alterar): ")
            if novo_doi:
                d['doi'] = novo_doi

            novo_pdf = input(f"Novo link para o PDF (deixe em branco para não alterar): ")
            if novo_pdf:
                d['pdf'] = novo_pdf

            nova_url = input(f"Nova URL (deixe em branco para não alterar): ")
            if nova_url:
                d['url'] = nova_url

            atualizar_autores = input("Deseja atualizar os autores? (s/n): ")
            if atualizar_autores.lower() == "s":
            
                if 'authors' not in d:
                    d['authors'] = []
                
                autores_atualizados = d['authors'] 
                nomes_autores = {autor['name'] for autor in autores_atualizados}  

                nome_autor = ""
                cond=True
                while cond:  
                    nome_autor = input("Nome do autor (deixe em branco para terminar): ")
                    
                    if nome_autor == "":  
                        cond = False
                
                    if nome_autor not in nomes_autores:
                        autor = {'name': nome_autor}

                        afiliacao = input(f"Afiliação de {nome_autor} (deixe em branco para não adicionar): ")
                        if afiliacao:
                            autor['affiliation'] = [afiliacao]
                        
                        orcid = input(f"ORCID de {nome_autor} (deixe em branco para não adicionar): ")
                        if orcid:
                            autor['orcid'] = [orcid]
                        
                        autores_atualizados.append(autor)
                        nomes_autores.add(nome_autor) 
                    else:
                        print(f"O autor '{nome_autor}' já está na lista de autores.")
            
            print(f"Publicação '{titulo}' atualizada com sucesso!")
    
    if not publicacao_encontrada:
        print("Publicação não encontrada.")

def listar_autor_pub(fnome):
    res={}
    for pub in fnome:
        if "authors" in pub:
            for autor in pub["authors"]:
                nome = autor["name"]
                if nome not in res:
                    res[nome]=[]
                res[nome].append(pub)
                    
    return res

def AutorporAno(fnome,autor):
    distrib={}
    for pub in fnome:
        for autores in pub["authors"]:
            if autores["name"].strip(". ") == autor:
                if "publish_date" in pub:
                    data = pub["publish_date"].split("-")
                    ano=data[0]
                    if ano in distrib:
                        distrib[ano] = distrib[ano] +1
                    else:
                        distrib[ano]= 1
                else:
                    if "Sem data" not in distrib.keys():
                        distrib["Sem data"]=1
                    else:
                        distrib["Sem data"]= distrib["Sem data"]+1
    return distrib

def graficoDistrib_autor(fnome, autor):
    distrib = AutorporAno(fnome, autor)
    if not distrib:
        print(f"Não há publicações para o autor {autor}.")
        return
    anos = list(distrib.keys())  
    publicacoes = list(distrib.values())
    
    plt.bar(anos, publicacoes, color='c')
    plt.title(f"Distribuição de Publicações de {autor} por Ano", fontsize=14)
    plt.xlabel("Ano", fontsize=12)
    plt.ylabel("Número de Publicações", fontsize=12)
    plt.xticks(rotation=45)
    plt.show()

def help():
    print("""
    Carregar o dataset: Carrega o ficheiro que contém a base de dados, que pode ser encontrado escrevendo o seu nome
    Inserir Publicação: Insere uma nova publicação à base de dados, preenchendo os campos pedidos: os autores têm a opção de escrever a afiliação e orcid, na data tem de apresentar um certo formato,
          o resto dos campos apenas necessita de completar se quiser.
    Atualizar Publicação: O utilizador vai ter opurtonidade de preencher todos os campos, tendo em atenção que a data apresenta um formato específico, autores apenas podem ser adicionados, 
          o resto dos campos é substituído pelo que for escrito.
    Consultar Publicações: Abre um sub menu onde pode escolher os filtros pelos quais quer consultar as publicações, tendo em conta que os resultados estarão ordenados por título.
    Análise de publicações por Autor: Dá como resultado a lista de autores da base de dados ordenada alfabeticamente, de seguida poderemos introduzir o nome do autor, 
          recebendo uma lista dos títulos das publicações do mesmo. Por último poderemos introduzir o título que quisermos e obteremos a publicação inteira
    Análise de publicações por palavras-chave: Dá como resultado a lista de palavras-chave da base de dados, onde podemos ordená-las por ocorrência ou alfabeticamente.
          De seguida poderemos introduzir o nome de uma palavra-chave e será nos dado uma lista com os títulos associados a essa palavra-chave.
    Estatísticas da publicação: Irá abrir um sub menu onde pode escolher o gráfico que deseja, dentro dos disponíveis
    Importar Dados: permite carregar um ficheiro que contém outra base de dados, adicionando-o à nossa base de dados inicial
    Listar Autores: Permite receber um dicionário com todos os autores seguidos das suas publicações.
    Apagar Publicação: Permite apagar uma publicação da base de dados sendo apenas necessário fornecer o título da publicação a eliminar.
    Sair: Fecha a aplicação, guardando as alterações feitas na base de dados
    Nota: Nas ações "Análise de publicações por Autor", "Análise de publicações por palavras-chave" e "Consultar Publicações" é possível exportar os resultados para um ficheiro
    """)
    return

def menuestatistica(ata):
    cond=True
    while cond:
        menu2 = """
    (1) Distribuição de publicações por ano.
    (2) Número de publicações por autor (top 20 autores).
    (3) Distribuição de palavras-chave pela sua frequência (top 20 palavras-chave).
    (4) Distribuição de palavras-chave mais frequente por ano.
    (5) Distribuição de publicações de um autor por anos
    (0) Sair do submenu
    """
        print(menu2)

        op = input("Introduza uma opção: ")
        if op == "1":
            print(graficoPub_Ano(ata))
        elif op == "2":
            print(graficoPostAutor(ata))
        elif op == "3":
            print(graficoFreq_keyw(ata))
        elif op == "4":
            ano = input("Introduza o ano que quer visualizar:")
            graficoFreq_keyw_ano(ata, str(ano))  
        elif op == "5":
            autor = input("Introduza o autor:")
            print(graficoDistrib_autor(ata, autor))
        elif op == "0":
            print("A sair do submenu estatísticas.")
            cond=False
        else:
            print("Opção inválida! Por favor tente novamente.")

def menuconsulta(ata):       
    cond=True
    while cond:
        menu1 = """
    (0) Sair do menu consulta
    (1) Consultar por título
    (2) Consultar por palavras-chave
    (3) Consultar por autor
    (4) Consultar por data de publicação
    (5) Consultar por afiliação
    """
        print(menu1)

        op = input("Introduza uma opção: ")
        if op == "1":
            titulo = input("Introduza o título da publicação: ")
            pesquisa = consultarRegisto_titulo(ata, titulo)
            print(pesquisa)
            exportar(pesquisa, "")
            
        elif op == "2":
            keywords = input("Introduza as palavras-chave da publicação: ")
            pesquisa = ordenaportitulo(consultarRegisto_palavras(ata, keywords))
            print(pesquisa)
            exportar(pesquisa, "")
                    
        elif op == "3":
            autor = input("Introduza o nome do autor: ")
            pesquisa = ordenaportitulo(consultarRegisto_autor(ata, autor))
            print(pesquisa)
            exportar(pesquisa, "")

        elif op == "4":
            publish_date = input("Introduza a data de publicação (YYYY-MM-DD): ")
            pesquisa = ordenaportitulo(consultarRegisto_data(ata, publish_date))
            print(pesquisa)
            exportar(pesquisa, "")

        elif op == "5":
            afiliacao = input("Introduza a afiliação do autor: ")
            pesquisa = ordenaportitulo(consultarRegisto_afiliacao(ata, afiliacao))
            print(pesquisa)
            exportar(pesquisa, "")
        
        elif op == "0":
            print("A sair do menu de consulta.")
            cond=False
        else:
            print("Opção inválida! Por favor tente novamente.")

def menu():
    print("""
(1) Carregar o dataset
(2) Inserir publicação
(3) Atualizar publicação
(4) Consultar publicação
(5) Análise de publicações por Autor
(6) Análise de publicações por palavras-chave
(7) Estatísticas da publicação
(8) Apagar publicação
(9) Listar Autores
(10) Importar Dados
(11) Help
(0) Sair
""")

ata = [] 
sair = True 

while sair:
    menu()
    op = input("Introduza uma opção: ").strip()

    if op == "1":
        fnome = input("Introduza o nome do ficheiro que quer carregar: ").strip()
        ata = carregarFicheiro(fnome)
        print("Ficheiro carregado com sucesso!")

    elif op == "2":
        inserirRegisto(ata)

    elif op == "3":
        atualizarPublicacao(ata)

    elif op == "4":
        menuconsulta(ata)

    elif op == "5":
        print(listarAutor(ata))
        autor = input("Introduza o nome do autor: ").strip()
        print(postAutor(ata, autor))
        title1 = input("Introduza o título do artigo: ").strip()
        busca = buscaporTitulo(ata, title1)
        print(busca)
        exportar(busca, "")

    elif op == "6":
        listar_Keyw(ata)
        ordena = input("Deseja ordenar as palavras-chave por ordem alfabética ou por ocorrência? Escreva 'a' para alfabético ou 'o' para ocorrência: ").lower().strip()
        if ordena == "a":
            print(ordena_Keyw_alfa(ata))
        elif ordena == "o":
            print(ordena_Keyw_ocor(ata))
        else:
            print("Opção inválida! Por favor, tente novamente.")
        key_w = input("Diga qual palavra-chave quer aceder: ").strip().lower()
        busca = post_keyw(ata, key_w)
        print(busca)
        exportar(busca, "")

    elif op == "7":
        menuestatistica(ata)

    elif op == "8":
        title = input("Introduza o título da publicação que quer eliminar: ").strip()
        eliminar(ata, title)

    elif op == "9":
        print(listar_autor_pub(ata))

    elif op == "10":
        fnome1 = input("Introduza o nome do ficheiro que quer importar: ").strip()
        import_dados(fnome1, ata)
    
    elif op == "11":
        print(help())

    elif op == "0":
        salvar = input("Deseja salvar os dados antes de sair? Responda 's' ou 'n': ").lower().strip()
        if salvar == "s":
            fnome = input("Introduza o nome do ficheiro onde deseja salvar os dados: ").strip()
            salvar_dados(fnome, ata)
            print("Os dados foram guardados com sucesso!")
        print("Saindo do programa. Até mais!")
        sair = False  

    else:
        print("Opção inválida! Por favor, tente novamente.")



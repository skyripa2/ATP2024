import json
import matplotlib.pyplot as plt

def carregar_base_dados_arquivo(fnome):
    f = open("./" + fnome, encoding='utf-8')
    ata = json.load(f)
    f.close()
    return ata

data_set=carregar_base_dados_arquivo("ata_medica_papers.json")

def listarAutor(fnome):#
    res =[]
    for d in fnome:
        for autor in d['authors']:
            if autor['name'] not in res:   
                res.append(autor['name'])
    res.sort()
    return res

def postAutor(fnome, autor):#
    posts=[]
    for d in fnome:
        for aut in d['authors']:
            if aut['name']== autor: 
                posts.append(d['title'])

    return posts


def postsPorAutor(fnome):
    dis= {}
    for d in fnome:
        for aut in d['authors']:
            if aut['name'] in dis:
                dis[aut['name']]=dis[aut['name']]+1
            else:
                dis[aut['name']]=1
    return dis

def ordenaAutor(fnome):
    posts_autor=postsPorAutor(fnome)
    ordena= sorted(posts_autor.items(), key=lambda item: item[1], reverse=True)
    return ordena[:20]

def graficoPostAutor(fnome):#

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

def ordena_Keyw_alfa(fnome):#
    dis_keywords=listar_Keyw(fnome)
    dic_ordenada=sorted(dis_keywords)
    return dic_ordenada

def post_keyw(fnome, key_w):#
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


def graficoPub_Ano(fnome):#

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

def graficoFreq_keyw(fnome):#

    freq_keyw=ordena_Keyw_ocor_top20(fnome)
    keyw= [keyw[0] for keyw in freq_keyw ]
    contagem = [keyw[1] for keyw in freq_keyw]

    plt.bar(keyw, contagem, color="c")
    plt.xticks(rotation=45, ha='right')
    plt.xlabel("Palavras-chave")
    plt.ylabel("Frequência de aparição")
    plt.title("Distribução de palavras-chave pela sua frequência")
    plt.show()
    return

def salvar_dados(fnome, dataset):
    f= open(fnome, 'w')
    json.dump(dataset, f, indent=4)
    f.close()
    return


    
def consultarRegisto_titulo(fnome,titulo):#
    res = []
    for dicionario in fnome:
        if 'title' in dicionario and dicionario['title'] == titulo:
            res.append(dicionario)
    return res

def consultarRegisto_palavras(fnome, keywords):#
    res = []
    for pub in fnome:
        if 'keywords' in pub:
            keyword_lista = pub['keywords'].split(", ")
            keywords_normalizadas = []
            for k in keyword_lista:
                keywords_normalizadas.append(k.strip().lower())
            if keywords.lower() in keywords_normalizadas:
                res.append(pub)
    if not res:
        print("Não foram encontradas publicações com essa palavra-chave.")
    return res

def consultarRegisto_data(fnome, publish_date):#
    res = []
    for pub in fnome:
        if 'publish_date' in pub and pub['publish_date'] == publish_date:
            res.append(pub)
    
    if not res:
        print("Não foram encontradas publicações para essa data de publicação.")
    return res

def consultarRegisto_autor(fnome, autor):#
    res = []
    for pub in fnome:
        if 'authors' in pub:
            for aut in pub['authors']:
                if autor == aut['name']:
                    res.append(pub)
    if not res:
        print("Não foram encontradas publicações com esses autores.")
    return res


def consultarRegisto_afiliacao(fnome, afiliacao):#
    res = []
    for pub in fnome:
        for aut in pub['authors']:
            if 'affiliation' in aut and afiliacao in aut['affiliation'].strip(".").split(". "):
                res.append(pub)
    if not res:
        print("Não foram encontradas publicações com esses autores.")
    return res

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

def graficoFreq_keyw_ano(fnome,ano):#

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

def ordenarpordata(res):
    return sorted(res, key=lambda pub: pub['publish_date'])

def ordenaportitulo(res):
    return sorted(res, key=lambda pub: pub['title'])

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

def graficoDistrib_autor(fnome, autor):#
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

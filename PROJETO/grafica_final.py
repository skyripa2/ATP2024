import FreeSimpleGUI as sg
import projeto as pr
import json
import matplotlib.pyplot as plt  


def carregar_base_dados_arquivo(fnome):
    f = open("./" + fnome, encoding='utf-8')
    ata = json.load(f)
    f.close()
    return ata

def exportar(resultados, nome_arquivo="resultados.json"):
    if not resultados:
        sg.popup("Nenhum resultado para exportar.", title="Erro")
        return

    layout_exportar = [
        [sg.Text("Digite o nome do arquivo para exportar:", font=("Helvetica", 12))],
        [sg.Text("Nome do Arquivo:"), sg.InputText(key="nome_arquivo", default_text=nome_arquivo)],
        [sg.Button("Exportar"), sg.Button("Cancelar", button_color=("white", "red"))]
    ]

    window_exportar = sg.Window("Exportar Resultados", layout_exportar)
    stop_exportar = True
    while stop_exportar:
        event_exportar, values_exportar = window_exportar.read()
        if event_exportar == sg.WINDOW_CLOSED or event_exportar == "Cancelar":
            window_exportar.close()
            stop_exportar = False
        elif event_exportar == "Exportar":
            nome_arquivo = values_exportar["nome_arquivo"]
            if nome_arquivo:
                file = open(nome_arquivo, "w", encoding="utf-8")
                json.dump(resultados, file, ensure_ascii=False, indent=4)
                file.close()
                sg.popup(f"Resultados exportados com sucesso para {nome_arquivo}.", title="Sucesso")
                window_exportar.close()
                stop_exportar = False

def salvarAta(fnome, ata):
    file = open("./" + fnome, "w", encoding="utf-8")
    json.dump(ata, file, ensure_ascii= False, indent = 4)
    file.close()

def import_dados(fnome, ata):
    f = open("./" + fnome, encoding='utf-8')
    novos_dados= json.load(f)
    ata.append(novos_dados)
    f.close()
    return ata

def menu_atualizar_publicacao(ata):
    layout_atualizar = [
        [sg.Text("Atualizar Publicação", font=("Helvetica", 14))],
        [sg.Text("Digite o título da publicação a ser atualizada:")],
        [sg.InputText(key="titulo_atualizar")],
        [sg.Button("Procurar"), sg.Button("Cancelar", button_color=("white", "red"))]
    ]

    window_atualizar = sg.Window("Atualizar Publicação", layout_atualizar)
    continuar_atualizando = True

    while continuar_atualizando:
        event_atualizar, values_atualizar = window_atualizar.read()

        if event_atualizar == sg.WINDOW_CLOSED or event_atualizar == "Cancelar":
            continuar_atualizando = False

        elif event_atualizar == "Procurar":
            titulo_atualizar = values_atualizar["titulo_atualizar"]
            publicacao_encontrada = None
            i = 0

            while i < len(ata) and publicacao_encontrada is None:
                if ata[i].get("title") == titulo_atualizar:
                    publicacao_encontrada = ata[i]
                i += 1

            if publicacao_encontrada:
                autores_text = "\n".join([
                    f"{autor['name']} - {autor.get('affiliation', 'Sem Afiliação')} - {autor.get('orcid', 'Sem ORCID')}" 
                    for autor in publicacao_encontrada["authors"]
                ])

                keywords_text = ", ".join(publicacao_encontrada.get("keywords", [])) if isinstance(publicacao_encontrada.get("keywords", []), list) else publicacao_encontrada.get("keywords", "")
                doi_text = publicacao_encontrada.get("doi", "")
                pdf_text = publicacao_encontrada.get("pdf", "")
                url_text = publicacao_encontrada.get("url", "")
                publish_date_text = publicacao_encontrada.get("publish_date", "")

                layout_editar = [
                    [sg.Text("Editar Publicação", font=("Helvetica", 14))],
                    [sg.Text("Título:"), sg.InputText(default_text=publicacao_encontrada["title"], key="title", size=(60, 1), disabled = True)],
                    [sg.Text("Resumo:"), sg.Multiline(default_text=publicacao_encontrada["abstract"], key="abstract", size=(80, 10))],
                    [sg.Text("Palavras-chave:"), sg.InputText(default_text=keywords_text, key="keywords", size=(60, 1))],
                    [sg.Text("Autores (Nome - Afiliação - ORCID):")],
                    [sg.Multiline(default_text=autores_text, key="authors", size=(70, 10))],
                    [sg.Text("DOI:"), sg.InputText(default_text=doi_text, key="doi", size=(60, 1))],
                    [sg.Text("PDF:"), sg.InputText(default_text=pdf_text, key="pdf", size=(60, 1))],
                    [sg.Text("Data de Publicação:"), sg.InputText(default_text=publish_date_text, key="publish_date", size=(60, 1))],
                    [sg.Text("URL:"), sg.InputText(default_text=url_text, key="url", size=(60, 1))],
                    [sg.Button("Salvar"), sg.Button("Cancelar", button_color=("white", "red"))]
                ]

                window_editar = sg.Window("Editar Publicação", layout_editar, size=(900, 600))
                continuar_editando = True

                while continuar_editando:
                    event_editar, values_editar = window_editar.read()

                    if event_editar == sg.WINDOW_CLOSED or event_editar == "Cancelar":
                        continuar_editando = False

                    elif event_editar == "Salvar":
                        publicacao_encontrada["title"] = values_editar["title"]
                        publicacao_encontrada["abstract"] = values_editar["abstract"]
                        publicacao_encontrada["keywords"] = [keyword.strip() for keyword in values_editar["keywords"].split(",") if keyword.strip()]
                        publicacao_encontrada["doi"] = values_editar["doi"].strip() if values_editar["doi"].strip() else None
                        publicacao_encontrada["pdf"] = values_editar["pdf"].strip() if values_editar["pdf"].strip() else None
                        publicacao_encontrada["url"] = values_editar["url"].strip() if values_editar["url"].strip() else None
                        publish_date = values_editar["publish_date"].strip()
                        publicacao_encontrada["publish_date"] = publish_date if publish_date else None

                        autores = values_editar["authors"].split("\n")
                        autores_processados = []
                        for autor in autores:
                            partes = autor.split(" - ")
                            autor_dict = {"name": partes[0]}
                            if len(partes) > 1:
                                autor_dict["affiliation"] = partes[1]
                            if len(partes) > 2:
                                autor_dict["orcid"] = partes[2]
                            autores_processados.append(autor_dict)

                        publicacao_encontrada["authors"] = autores_processados

                        sg.popup("Publicação atualizada com sucesso!", title="Sucesso")
                        continuar_editando = False

                window_editar.close()
            else:
                sg.popup("Publicação não encontrada.", title="Erro")

    window_atualizar.close()

def consulta_por_titulo(ata, window):
    layout_titulo = [[sg.Text('Digite o título:'), sg.Input(key='-TITULO-')],
                     [sg.Radio("Ordenar por Título", "ORDENAR", key="ORD_TITULO", default=True), 
                      sg.Radio("Ordenar por Data", "ORDENAR", key="ORD_DATA")],
                     [sg.Button('Procurar'), sg.Button('Voltar', button_color=("white", "red"))]]
    window_titulo = sg.Window('Consultar por Título', layout_titulo)
    stop3 = True
    while stop3:
        event_titulo, values_titulo = window_titulo.read()
        if event_titulo == sg.WINDOW_CLOSED or event_titulo == 'Voltar':
            window_titulo.close()
            stop3=False
        if event_titulo == 'Procurar':
            titulo = values_titulo['-TITULO-']
            res = pr.consultarRegisto_titulo(ata, titulo)

            if values_titulo["ORD_TITULO"]:
                res = ordenar_por_titulo(res)
            elif values_titulo["ORD_DATA"]:
                res = ordenar_por_data(res)

            window['-RESULT-'].update([pub["title"] for pub in res])
            window_titulo.close()

def consulta_por_palavra_chave(ata, window):
    layout_keyword = [[sg.Text('Digite a palavra-chave:'), sg.Input(key='-KEYWORD-')],
                      [sg.Radio("Ordenar por Título", "ORDENAR", key="ORD_TITULO", default=True), 
                       sg.Radio("Ordenar por Data", "ORDENAR", key="ORD_DATA")],
                      [sg.Button('Procurar'), sg.Button('Voltar', button_color=("white", "red"))]]
    window_keyword = sg.Window('Consultar por Palavra-chave', layout_keyword)
    
    stop4=True
    while stop4:
        event_keyword, values_keyword = window_keyword.read()
        if event_keyword == sg.WINDOW_CLOSED or event_keyword == 'Voltar':
            window_keyword.close()
            stop4=False
        if event_keyword == 'Procurar':
            keyword = values_keyword['-KEYWORD-']
            res = pr.consultarRegisto_palavras(ata, keyword)

            if values_keyword["ORD_TITULO"]:
                res = ordenar_por_titulo(res)
            elif values_keyword["ORD_DATA"]:
                res = ordenar_por_data(res)

            window['-RESULT-'].update([pub["title"] for pub in res])
            window_keyword.close()

def consulta_por_data(ata, window):
    layout_data = [[sg.Text('Digite a data (YYYY-MM-DD):'), sg.InputText('', key='-DATA-', size=(10, 1)), sg.CalendarButton("Selecionar Data", target="-DATA-", format="%Y-%m-%d")],
                   [sg.Radio("Ordenar por Título", "ORDENAR", key="ORD_TITULO", default=True), 
                    sg.Radio("Ordenar por Data", "ORDENAR", key="ORD_DATA")],
                   [sg.Button('Procurar'), sg.Button('Voltar', button_color=("white", "red"))]]
    window_data = sg.Window('Consultar por Data', layout_data)
    stop5 = True
    while stop5:
        event_data, values_data = window_data.read()
        if event_data == sg.WINDOW_CLOSED or event_data == 'Voltar':
            window_data.close()
            stop5=False
        if event_data == 'Procurar':
            data = values_data['-DATA-']
            res = pr.consultarRegisto_data(ata, data)

            if values_data["ORD_TITULO"]:
                res = ordenar_por_titulo(res)
            elif values_data["ORD_DATA"]:
                res = ordenar_por_data(res)
            
            window['-RESULT-'].update([pub["title"] for pub in res])
            window_data.close()

def consulta_por_autor(ata, window):
    layout_autor = [[sg.Text('Digite o nome do autor:'), sg.Input(key='-AUTOR-')],
                    [sg.Radio("Ordenar por Título", "ORDENAR", key="ORD_TITULO", default=True), 
                     sg.Radio("Ordenar por Data", "ORDENAR", key="ORD_DATA")],
                    [sg.Button('Procurar'), sg.Button('Voltar', button_color=("white", "red"))]]
    window_autor = sg.Window('Consultar por Autor', layout_autor)

    stop6=True
    while stop6:
        event_autor, values_autor = window_autor.read()
        if event_autor == sg.WINDOW_CLOSED or event_autor == 'Voltar':
            window_autor.close()
            stop6=False
        if event_autor == 'Procurar':
            autor = values_autor['-AUTOR-']
            res = pr.consultarRegisto_autor(ata, autor)

            if values_autor["ORD_TITULO"]:
                res = ordenar_por_titulo(res)
            elif values_autor["ORD_DATA"]:
                res = ordenar_por_data(res)

            window['-RESULT-'].update([pub["title"] for pub in res])
            window_autor.close()

def consulta_por_afiliacao(ata, window):
    layout_afiliacao = [[sg.Text('Digite a afiliação:'), sg.Input(key='-AFILIACAO-')],
                       [sg.Radio("Ordenar por Título", "ORDENAR", key="ORD_TITULO", default=True), 
                        sg.Radio("Ordenar por Data", "ORDENAR", key="ORD_DATA")],
                       [sg.Button('Procurar'), sg.Button('Voltar', button_color=("white", "red"))]]
    window_afiliacao = sg.Window('Consultar por Afiliação', layout_afiliacao)

    stop7 = True
    while stop7:
        event_afiliacao, values_afiliacao = window_afiliacao.read()
        if event_afiliacao == sg.WINDOW_CLOSED or event_afiliacao == 'Voltar':
            window_afiliacao.close()
            stop7=False
        if event_afiliacao == 'Procurar':
            afiliacao = values_afiliacao['-AFILIACAO-']
            res = pr.consultarRegisto_afiliacao(ata, afiliacao)
            
            if values_afiliacao["ORD_TITULO"]:
                res = ordenar_por_titulo(res)
            elif values_afiliacao["ORD_DATA"]:
                res = ordenar_por_data(res)

            window['-RESULT-'].update([pub["title"] for pub in res])
            window_afiliacao.close()

def ordenar_por_data(res):
    return sorted(res, key=lambda pub: pub.get('date', ''))


def ordenar_por_titulo(res):
    return sorted(res, key=lambda pub: pub.get('title', '').lower())

def mostrar_publicacao_popup(publicacao):
    publicacao_formatada = json.dumps(publicacao, indent=4, ensure_ascii=False)
    sg.popup_scrolled(publicacao_formatada, title="Informações da Publicação", size=(80, 20))

def menu_visualizar_autores(ata):
    autores = pr.listarAutor(ata)

    layout = [
        [sg.Text("Lista de Autores", font=("Helvetica", 14))],
        [sg.Listbox(values=autores, size=(50, 20), key="-AUTORES-", enable_events=True)],
        [sg.Text("Publicações associadas:")],
        [sg.Listbox(values=[], size=(50, 20), key="-TITULOS-")],
        [sg.Button("Ver Publicação"), sg.Button("Exportar"), sg.Button("Voltar", button_color=("white", "red"))]
    ]

    window_autor = sg.Window("Visualizar Autores", layout)

    stop8=True
    while stop8:
        event_autor, values_autor = window_autor.read()

        if event_autor == sg.WINDOW_CLOSED or event_autor == "Voltar":
            stop8=False

        elif event_autor == "-AUTORES-" and values_autor["-AUTORES-"]:
            autor_selecionado = values_autor["-AUTORES-"][0]
            titulos = pr.postAutor(ata, autor_selecionado)
            window_autor["-TITULOS-"].update(titulos)

        elif event_autor == 'Ver Publicação':
            selecionada = values_autor['-TITULOS-']
            if selecionada:
                publicacao = None
                i = 0 
                while i < len(ata) and publicacao is None: 
                    if "title" in ata[i] and ata[i]["title"].strip().lower() == selecionada[0].strip().lower():  
                        publicacao = ata[i]  
                    i = i + 1  
        
                if publicacao:
                    mostrar_publicacao_popup(publicacao)
                else:
                    sg.popup("Publicação não encontrada!", title="Erro")
            else:
                sg.popup("Selecione uma publicação primeiro!", title="Erro")

        elif event_autor == "Exportar":
            if values_autor["-AUTORES-"]:
                autor_selecionado = values_autor["-AUTORES-"][0] 
        
                publicacoes_associadas = []
                i = 0  
                while i < len(ata): 
                    publicacao = ata[i] 
            
                    if 'authors' in publicacao: 
                        j = 0  
                        while j < len(publicacao['authors']):  
                            autor = publicacao['authors'][j]
                            if autor['name'].strip().lower() == autor_selecionado.strip().lower(): 
                                publicacoes_associadas.append(publicacao)  
                            j += 1 
            
                    i = i + 1   

                if publicacoes_associadas:
                    exportar(publicacoes_associadas) 
                else:
                    sg.popup("Não há publicações associadas ao autor selecionado.", title="Erro")
            else:
                sg.popup("Selecione um autor primeiro!", title="Erro")
    window_autor.close()


    
def menu_listar_palavras_chave(ata):
    layout = [
        [sg.Text("Ordenar palavras-chave por:"), 
         sg.Radio("Ocorrência", "ORDENAR", key="OCCURRENCE", default=True), 
         sg.Radio("Alfabética", "ORDENAR", key="ALPHABETICAL")],
        [sg.Button("Atualizar Lista")],
        [sg.Listbox(values=[], size=(50, 20), key="KEYWORDS", enable_events=True)],
        [sg.Text("Publicações associadas:")],
        [sg.Listbox(values=[], size=(50, 20), key="POSTS")],
        [sg.Button("Ver Publicação"), sg.Button("Exportar"), sg.Button("Voltar", button_color=("white", "red"))]
    ]

    window = sg.Window("Lista de Palavras-Chave", layout)

    stop_ = True
    while stop_:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Voltar":
            stop_ = False

        elif event == "Atualizar Lista":
            if values["OCCURRENCE"]:
                keywords = pr.ordena_Keyw_ocor(ata)
                window["KEYWORDS"].update([f"{k[0]}" for k in keywords])
            elif values["ALPHABETICAL"]:
                keywords = pr.ordena_Keyw_alfa(ata)
                window["KEYWORDS"].update(keywords)

        elif event == "KEYWORDS" and values["KEYWORDS"]:
            keyw = values["KEYWORDS"][0]
            posts = pr.post_keyw(ata, keyw)
            window["POSTS"].update(posts)

        elif event == 'Ver Publicação':
            selecionada = values['POSTS']
            if selecionada:
                publicacao = None
                i = 0
                while i < len(ata) and publicacao is None:  
                    if ata[i]["title"] == selecionada[0]:
                        publicacao = ata[i]  
                    i += 1  

                if publicacao:
                    mostrar_publicacao_popup(publicacao)
                else:
                    sg.popup("Publicação não encontrada!", title="Erro")
            else:
                sg.popup("Selecione uma publicação primeiro!", title="Erro")

        elif event == "Exportar":
            if values["KEYWORDS"]:
                keyw = values["KEYWORDS"][0]  
                posts = pr.post_keyw(ata, keyw) 

                if posts:  
                    resultados = posts  
                    exportar(resultados)  
                else:
                    sg.popup("Não há publicações associadas a essa palavra-chave.", title="Erro")
            else:
                sg.popup("Selecione uma palavra-chave primeiro!", title="Erro")

    window.close()

def menu_graficos(ata):
    layout = [
        [sg.Text("Selecione uma ação:")],
        [sg.Button("Distribuição de publicações por ano")],
        [sg.Button("Número de publicações por autor (top 20 autores)")],
        [sg.Button("Distribuição de palavras-chave pela sua frequência (top 20 palavras-chave)")],
        [sg.Button("Distribuição de palavras-chave mais frequente por ano")],
        [sg.Button("Distribuição de publicações de um autor por ano")],
        [sg.Button("Sair", button_color=("white", "red"))]
    ]

    window = sg.Window("Menu de Gráficos", layout)
    stop_1 = True
    while stop_1:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Sair":
            stop_1 = False

        elif event == "Distribuição de publicações por ano":
            pr.graficoPub_Ano(ata)

        elif event == "Número de publicações por autor (top 20 autores)":
            pr.graficoPostAutor(ata)

        elif event == "Distribuição de palavras-chave pela sua frequência (top 20 palavras-chave)":
            pr.graficoFreq_keyw(ata)
        
        elif event == "Distribuição de palavras-chave mais frequente por ano":
            
            layout_ano =[
                [sg.Text("Insira o ano que quer visualizar:"), sg.Input(key='-ANO-') ],
                [sg.Button("OK"), sg.Button("Cancelar", button_color=("white", "red"))]
            ]
            window_ano = sg.Window("Escolha do ano", layout_ano)
            stop_2 = True
            while stop_2:
                event_ano, values_ano = window_ano.read()

                if event_ano == sg.WINDOW_CLOSED or event_ano == "Cancelar":
                    stop_2 = False
                    window_ano.close()
                
                elif event_ano  == "OK":
                    ano_input = values_ano['-ANO-']
                    if ano_input.isdigit():
                        ano = int(ano_input)

                        if 1999 <= ano <= 2024:
                            pr.graficoFreq_keyw_ano(ata, str(ano))  
                            stop_2 = False
                            window_ano.close()
                        else:
                            sg.popup("Ano inválido. Por favor, insira um ano entre 1900 e 2024.", title="Erro")
                    else:
                        sg.popup("Por favor, insira um ano válido.", title="Erro")
        elif event == "Distribuição de publicações de um autor por ano":
            layout_autor = [
                [sg.Text("Insira o nome do autor que quer visualizar:"), sg.Input(key='-AUTOR-')],
                [sg.Button("OK"), sg.Button("Cancelar", button_color=("white", "red"))]
            ]
            window_autor = sg.Window("Escolha do autor", layout_autor)
            stop_3 = True
            while stop_3:
                event_autor, values_autor = window_autor.read()

                if event_autor == sg.WINDOW_CLOSED or event_autor == "Cancelar":
                    stop_3 = False
                    window_autor.close()
                
                elif event_autor == "OK":
                    autor = values_autor['-AUTOR-'].strip()
                    if autor:
                        pr.graficoDistrib_autor(ata, autor)
                        stop_3 = False
                        window_autor.close()
                    else:
                        sg.popup("Por favor, insira um nome de autor válido.", title="Erro")

    window.close()

custom_theme = {
    'BACKGROUND': '#000080',
    'TEXT': '#FFFFFF',
    'INPUT': '#F0F0F0',
    'TEXT_INPUT': '#000000',
    'SCROLL': '#FFFFFF',
    'BUTTON': ('#FFFFFF', '#007BFF'),
    'PROGRESS': ('#FFFFFF', '#007BFF'),
    'BORDER': 1,
    'SLIDER_DEPTH': 0,
    'PROGRESS_DEPTH': 0
}

sg.LOOK_AND_FEEL_TABLE['MeuTema'] = custom_theme
sg.theme('MeuTema')

layout1 = [
        [sg.Text("Sistema de Gestão de Publicações", font=("Helvetica", 16), justification="center", size=(50, 1))],
        [sg.HorizontalSeparator()],
        [sg.Button("Criar Publicação", size=(30, 1))],
        [sg.Button("Atualização de Publicações", size=(30,1))],
        [sg.HorizontalSeparator()],
        [sg.Button("Consultar Publicações", size=(30, 1))],
        [sg.Button("Visualizar Autores", size=(30, 1))],
        [sg.Button("Visualizar Palavras-Chave", size=(30, 1))],
        [sg.HorizontalSeparator()],
        [sg.Button("Gráficos", size=(30, 1))],
        [sg.Button("Importar Dados", size=(30, 1))],
        [sg.Button("Sair", size=(30, 1), button_color=("white", "red"))]
    ]

window_principal = sg.Window("Sistema de Gestão de Publicações", layout1)

ata = carregar_base_dados_arquivo("ata_medica_papers.json")
stop = True
while stop:
    event_principal, values_principal = window_principal.read()

    if event_principal == sg.WINDOW_CLOSED or event_principal == "Sair":
        resposta = sg.popup_yes_no("Deseja salvar as alterações antes de sair?", title="Salvar Dados")
        if resposta == "Yes":
                
            layout_salvar = [
                    [sg.Text("Digite o título do arquivo para salvar os dados:", font=("Helvetica", 12))],
                    [sg.Text("Título do Arquivo:"), sg.InputText(key="titulo_arquivo", default_text="dados.json")],
                    [sg.Button("Salvar"), sg.Button("Cancelar", button_color=("white", "red"))]
                ]

            window_salvar = sg.Window("Salvar Arquivo", layout_salvar)
            stop_salvar = True
            while stop_salvar:
                event_salvar, values_salvar = window_salvar.read()
                if event_salvar == sg.WINDOW_CLOSED or event_salvar == "Cancelar":
                    stop_salvar = False
                elif event_salvar == "Salvar":
                        
                    titulo_arquivo = values_salvar["titulo_arquivo"]
                    salvarAta(titulo_arquivo, ata)
                    sg.popup(f"Dados salvos com sucesso em {titulo_arquivo}!", title="Sucesso")
                    stop_salvar = False

            window_salvar.close()
        stop=False

    elif event_principal == "Importar Dados":  
        layout_importar = [
                [sg.Text("Importar Dados", font=("Helvetica", 14))],
                [sg.Text("Arquivo:"), sg.Input(key="arquivo_importar")],
                [sg.Button("Importar"), sg.Button("Cancelar", button_color=("white", "red"))]
            ]

        window_importar = sg.Window("Importar Dados", layout_importar)
        stop_importar = True
        while stop_importar:
            event_importar, values_importar = window_importar.read()
            if event_importar == sg.WINDOW_CLOSED or event_importar == "Cancelar":
                stop_importar = False
            elif event_importar == "Importar":
                ata = import_dados(values_importar["arquivo_importar"], ata)
                sg.popup("Dados importados com sucesso!")
                stop_importar = False

        window_importar.close()
        
    elif event_principal == "Atualização de Publicações":
            menu_atualizar_publicacao(ata)
        
    elif event_principal == "Criar Publicação":
            layout = [
        [sg.Text("Criar Nova Publicação", font=("Helvetica", 14))],
        [sg.Text("Título:"), sg.Input(key="-TITULO-")],
        [sg.Text("Autores:"), sg.Button("Adicionar Autor")],
        [sg.Listbox(values=[], size=(40, 5), key="-AUTORES-"), sg.Button("Remover Autor")],
        [sg.Text("Palavras-chave:"), sg.Button("Adicionar Palavra-chave")],
        [sg.Listbox(values=[], size=(40, 5), key="-KEYWORDS-"), sg.Button("Remover Palavra-chave")],
        [sg.Text("Data:"), sg.Input(key="-DATA-"), sg.CalendarButton("Selecionar Data", target="-DATA-", format="%Y-%m-%d")],
        [sg.Text("URL:"), sg.Input(key="-URL-")],
        [sg.Text("DOI:"), sg.Input(key="-DOI-")],
        [sg.Text("PDF:"), sg.Input(key = "-PDF-")],
        [sg.Text("Abstrato:")],
        [sg.Multiline(size=(50, 5), key="-ABSTRATO-")],
        [sg.Button("Salvar"), sg.Button("Cancelar", button_color=("white", "red"))]
    ]

            window_criar = sg.Window("Criar Publicação", layout)

            autores = []
            keywords = []
            stop_criar = True
            while stop_criar:
                event_criar, values_criar = window_criar.read()

                if event_criar == sg.WINDOW_CLOSED or event_criar == "Cancelar":
                    stop_criar = False

                elif event_criar == "Adicionar Autor":
                    nome = sg.popup_get_text("Nome do Autor:", title="Adicionar Autor")
                    if nome:
                        afiliacao = sg.popup_get_text(f"Afilição de {nome} (opcional):", title="Adicionar Afilição") or None
                        orcid = sg.popup_get_text(f"Orcid de {nome} (opcional):", title="Adicionar Orcid") or None
        
                    autor = {"name": nome}
                    if afiliacao:
                        autor["affiliation"] = afiliacao
                    if orcid:
                        autor["orcid"] = orcid
        
                    autores.append(autor)
        
                    autores_str = []
                    for a in autores:
                        autor_str = a["name"]
                        if "affiliation" in a:
                            autor_str += f" ({a['affiliation']})"
                        if "orcid" in a:
                            autor_str += f" ({a['orcid']})"
                        autores_str.append(autor_str)
        
                    window_criar["-AUTORES-"].update(autores_str)


                elif event_criar == "Remover Autor":
                    selecionados = values_criar["-AUTORES-"] 
                    if selecionados:
                        for sel in selecionados:
          
                            nome = sel.split(" (")[0] 
                            autores = [a for a in autores if a["name"] != nome] 

        
                        autores_str = []
                        for a in autores:
                            autor_str = a["name"]
                            if "affiliation" in a:
                                autor_str += f" ({a['affiliation']})"
                            if "orcid" in a:
                                autor_str += f" ({a['orcid']})"
                            autores_str.append(autor_str)
                        window_criar["-AUTORES-"].update(autores_str)

                elif event_criar == "Adicionar Palavra-chave":
                    keyword = sg.popup_get_text("Palavra-chave:", title="Adicionar Palavra-chave")
                    if keyword:
                        keywords.append(keyword)
                        window_criar["-KEYWORDS-"].update(keywords)

                elif event_criar == "Remover Palavra-chave":
                    selecionados = values_criar["-KEYWORDS-"]
                    if selecionados:
                        for sel in selecionados:
                            keywords.remove(sel)
                        window_criar["-KEYWORDS-"].update(keywords)

                elif event_criar == "Salvar":
                    titulo = values_criar["-TITULO-"]
                    data = values_criar["-DATA-"]
                    url = values_criar["-URL-"]
                    doi = values_criar["-DOI-"]
                    pdf = values_criar["-PDF-"]
                    abstrato = values_criar["-ABSTRATO-"].strip()

            
                    if not titulo or not autores or not data:
                        sg.popup("Por favor, preencha os campos obrigatórios (Título, Autores, Data).", title="Erro")
                    else:
                
                        nova_publicacao = {
                    "title": titulo,
                    "authors": autores,
                    "keywords": keywords,
                    "publish_date": data,
                    "url": url.strip() if url else None,
                    "doi": doi.strip() if doi else None,
                    "pdf": pdf.strip() if pdf else None, 
                    "abstract": abstrato.strip() if abstrato else None
                }
                        ata.append(nova_publicacao)
                        sg.popup("Publicação criada com sucesso!", title="Sucesso")
                        stop_criar = False

            window_criar.close()

    elif event_principal == "Consultar Publicações":
        layout = [
        [sg.Text('Selecione a consulta desejada:')],
        [sg.Button('Consultar por Título')],
        [sg.Button('Consultar por Palavra-chave')],
        [sg.Button('Consultar por Data')],
        [sg.Button('Consultar por Autor')],
        [sg.Button('Consultar por Afiliação')],
        [sg.Text('Resultados:', size=(40, 1))],
        [sg.Listbox(values=[], size=(80, 20), key='-RESULT-', enable_events=True)],
        [sg.Button("Ver Publicação"), sg.Button('Exportar'), sg.Button('Sair', button_color=("white", "red"))]
    ]

        window_consultar = sg.Window('Sistema de Consultas', layout)
        stop2 = True
        while stop2:
            event, values = window_consultar.read()

            if event == sg.WINDOW_CLOSED or event == 'Sair':
                window_consultar.close()
                stop2=False

            elif event == 'Consultar por Título':
                consulta_por_titulo(ata, window_consultar)

            elif event == 'Consultar por Palavra-chave':
                consulta_por_palavra_chave(ata, window_consultar)

            elif event == 'Consultar por Data':
                consulta_por_data(ata, window_consultar)

            elif event == 'Consultar por Autor':
                consulta_por_autor(ata, window_consultar)

            elif event == 'Consultar por Afiliação':
                consulta_por_afiliacao(ata, window_consultar)

            elif event == 'Ver Publicação':
                selecionada = values['-RESULT-']
                if selecionada:
                    publicacao = None
                    i = 0 
                    while i < len(ata) and publicacao is None: 
                        if 'title' in ata[i] and ata[i]["title"] == selecionada[0]:  
                            publicacao = ata[i]  
                        i = i + 1 
        
                    if publicacao:
                        mostrar_publicacao_popup(publicacao)
                    else:
                        sg.popup("Publicação não encontrada!", title="Erro")
                else:
                    sg.popup("Selecione uma publicação primeiro!", title="Erro")
        
            elif event == 'Exportar':
                resultados = window_consultar['-RESULT-'].get_list_values()
                exportar(resultados)
        window_consultar.close()

    elif event_principal == "Visualizar Autores":
        menu_visualizar_autores(ata)

    elif event_principal == "Visualizar Palavras-Chave":
        menu_listar_palavras_chave(ata)

    elif event_principal == "Gráficos":
        menu_graficos(ata)

window_principal.close()

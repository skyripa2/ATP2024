
# Relatório do trabalho em Python sobre Consulta e Análise de Publicações Científicas

## Data: 2025-01-05
## Unidade Curricular: Algoritmos e Técnicas de Programação
## Docentes: José Carlos Ramalho e Luís Filipe Cunha
## Grupo 6: Daniela Faria (a107228), Tiago Maia (a107203) e Vera Campos (a107235)

Neste relatório iremos abordar o funcionameto das funções criadas e usadas no ficheiro "linha_comando.py", e "projeto.py" que são então importadas para o ficheiro "gráfica_final.py".
Por fim também iremaos colocar neste relatório a documentação detalhada de como utlizar o sistema.
Este projeto permite-nos fazer alterações, pesquisas, e análises de uma base de dados fornecino no nome de "ata_medica_papers.json".
Decidimos incorporar três ficheiros no desenvolvimento do projeto de forma a facilitar a interação entre as funções e a interface gráfica de forma a organizar e permitir uma melhor perceção do funcionamento do sistema.

### __1. Carregamento da base de dados__
-A função carregarFicheiro recebe um argumento: fnome, e tem como objetivo carregar o ficheiro da base de dados.
O arquivo é aberto com a codificação "utf-8" e o comando json.load(f) carrega o conteúdo do arquivo json fornecido.
Na linha de comando, o carregamento do ficheiro é realizado ao chamar a opção correta. 
Na Interface Gráfica o carregamento é feito automaticamente no início do programa.

### __2. Criação de Publicações__
-A função inserirRegisto tem como objetivo adicionar uma nova publicação a uma lista (ata) com os seguintes parâmetros: ata, authors, abstract, keywords, doi, pdf, publish_date, title, url, name, affiliation, orcid.
É criado um registo de publicação com informações como resumo, palavras-chave, autores, DOI, PDF, data de publicação, título e URL, tendo ainda em conta que o título e o autor são obrigatórios e que no campo data de publicação o programa só avançará se a data for indroduzida no formato correto.
Permite adicionar autores à lista de autores (authors), perguntando ao utilizador se ele deseja incluir novos autores.
Adiciona o registo criado (incluindo os autores) à lista de publicações (ata).
No final, retorna a lista atualizada contendo o novo registo.

### __3. Atualização de Publicações__ 

A função atualizarPublicacao tem como objetivo permitir que o utilizador consiga mudar, se quiser, os vários parâmetros de uma publicação.
Na execução desta função é pedido ao utilizador que forneça o título da publicação a atualizar. Se a publicação não for encontrada o programa irá exibir uma mensagem de erro. Se encontrar, vai pedir ao utilizador que preencha o que quer mudar da publicação inicial, sendo que o programa não avançará se a data não for colocada no formato correto ou deixar em branco se quiser avançar. Se o utilizador escrever palavras-chave separadas por vírgulas e espaço elas serão colocadas na publicação ao invés das antigas. Se o utilizador decidir preencher os autores terá a opção de adicionar afiliação e orcid. No final os autores são adicionados à lista de autores já existentes.
Os restantes parâmetros irão ser substituídos pelos novos.
No final de serem fornecidos os parâmetros novos, o sistema irá guardar a informação em formato dicionário igual ao da base de dados inicial.

### __4. Consulta de Publicações__
* **Por título**
- A função consultarRegisto_titulo recebe dois argumentos: fnome e titulo e tem como objetivo consultar um registo quando inserido um título.
Cria uma lista vazia res para armazenar os resultados.
Itera sobre cada dicionário em fnome.
Para cada dicionário, verifica se contém a chave 'title' e se o valor do título corresponde ao titulo fornecido.
Se encontrar uma correspondência, adiciona o dicionário à lista res.
No final, retorna a lista res, que contém todos os registos encontrados com o título especificado.

* **Por palavras-chave**
- A função consultarRegisto_palavras recebe dois argumentos: fnome e keywords e tem como objetivo consultar um registo quando inserida(s) palavras-chave.
Cria uma lista vazia res para armazenar os resultados.
Itera sobre cada publicação (pub) em fnome.
Para cada publicação, verifica se ela contém a chave 'keywords':
Se contiver, divide a string de palavras-chave (separadas por ",") numa lista chamada keyword_lista.
Cria uma nova lista keywords_normalizadas, onde cada palavra-chave é convertida para minúsculas e remove espaços extras.
Verifica se a palavra-chave fornecida (keywords) está na lista keywords_normalizadas.
Se sim, adiciona a publicação à lista res. Se não, imprime uma mensagem a dizer que não foram encontradas publicações com a palavra-chave.
No final, retorna a lista res, que contém todas as publicações que possuem a palavra-chave fornecida.

* **Por data**
- A função consultarRegisto_data recebe dois argumentos: fnome e publish_date e tem como objetivo consultar um registo quando inserida uma data.
Cria uma lista vazia res para armazenar os resultados.
Itera sobre cada publicação (pub) em fnome.
Para cada publicação, verifica se ela contém a chave 'publish_date' e se o valor dessa chave é igual à publish_date fornecida.
Se encontrar uma correspondência, adiciona a publicação à lista res. Se não, imprime uma mensagem a dizer que não foram encontradas publicações para a data fornecida.
Por fim, retorna a lista res, que contém todas as publicações com a data de publicação especificada.

* **Por autor**
- A função consultarRegisto_autor recebe dois argumentos: fnome e autor e tem como objetivo consultar o registo de um determinado autor.
Cria uma lista vazia res para armazenar os resultados.
Itera sobre cada publicação (pub) em fnome.
Para cada publicação, verifica se existe a chave 'authors'.
Se houver, itera sobre a lista de autores de cada publicação.
Para cada autor, verifica se o nome do autor (aut['name']) é igual ao nome fornecido (autor).
Se encontrar uma correspondência, adiciona a publicação à lista res. Se não, imprime uma mensagem a dizer que não foram encontradas publicações com o autor especificado.
No final, retorna a lista res, que contém todas as publicações com o autor fornecido.

* **Por afiliação**
- A função consultarRegisto_afiliacao recebe dois argumentos: fnome e afiliação e tem como objetivo consultar um registo inserindo uma determinada afiliação.
Cria uma lista vazia res para armazenar os resultados.
Itera sobre cada publicação (pub) em fnome.
Para cada publicação, itera sobre a lista de autores:
Verifica se o autor possui a chave 'affiliation'.
Se a afiliação do autor (após remover pontos finais e dividir por ".") contém o valor fornecido em afiliacao, a publicação é adicionada à lista res. Se nenhuma publicação for encontrada, imprime uma mensagem a dizer que não foram encontradas publicações com a afiliação fornecida.
No final, retorna a lista res, que contém todas as publicações com autores que possuem a afiliação fornecida.


### __5. Análise de publicações por autor__
#### **Listar autores**
-A função listarAutor tem como objetivo receber uma lista de registos e retornar uma lista ordenada contendo os nomes dos autores únicos presentes nos registos. 
O código itera sobre cada item em fnome.
Para cada registo, ele itera pela lista de autores no campo authors e antes de adicionar o nome do autor a res, verifica se o nome já está na lista.
A lista resultante é ordenada alfabeticamente e retornada.

#### **Análise de títulos de publicações por autor**
-A função postAutor tem como objetivo procurar todos os títulos de publicações em que um autor específico está listado.
O código itera sobre cada item em fnome.
Para cada publicação, ele itera sobre a lista de authors e verifica se o nome do autor corresponde ao argumento autor. Se o nome do autor for encontrado, o título da publicação é adicionado à lista posts.
Após a iteração, a função retorna a lista de títulos associados ao autor.


#### **Publicação**
O código da função buscaporTitulo procura retornar a publicação associado a um título específico de uma publicação.
Itera sobre os itens em fnome (que é uma lista de dicionários).
Verifica se o dicionário contém o título especificado em title. Se encontrar o título, adiciona a publicação à variável publicacao_encontrada e devolve-a no final.
Retorna a URL encontrada (caso exista) ou, se não encontrada, retorna None.


### __6. Análise de publicações por palavras-chave__
- A função listar_Keyw conta a frequência de palavras-chave numa lista de dicionários.
Cria um dicionário vazio dic para armazenar a contagem das palavras-chave e itera sobre cada publicação (d) em fnome.
Para cada publicação que contém a chave 'keywords', divide a string de palavras-chave (separadas por ",") e percorre cada palavra-chave.
Conta a frequência de cada palavra-chave:
Se a palavra-chave já estiver no dicionário, aumenta o seu contador. Se não, adiciona a palavra-chave ao dicionário com o valor inicial de 1.
Retorna o dicionário dic, que contém cada palavra-chave como chave e a sua frequência de ocorrência como valor.

- A função ordena_Keyw_ocor é utilizada para ordenar as palavras-chave por frequência de ocorrência.
Chama a função listar_Keyw(fnome) que converte o dicionário numa lista de tuplos (onde cada tuplo contém uma palavra-chave e sua contagem) usando o método.items().
Ordena a lista de tuplos com base na contagem (valor de cada tuplo) usando a função sorted(), especificando que a ordenação será feita pelo segundo elemento da tupla (a contagem), com o parâmetro key=lambda item: item[1]. Esta lista é então devolvida.

- A função ordena_Keyw_alfa é usada para ordenar alfabeticamente as palavras-chave extraídas de uma lista de dicionários. 
Chama a função listar_Keyw(fnome) e faz a conversão tal como na função anterior.
Ordena a lista de palavras-chave (não tendo em consideração as contagens) por ordem alfabética, usando a função sorted(). No fim, retorna a lista ordenada.

- A função post_keyw procura títulos de publicações associados a uma palavra-chave específica fornecida como argumento.
Itera sobre cada publicação (d) em fnome e, para cada uma, verifica se ela contém a chave 'keywords'.
Se a publicação tiver palavras-chave, a função divide a string de palavras-chave (presumivelmente separadas por ", ") e percorre cada palavra-chave, verificando se a palavra-chave (keyw.lower) é igual à palavra-chave fornecida (key_w.lower).
Se sim, adiciona o título da publicação (d['title']) à lista posts e devolve-a ordenada alfabeticamente.

### __7. Estatísticas de Publicação__

As funções graficoPub_Ano, graficoPostAutor, graficoFreq_keyw, graficoFreq_keyw_ano, graficoDistrib_autor têm como objetivo apresentar relatórios estatísticos de distribuições específicas. 
Cada um destes gráficos, utiliza funções que calculam as distribuições pedidas sendo elas: distrib_pub_ano, distrib_keyw_ano, AutorporAno, postsPorAutor, listar_Keyw. Todas estas funções iteram sobre cada dicionário numa lista e verificam se a chave necessária para cada distribuição existe no dicionário. De seguida, fazem a atualização da distribuição. Se a variável que queremos verificar já existe na distribuição aumenta a contagem. Se não, cria uma entrada nova na distribuição.
Existem apenas duas exceções que criam um campo para publicações sem data nas distribuições.
São ainda utilizadas funções de ordenação, sendo elas: ordena_Keyw_ocor_top20, ordena_Keyw_ocor_ano_top20, ordenaAutor, ordena_Ano_pub.
Todas as funções de ordenação recebem uma das funções da distribuição anteriores, específica para cada objetivo de ordenação. A ordenação é feita através da função sorted(), sendo sempre indicado o método de ordenação. 
Estas funções devolvem sempre listas de tuplos.
Com a exceção da função ordena_Ano_pub, todas as outras apresentam reverse=True dentro do sorted() e, por fim, são retirados os 20 primeiros termos.
Por último, cada gráfico recebe os resultados das ordenações e adiciona um elemento de cada tuplo em duas variáveis distintas. Estas variáveis são usadas para a crição do gráfico. Existe ainda a exceção do gráfico graficoDistrib_autor que recebe uma distribuição ao invés de uma lista ordenada e divide em duas variáveis utilizando a função list() para a criação da lista de tuplos e das funções .keys() e .values() de forma a separar os elementos dos tuplos pelas variáveis.
De seguida, cria um gráfico de barras com o matplotlib, como mostrado no exemplo a seguir:
plt.bar(data, contagem, color="c"): Cria um gráfico de barras, onde os anos (data) estão no eixo X e a quantidade de publicações (contagem) no eixo Y. O parâmetro color="c" define a cor das barras.
Configurações adicionais:
plt.xticks(rotation=45, ha='right'): Roda as etiquetas do eixo X para 45 graus para melhor visualização e alinha as etiquetas à direita.
plt.xlabel("Anos"): Define o rótulo para o eixo X.
plt.ylabel("Nº de publicações"): Define o rótulo para o eixo Y.
plt.title("Distribuição de publicações por ano"): Define o título do gráfico.
Exibe o gráfico com plt.show().

### __8. Armazenamento dos dados__

A função salvar_dados é projetada para receber dois argumentos: fnome e ata. 
O arquivo é aberto no modo de escrita ("w") com a codificação "utf-8".
O comando json.dump(ata, file) grava o conteúdo de ata no arquivo no formato JSON. O uso de file.close() garante que o arquivo seja fechado após a escrita. 
Esta função permitirá, então, criar um ficheiro em que os dados apareçam exatamente no mesmo formato que os da base de dados inicial permitindo assim o seu uso futuro nestas aplicações e a sua consulta futura.

### __9. Importação de dados__

A função import_dados importa dados de um arquivo JSON e adiciona-os à lista previamente carregada. Esta função é semelhante à função carregar apenas diferindo na adição de elementos.
O arquivo é aberto com a codificação "utf-8" e o comando json.load(f) carrega o conteúdo do arquivo json. 
No final o conteúdo é adicionado à base de dados inicial através da utilização da funcionalidade append()


### __10. Exportação parcial de dados__

A função exportar recebe o resultado de uma pesquisa e o nome do ficheiro a ser criado. Funciona de uma forma semelhante à salvarAta.
O resultado da pesquisa é colocado numa lista que é então escrita num ficheiro através do json.dump() deixando o produto exportado de forma correta e semelhante à base de dados inicial.
No menu de linha de comando a função está implementada no menuconsulta em cada filtro, na análise de autores e na análise de palavras-chave. No fim de cada pesquisa é perguntado se o utilizador quer exportar aparecendo mensagem de erro enquanto não for dada a resposta pedida.
No menu de interface gráfica em cada um dos menus sejam eles de consulta, visualizar autores ou visualizar palavras-chave, o utilizador apenas pode exportar clicando no botão específico e colocando o nome que quiser.

### __11. Apagar registo__

A função eliminar recebe como parâmetros a base de dados (fnome) e o título da publicação que quer eliminar.
Esta função, primeiramente, verifica o tamanho da lista, e, de seguida através do código fnome[:] o programa substitui diretamente a ata com todos os elementos da base de dados anterior com exceção da publicação cujo título foi fornecido.
De seguida verifica se a nova ata for mais pequena que a anterior. Se for, apresenta uma mensagem de sucesso. Se não aparece uma mensagem a dizer que o título não foi encontrado.


### __Menus da linha de comando__

A função menuestatistica apresenta um menu de opções estatísticas e executa a ação correspondente com base na distribuição de publicações por ano, por autor(top 20), por publicações por autor de um determinado ano, por palavras-chave(top 20) e por palavras-chave mais frequentes num ano. Este menu chama as funções graficoPub_Ano, graficoPostAutor, graficoFreq_keyw, graficoFreq_keyw_ano, graficoDistrib_autor previamente descritas.

A função menuconsulta apresenta um menu de opções que executa a ação correspondente com base em títulos, em palavras-chave, em autores, datas de publicação e afiliações. Este menu utiliza as funções consultarRegisto_titulo, consultarRegisto_palavras, consultarRegisto_data, consultarRegisto_autor, consultarRegisto_afiliacao previamente descritas.

A função menu apresenta um menu de opções com diferentes ações: carregar dataset, inserir publicação, atualizar publicação, consultar publicação, analisar publicações por autor, analisar publicações por palavras-chave, estatísticas de publicação, apagar publicação, gravar o modelo em ficheiro, importar dados, exportação parcial de dados e finalmente sair do menu. Este menu utiiza as funções carregarFicheiro, inserirRegisto, atualizarPublicacao, menuconsulta, todas as funções explicadas nos tópicos 5 e 6, menuestatistica, eliminar, salvar_dados, import_dados e exportar, todas já descritas.

### __Documentaçãao detalhada do funcionamento e do uso da interface gráfica__

MENU PRINCIPAL:
* Layout(Janela):
Título "Sistema de Gestão de Publicações"
Botões "Criar Publicação", "Atualização de Publicações", "Consultar Publicações", "Visualizar Autores", "Visualizar Palavras-chave", "Gráficos","Importar Dados" e "Sair".
* Execução:
O menu aparece quando executamos o ficheiro. Ao clicar em qualquer botão vai ser apresentada outra janela com os seus próprios menus. 
A base de dados é carregada diretamente para uma variável.
* Se clicarmos no botão "Sair" será apresentado um popup_yes_no a perguntar se queremos salvar o ficheiro. Se clicarmos em yes aparece um layout a perguntar o título para o qual queremos salvar os dados. Apresenta também os botões "Salvar" e "Cancelar". O botão "Salvar" salva os dados utilizando a função salvar_dados, o "Cancelar" fecha o menu principal. 
* Se clicarmos no botão "Importar Dados" irá criar o seguinte layout: 
Título "Importar Dados"
Uma barra de escrita para introduzir o nome do arquivo e os botões "Importar" e "Cancelar". O botão importar utiliza a função import_dados e se os dados forem importados com sucesso impime uma mensagem de sucesso. O botão "Cancelar" fecha a janela.
* Se clicarmos no botão "Criar Publicação" é mostrada uma janela onde:
Aparecerão barras de inserção de texto, listboxes e botões necessários à criação de uma publicação. 
Nas áreas de “Título”, “URL”, “DOI”, “Abstrato” e “PDF”, apenas temos de escrever o que pretendemos. 
Na data, podemos escrever a data no formato ano-mês-dia ou podemos selecionar no calendário usando o botão “Selecionar Data”.
Para adicionar um autor, usamos o “Adicionar Autor”, aparecendo uma janela que pede para escrever o nome do autor e depois se clicarmos em “Ok” irá pedir, também, a afiliação do autor e o seu Orcid. Para remover um autor (por exemplo, se nos tivermos enganado a escrever o seu nome), clicamos no autor que pretendemos eliminar e usamos o botão “Remover Autor”;
Para adicionar palavras-chave, a lógica é a mesma que a dos autores: irá aparecer uma janela que pede para escrever a palavra-chave e clicamos em “Ok”, e para remover uma palavra-chave selecionamos a que queremos e clicamos em “Remover Palavra-Chave”.
No fim, clicamos em “Salvar” e se tivermos preenchido todo os campos obrigatórios (Título, Autor e Data), o sistema irá mostrar uma mensagem a confirmar que a publicação foi criada.
*  Ao clicar no botão "Consultar Publicações" irá aparecer uma janela com o layout onde surgem os botões:
- "Consultar por Título", "Consultar por Palavra-chave", "Consultar por Data", "Consultar por Autor" e "Consultar por Afiliação" que chamam, respetivamente, os seguintes menus: consulta_por_titulo, consulta_por_palavra_chave, consulta_por_data, consulta_por_autor e consulta_por_afiliacao.
- "Ver publicação" em que o código procura a publicação na ata comparando o título da publicação selecionada com o título na lista "-TITULOS-". Por fim utiiza a seguinte função:
- - mostrar_publicacao_popup que serve para exibir um popup com as informações de uma publicação em um formato bem organizado e legível.
A função json.dumps() converte a publicação, que provavelmente é um dicionário Python, em uma string JSON.
O argumento indent=4 organiza o JSON de maneira legível, com 4 espaços de indentação.
O argumento ensure_ascii=False permite que caracteres especiais (como acentos e caracteres de outros idiomas) sejam mantidos corretamente, sem forçar a codificação para ASCII. 
sg.popup_scrolled() é uma função do PySimpleGUI que exibe um popup com uma área de movimentação.
O conteúdo do popup é publicacao_formatada, que contém a publicação convertida para o formato JSON e bem estruturada.
title="Informações da Publicação" define o título da janela do popup.
size=(80, 20) define o tamanho do popup, sendo 80 a largura (em caracteres) e 20 a altura.
- "Exportar": a função exportar é chamada para exportar os resultados da consulta (autores selecionados).
- "Sair": retorna à tela anterior.
* Se clicar em qualquer dos restantes botões serão chamados os menus para eles definidos que serão descritos em seguida.

- A função **menu_atualizar_publicacao** permite procurar uma publicação pelo título, visualizar e editar as suas informações, como também salvar as modificações.

* Layout(Janela):
Texto para pedir ao utilizador o título da publicação a ser atualizada;
Um campo de texto para inserir o título da publicação;
Botões "Procurar" e "Cancelar".
A janela window_atualizar é criada com esse layout.
* Execução:
Quando clicamos em "Procurar", o programa verifica se há uma publicação com o título fornecido.
Se a publicação for encontrada exibe as informações detalhadas da publicação (título, resumo, autores, palavras-chave, DOI, URL, PDF, data de publicação) e permite ao utilizador editar essas informações.
Se a quisermos editar, a janela de edição layout_editar é criada, permitindo a edição de vários campos: resumo, palavras-chave, autores, DOI, PDF, data de publicação e URL.
As informações dos autores são exibidas em formato "Nome - Afiliação - ORCID".
O utilizador pode salvar as edições clicando no botão "Salvar".
Ao salvar, o programa atualiza os campos da publicação com os novos dados fornecidos pelo utilizador:
O campo de palavras-chave é processado e dividido numa lista de palavras-chave.
O campo de autores é processado para manter o formato "Nome - Afiliação - ORCID".
Os campos DOI, PDF, URL, data de publicação são tratados para garantir que valores vazios não sejam salvos.
Se a publicação for atualizada com sucesso, ao clicar em "Salvar", um popup de sucesso é exibido.
Se o utilizador clicar em "Cancelar" em qualquer parte do processo, a janela correspondente será fechada e o fluxo será interrompido.
Se a publicação não for encontrada, o utilizador é notificado com um popup de erro.


- A função **consulta_por_titulo** permite procurar e visualizar publicações com base no título, ordenando-as por título ou data.

* Layout(Janela):
Um campo de texto para o utilizador introduir o título da publicação que deseja consultar;
Dois botões de rádio para escolher a ordenação (por título ou por data) e mais dois botões com "Procurar" e "Voltar";
A janela window_titulo é criada com esse layout.
* Execução:
Quando fechamos a janela ou clicamos no botão "Voltar", o loop é interrompido e a janela é fechada.
Quando clicamos em "Procurar":
A função captura o título inserido pelo utilizador.
Utiliza a função pr.consultarRegisto_titulo para procurar as publicações relacionadas ao título fornecido e dependendo da opção de ordenação selecionada (por título ou por data), as publicações são ordenadas utilizando as funções ordenar_por_titulo ou ordenar_por_data.
A função window['-RESULT-'].update(...) atualiza a lista de resultados na interface gráfica, exibindo os títulos das publicações encontradas.
Após a procura, a janela de consulta é fechada com o comando window_titulo.close().



- A função **consulta_por_palavra_chave** permite procurar publicações com base numa palavra-chave específica.

* Layout(Janela):
Campo de entrada de texto para o utilizador digitar a palavra-chave.
Dois botões de rádio para escolher como os resultados devem ser ordenados: por título ou por data e mais outros dois botões com "Procurar" e "Voltar";
A janela é criada com o layout layout_keyword usando o método sg.Window.
* Execução:
A função entra num loop onde window_keyword.read() aguarda interações do utilizador.
Eventos tratados:
Quando fechamos a janela ou clicamos no botão "Voltar" o loop é interrompido e a janela é fechada com window_keyword.close().
Quando clicamos em "Procurar":
A função captura a palavra-chave escrita pelo utilizador (values_keyword['-KEYWORD-']);
Utiliza a função pr.consultarRegisto_palavras para procurar publicações relacionadas à palavra-chave fornecida.
Dependendo da escolha do utilizador (ordenar por título ou por data), os resultados são ordenados usando ordenar_por_titulo ou ordenar_por_data.
A função window['-RESULT-'].update(...) atualiza a interface gráfica com os títulos das publicações encontradas.
Após a consulta e atualização dos resultados, a janela de consulta é fechada com o comando window_keyword.close().



- A função **consulta_por_data** permite realizar uma consulta de publicações com base numa data específica, com a opção de ordenar os resultados por título ou por data.

* Layout(Janela):
Campo de entrada de texto para o utilizador digitar a data no formato "YYYY-MM-DD".
Botão de calendário para facilitar a seleção da data.
Dois botões de rádio para escolher como ordenar os resultados: por título ou por data e mais dois botões com "Procurar" e "Voltar"
A janela é criada usando o layout layout_data e o método sg.Window.
* Execução:
O código entra num loop onde window_data.read() aguarda interações do utilizador.
Quando fechamos a janela ou clicamos no botão "Voltar" o loop é interrompido e a janela é fechada com window_data.close().
Quando clicamos em "Procurar":
A função lê a data fornecida pelo utilizador (values_data['-DATA-']).
Usa a função pr.consultarRegisto_data para procurar publicações relacionadas à data.
Dependendo da escolha do utilizador (ordenar por título ou por data), os resultados são ordenados utilizando ordenar_por_titulo ou ordenar_por_data.
Os resultados das publicações são atualizados na interface gráfica com window['-RESULT-'].update(...), exibindo os títulos das publicações encontradas.
Após a consulta e atualização dos resultados, a janela de consulta é fechada com o comando window_data.close().



- A função **consulta_por_autor** implementa a funcionalidade de consulta de publicações com base no nome de um autor.

* Layout(janela):
Campo de entrada de texto para o utilizador escrever o nome do autor.
Dois botões de rádio para escolher como ordenar os resultados: por título ou por data e mais dois botões com "Procurar" e "Voltar" para iniciar a procura ou voltar à tela anterior.
A janela é criada usando o layout layout_autor e o método sg.Window.
* Execução:
O código entra num loop onde window_autor.read() aguarda interações do utilizador.
Quando fechamos a janela ou clicamos no botão "Voltar" o loop é interrompido e a janela é fechada com window_data.close().
Quando clicamos em "Procurar":
A função lê o nome do autor fornecido pelo utilizador (values_autor['-AUTOR-']).
Usa a função pr.consultarRegisto_autor para procurar publicações relacionadas ao autor.
Dependendo da escolha do utilizador (ordenar por título ou por data), os resultados são ordenados utilizando ordenar_por_titulo ou ordenar_por_data.
Os resultados das publicações são atualizados na interface gráfica com window['-RESULT-'].update(...), exibindo os títulos das publicações encontradas.
Após a consulta e atualização dos resultados, a janela de consulta é fechada com o comando window_autor.close().



- A função **consulta_por_afiliacao** permite procurar publicações com base na afiliação dos autores.

* Layout (janela):
Campo de entrada de texto para o utilizador digitar a afiliação.
Dois botões de rádio para escolher a ordem de exibição: por título ou por data.
Botões "Procurar" para executar a consulta e "Voltar" para retornar à tela anterior.
A janela é criada usando layout_afiliacao e o método sg.Window.
* Execução:
O código entra num loop, aguardando a interação do utilizador.
Quando fechamos a janela ou clicamos em "Voltar" o loop é interrompido e a janela é fechada com window_afiliacao.close().
Quando clicamos em "Procurar":
A função lê a afiliação inserida pelo utilizador (values_afiliacao['-AFILIACAO-']).
Utiliza a função pr.consultarRegisto_filiacao para consultar as publicações associadas à afiliação.
Dependendo da escolha do utilizador, os resultados são ordenados usando ordenar_por_titulo ou ordenar_por_data.
Os títulos das publicações são exibidos na interface com window['-RESULT-'].update([pub["title"] for pub in res]).
A janela de consulta é fechada após a exibição dos resultados.



- A função **ordenar_por_data** tem como objetivo ordenar uma lista de publicações com base na data. Recebe uma lista de publicações (res) e ordena essas publicações com base na data presente em cada item da lista. Para cada publicação (pub), é usado o método .get() para aceder ao valor da chave 'date'. Se a chave 'date' não existir, será retornado uma string vazia ('') como valor padrão. O sorted(): Ordena a lista res com base no valor da chave 'date'. Se a chave 'date' não existir, as publicações que não tiverem a data definida ficarão no início ou no final da lista, dependendo da ordem de ordenação. 


- A função **ordenar_por_titulo** tem como objetivo ordenar uma lista de publicações com base no título de cada publicação. Recebe uma lista de publicações (res) e ordena essas publicações com base no título de cada uma. lambda pub: pub.get('title', '').lower(): Para cada publicação (pub), o valor da chave 'title' é obtido com o método .get(). Se a chave 'title' não existir, será devolvida uma string vazia (''). O valor devolvido é então convertido para minúsculas usando .lower() para garantir que a ordenação seja insensível ao uso de maisúsculas. A função sorted() organiza as publicações em ordem alfabética com base no título.


- A função **menu_visualizar_autores** exibe uma interface para visualizar autores e as publicações associadas a eles, com a opção de ver detalhes da publicação e exportar os resultados.

* Layout(Janela):
Lista de Autores: Exibe os nomes dos autores disponíveis.
Lista de Publicações: Exibe as publicações associadas ao autor selecionado.
Botões de Ação:
"Ver Publicação" exibe detalhes da publicação selecionada.
"Exportar" permite exportar os resultados.
"Voltar" retorna à tela anterior.
* Execução:
Fechar a Janela ou Clicar em "Voltar": Se o evento for "Voltar" ou sg.WINDOW_CLOSED, o loop é interrompido e a janela é fechada.
Seleção de Autor: Quando um autor é selecionado na lista "-AUTORES-", a função pr.postAutor é chamada para procurar as publicações associadas ao autor selecionado.
As publicações associadas ao autor são atualizadas na lista "-TITULOS-" da interface.
Quando o utilizador clica em "Ver Publicação", a publicação associada ao título selecionado na lista "-TITULOS-" é localizada e exibida em um popup com detalhes.
Se nenhuma publicação for selecionada, ou se o título não for encontrado, o programa mostra uma mensagem de erro.
Ao clicar em "Exportar", a função exportar é chamada para exportar os resultados da consulta (autores selecionados).
Ao selecionar "Ver Publicação", o código procura a publicação na ata comparando o título da publicação selecionada com o título na lista "-TITULOS-".
Quando a publicação é encontrada, ela é exibida num popup usando a função mostrar_publicacao_popup.
Após o término do loop de execução, a janela é fechada com window_autor.close().

- A função **menu_listar_palavras_chave** exibe uma interface para visualizar as palavras-chave e as publicações associadas a elas, com a opção de ver detalhes da publicação e exportar os resultados.

* Layout(Janela): 
Opções de Ordenação: O utilizador pode escolher entre ordenar as palavras-chave por:
Ocorrência (quantas vezes cada palavra-chave aparece nas publicações).
Alfabética (ordem alfabética das palavras-chave).
Lista de Palavras-chave: Exibe as palavras-chave disponíveis, com a possibilidade de clicar para selecionar.
Lista de Publicações: Exibe as publicações associadas à palavra-chave selecionada.
Botões de Ação:
"Atualizar Lista" carrega a lista de palavras-chave ordenada.
"Ver Publicação" exibe detalhes da publicação selecionada.
"Exportar" permite exportar os resultados.
"Voltar" retorna à tela anterior.
* Execução:
O loop principal espera os seguintes eventos:
Fechar a Janela ou Clicar em "Voltar":
Se o evento for "Voltar" ou sg.WINDOW_CLOSED, o loop é interrompido e a janela é fechada.
Atualizar Lista:
Quando o utilizador clica em "Atualizar Lista", a função pr.ordena_Keyw_ocor ou pr.ordena_Keyw_alfa é chamada para ordenar as palavras-chave conforme a opção escolhida (por ocorrência ou ordem alfabética).
As palavras-chave são ,então, exibidas na lista "KEYWORDS".
Seleção de Palavras-chave:
Quando o utilizador seleciona uma palavra-chave na lista "KEYWORDS", a função pr.post_keyw é chamada para procurar as publicações associadas à palavra-chave selecionada.
As publicações associadas à palavra-chave são exibidas na lista "POSTS".
Ao clicar em "Exportar", a função exportar é chamada para exportar os resultados da consulta (autores selecionados).
Visualizar Publicação:
Quando o utilizador  clica em "Ver Publicação", a publicação associada ao título selecionado na lista "POSTS" é localizada e exibida num popup com detalhes usando a função mostrar_publicacao_popup.
Se nenhuma publicação for selecionada ou se o título não for encontrado, o código mostra uma mensagem de erro.
Após o término do loop, a janela é fechada com window.close().

- A função **menu_graficos** exibe uma interface que permite escolher de entre alguns relatórios estatísticos.

* Layout:
Botões de ação:
"Distribuição de publicações por ano": permite que apareça um gráfico com número de publicações por ano.
"Número de publicações por autor (top 20 autores)": permite visualizar um gráfico com 20 autores com o maior número de publicações.
"Distribuição de palavras-chave pela sua frequência (top 20 palavras-chave)": Permite visualizar um gráfico com as 20 palavras com maior frequência.
"Distribuição de palavras-chave mais frequentes por ano": Permite visualizar um gráfico com as 20 palavavras-chave mais frequentes de um determinado ano.
"Distribuição de publicações de um autor por ano": Permite visualizar um gráfico com a quantidade de publicações, por ano, de um determinado autor.
* Execução:
Fechar a Janela ou Clicar em "Voltar":
Se o evento for "Voltar" ou sg.WINDOW_CLOSED, o loop é interrompido e a janela é fechada.
Quando o utilizador clica nos botões "Distribuição de publicações por ano", "Número de publicações por autor (top 20 autores)" ou "Distribuição de palavras-chave pela sua frequência (top 20 palavras-chave)" o programa apenas executa as funções: graficoPub_Ano, graficoPostAutor ou graficoFreq_keyw, respetivamente.
Se clicar no botão "Distribuição de palavras-chave mais frequente por ano" irá aparecer uma janela onde será possível definir um ano e/ou também clicar nos botões "OK" ou "Cancelar".
Se o evento for "Cancelar" ou sg.WINDOW_CLOSED, o loop é interrompido e a janela é fechada.
Se clicar em "OK" o ano inserido vai ser analisado para saber se está entre 1999 e 2024, inclusive. De seguida vai executar a função graficoFreq_keyw_ano.
Se clicar no botão "Distribuição de publicações de um autor por ano" vai aparecer uma janela semelhante à anterior, sendo a única diferença que esta janela lê o nome de um autor e chama a função graficoDistrib_autor.

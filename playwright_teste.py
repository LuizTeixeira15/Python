from ntpath import join
from tabulate import tabulate

from playwright.sync_api import sync_playwright

with sync_playwright() as pw:
    navegador = pw.chromium.launch()
    contexto = navegador.new_context()
    page = contexto.new_page()

    page.goto("https://ge.globo.com/futebol/brasileirao-serie-a/")
    
    
    print('\n' + page.title() + '\n')

    tabela = []

    times = page.locator("strong").all_text_contents()[2:8:]
    # print(times[1])
    cabecalho = page.locator(".tabela__head").all()
    linha = page.query_selector_all("tr[class='classificacao__tabela--linha']")
    jogos = page.locator("span[class*='classificacao__ultimos_jogos']").all()

    # print(cabecalho[0].inner_text() + "      " + cabecalho[1].inner_text())
    for i, time in enumerate(linha[:5:]):
    # # print(join(linha[21].inner_text()))
        times = page.locator("strong").all_text_contents()[2::]
        texto = linha[i+20].query_selector("td[class='classificacao__pontos classificacao__pontos--ultimos_jogos']")
        texto = texto.inner_html().replace("<span class=\"classificacao__ultimos_jogos classificacao__ultimos_jogos--", "").replace("\">", "").replace("</span>", "")   
    #     print(f'{i+1}º {times[i]}' + '      ' + f'{join(linha[i+20].inner_text())} {texto}')
        tabela.append([f'{i+1}º {times[i]}', f'{join(linha[i+20].inner_text())} {texto}'])
   
    
    #     pontos = time.query_selector("td[class='classificacao__pontos']").in_text()
    #     
    cab = [cabecalho[0].inner_text(),cabecalho[1].inner_text(),"P J V E D GP GC SG % ÚLT. JOGOS"]
    print(tabulate(tabela, headers=cab, tablefmt="", stralign="left"))
    
    

    # for indice, time in enumerate(times):
    #     print(f'{indice + 1}º {time}')
    
    print('\n')
    navegador.close()


    
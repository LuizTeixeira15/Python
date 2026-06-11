from playwright.sync_api import sync_playwright

notas = [
        
        26260609132989000161550010000653251453620919,
        26260660219485000130550010000006161322921079,
        26260647681833000129550010000037561124006675,
        35260625205232000107550010000095241952294001,
        27260645034218000103550010000001321495988240
    ]

with sync_playwright() as pw:
    navegador = pw.chromium.launch(headless=False, args=[
                "--disable-blink-features=AutomationControlled",
                "--disable-infobars",
                "--no-sandbox",
                "--disable-dev-shm-usage"
            ])
    contexto = navegador.new_context()
    page = contexto.new_page()

    page.goto("https://meudanfe.com.br/#")
    for nota in notas:
        page.get_by_role("textbox", name="Chave de Acesso:").fill(str(nota))
        page.get_by_role("link", name="BUSCAR", exact=True).click()

        with page.expect_download() as download_info:
            page.get_by_role("link", name="Baixar XML", exact=True).click()   
        
        download = download_info.value
        download.save_as("./downloads/xml/" + download.suggested_filename)

        with page.expect_download() as download_info:
            page.get_by_role("link", name="Baixar PDF", exact=True).click()   
        
        download = download_info.value
        download.save_as("./downloads/nf/" + download.suggested_filename)
        page.get_by_role("link", name="NOVA CONSULTA", exact=True).click()
    
    navegador.close()
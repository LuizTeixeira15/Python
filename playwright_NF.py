from playwright.sync_api import sync_playwright

notas = [
        26260512919018000170550010000385691014971816,
        27260645034218000103550010000001271310932501,
        26260515426874001154550010000263681394665003
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
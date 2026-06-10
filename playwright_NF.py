from playwright.sync_api import sync_playwright

notas = [
        26260650770643000869550020000224871785532687,
        26260604917818000205550010000047121809341290,
        26260661234985007117550050001367941461841381,
        26260661234985007117550050001367881331195342,
        26260610258873000748550000000188001360101934
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
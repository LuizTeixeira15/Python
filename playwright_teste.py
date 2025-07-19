from playwright.sync_api import sync_playwright

def run_playwright_example():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://www.flamengo.com.br/')
        print(page.title())
        browser.close()

if __name__ == "__main__":
    run_playwright_example()
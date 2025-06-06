import asyncio
from playwright.async_api import async_playwright


async def parse_wb(product_url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(args=[
            '--disable-blink-features=AutomationControlled',
            '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36...'
        ])
        page = await browser.new_page()
        await page.goto(product_url)
        await page.wait_for_selector(".product-page__title")
        await page.wait_for_selector(".price-block__final-price")

        title = await page.text_content(".product-page__title")
        pre_price = await page.text_content(".price-block__final-price")
        price = int(pre_price.split()[0])

        print(title, price)
        await browser.close()


if __name__ == "__main__":
    url = "https://www.wildberries.ru/catalog/303240677/detail.aspx"
    asyncio.run(parse_wb(url))

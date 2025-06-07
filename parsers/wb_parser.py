from playwright.async_api import async_playwright

from lexicon.lexicon import LEXICON
from logging_conf.base_conf import get_logger

logger = get_logger()


async def parse_wb(product_url, user_id):
    async with async_playwright() as p:
        browser = await p.chromium.launch(args=[
            '--disable-blink-features=AutomationControlled',
            '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36...'
        ])
        page = await browser.new_page()
        result = {'shop': LEXICON['wb_shop'],
                  'title': None,
                  'price': None,
                  'product_url': product_url,
                  'article_number': None,
                  'user_id': user_id}
        try:
            await page.goto(product_url)

            try:
                await page.wait_for_selector('.product-page__title')
                title = await page.text_content('.product-page__title')
                result['title'] = title
                logger.info(LEXICON['selector_is_found'].format('title'))
            except Exception as e:
                logger.critical(
                    LEXICON['selector_not_found'].format(f'title: {e}')
                )

            try:
                await page.wait_for_selector('.price-block__final-price')
                pre_price = await page.text_content(
                    '.price-block__final-price'
                )
                price = int(pre_price.split()[0])
                result['price'] = price
                logger.info(LEXICON['selector_is_found'].format('price'))
            except Exception as e:
                logger.critical(
                    LEXICON['selector_not_found'].format(f'price: {e}')
                )

            try:
                await page.wait_for_selector('.product-params__copy')
                article = await page.text_content(
                    '.product-params__copy'
                )
                result['article_number'] = article
                logger.info(LEXICON['selector_is_found'].format('article'))
            except Exception as e:
                logger.critical(
                    LEXICON['selector_not_found'].format(f'article: {e}')
                )

        except Exception as e:
            logger.error(LEXICON['page_loading_error'], e)
        finally:
            await browser.close()
            return result

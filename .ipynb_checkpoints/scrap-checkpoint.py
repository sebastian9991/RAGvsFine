## WEB SCRAPING CELL: 
from playwright.async_api import async_playwright
import asyncio
 

async def main():
   async with async_playwright() as pw:
       browser = await pw.chromium.launch(
           ##Using a proxy creates HTTP errors.
          headless=False
      )

       #Beginning page: 
       page = await browser.new_page()
       await page.goto('https://world.openfoodfacts.org/')
       await page.wait_for_timeout(5000)
       result = {}
       food_urls = page.query_selector_all('.list_product_a').map(lambda item: item.get_attribute('href'))
    for food_url in food_urls: 
        page.goto(food_url)
        #Title: 
        title = page.locator(".title-1")
        title = await title.inner_text()
        result['title'] = title
        #Common Name: 
        common_name = page.locator("#field_generic_name_value")
        common_name = await common_name.inner_text()
        result['common_name'] = common_name
        #Quantity:
        quantity = page.locator("#field_quantity_value")
        quantity = await quantity.inner_text()
        result['quantity'] = quantity
        #Packaging: 
        packaging = page.locator("#field_packaging_value")
        packaging = await packaging.inner_text()
        result['packaging'] = packaging
        break
       
       
       

       
           
           
           
       await browser.close()
       print(result)
if __name__ == '__main__':
   await asyncio(main())


#CITATIONs: 
#Code cited from OxyLabs: https://github.com/oxylabs/playwright-web-scraping?tab=readme-ov-file
#,https://playwright.dev/python/docs/locators
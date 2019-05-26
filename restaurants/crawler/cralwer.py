from bs4 import BeautifulSoup
from selenium import webdriver
import os

_driver_url = os.getenv(
    'GOOGLE_CHROME_SHIM',
    os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'chromedriver'
    )
)
_search_url = 'https://store.naver.com/restaurants/list?entry=pll&query='


def parsingRestaurnts(query):
    options = webdriver.ChromeOptions()
    options.binary_location = os.getenv('GOOGLE_CHROME_BIN', None)
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    print(os.path.dirname(os.path.abspath(__file__)))

    driver = webdriver.Chrome(_driver_url, chrome_options=options)
    driver.get(_search_url + query)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    elements = soup.select(
        'span.tit_inner'
    )[:5]

    message = []

    for element in elements:
        messageItem = []
        messageItem.append('- ')
        messageItem.append(element.find('a').get('title'))
        messageItem.append(' : ')
        messageItem.append(element.find_all('span')[-1].text)
        messageItem.append('\n')
        messageItem.append(element.find('a').get('href'))

        message.append(''.join(messageItem))

    driver.close()

    return message

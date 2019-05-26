from bs4 import BeautifulSoup
from selenium import webdriver
import os

driver_url = os.getenv('GOOGLE_CHROME_SHIM')
if driver_url == None:
    dir = os.path.dirname(os.path.abspath(__file__))
    driver_url = os.path.join(dir, 'chromedriver')

_driver_url = driver_url
_search_url = 'https://store.naver.com/restaurants/list?entry=pll&query='


def parsingRestaurnts(query):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")

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

from pickle import FALSE, TRUE
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from bs4 import BeautifulSoup
import requests
import webbrowser
import time


SCORE = r'C:\Users\bv2cq\Downloads\score_' # Download Path
RENDER = r'Render\score_' # Destination path (relative to MusescoreExtractor)
PATH = "C:\Program Files (x86)\chromedriver.exe"

def write_text(data: str, path: str):
    with open(path, 'w') as file:
        file.write(data)

driver = webdriver.Chrome(PATH)
driver.get("https://musescore.com/captainmeow/chinozo-ft-flower")
driver.set_window_size(1024, 600)
driver.maximize_window()
scrollbar = driver.find_element(By.ID, 'jmuse-scroller-component')
time.sleep(1)

urls = []
html_content = driver.page_source
soup = BeautifulSoup(html_content, "html.parser")
#remove pages_added and add calculation at pagecount+=pagesadded instead
unique_url = True
page_count = 0
scroll_page = 0
while unique_url:
    pages_added = 0
    for link in soup.find(id='jmuse-scroller-component').find_all('img'):
        print(link)
        if str(link).find('svg') != -1:
            score_url = link['src']
            if link['src'] not in urls:
                svg = requests.get(score_url).text
                write_text(svg, SCORE + str(len(urls)) + '.svg') 
                urls.append(score_url)
                pages_added += 1
                 
    print(page_count)
    print(len(urls))
    if page_count < len(urls):
        scroll_page += 1175
        page_count += pages_added
        driver.execute_script("document.querySelector('[id=\"jmuse-scroller-component\"]').scrollTop=" + str(scroll_page), scrollbar)
        time.sleep(5)
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, "html.parser")   
    else:
        unique_url = False
        
driver.quit()
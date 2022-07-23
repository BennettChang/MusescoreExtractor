from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup
import requests
import time

def write_text(data: str, path: str):
    with open(path, 'w') as file:
        file.write(data)

def download_musescore_svg(musescore_link, download_path, PATH):
    MUSESCORE = musescore_link
    DOWNLOAD = download_path + '/score_'
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome(executable_path=PATH, chrome_options=options)
    driver.get(musescore_link)
    driver.set_window_size(1024, 600)
    driver.maximize_window()
    scrollbar = driver.find_element(By.ID, 'jmuse-scroller-component')
    urls = []
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, "html.parser")
    unique_url = True
    page_count = 0
    scroll_page = 0

    # Runs the loop until a unique score url cannot be found
    while unique_url:
        pages_added = 0
        for link in soup.find(id='jmuse-scroller-component').find_all('img'):
            if str(link).find('svg') != -1:
                score_url = link['src']
                if link['src'] not in urls:
                    svg = requests.get(score_url).text
                    write_text(svg, DOWNLOAD + str(len(urls)) + '.svg') 
                    urls.append(score_url)
                    pages_added += 1
        if page_count < len(urls):
            scroll_page += 1175
            page_count = len(urls)
            driver.execute_script("document.querySelector('[id=\"jmuse-scroller-component\"]').scrollTop=" + str(scroll_page), scrollbar)
            time.sleep(1)
            html_content = driver.page_source
            soup = BeautifulSoup(html_content, "html.parser")   
        else:
            unique_url = False
            
    driver.quit()
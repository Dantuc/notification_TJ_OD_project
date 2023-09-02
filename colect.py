import urllib
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=service)

i = 301

while i <= 800:

    nav.get("https://dje.tjmg.jus.br/ultimaEdicao.do")
    captcha = nav.find_element("xpath", '//*[@id="captcha_image"]')
    src = captcha.get_attribute("src")
    print("Buscando arquivo...")
    file = urllib.request.urlretrieve(src, f"./projeto_find/captcha_database/captcha{i}.png")
    print("arquivo baixado com sucesso", file)
    i+=1
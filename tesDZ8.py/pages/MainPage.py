from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys   # кнопки

class MainPage:

    def __init__(self, driver):
        self._drver = driver
        self._drver.get("https://www.labirint.ru")
        self._drver.implicitly_wait(4)   
        self._drver.maximize_window()

    def set_cookei_policy(self):
        cookie = {   # убераем окно с куки
        "name": "cookie_policy",
        "value": "1"
    } 
        self._drver.add_cookie(cookie)
        print('Меня вызвали')
    
    def search(self, term):
        self._drver.find_element(By.CSS_SELECTOR, "#search-field").send_keys(term)
        self._drver.find_element(By.CSS_SELECTOR, "#searchform > div.b-search-e-input-wrapper > button > span.b-header-b-search-e-btntxt").click()
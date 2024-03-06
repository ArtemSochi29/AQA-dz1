from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  

class OpensPage:

    def __init__(self, driver):
        self._drver = driver
        self._drver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._drver.implicitly_wait(4)   
        self._drver.maximize_window()

    def first (self, name):
        self._drver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(1) > div:nth-child(1) > label > input").send_keys(name)
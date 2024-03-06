from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys   # кнопки

from pages.OpenPage import OpensPage

def test_open():
    driver = webdriver.Chrome()

    opens_page = OpensPage(driver)
    opens_page.first("Иван")

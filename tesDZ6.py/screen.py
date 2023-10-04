
from time import sleep    # Время работы браузера
from selenium.webdriver.common.by import By    # Елементы
from selenium import webdriver   #  Браузер
from selenium.webdriver.common.keys import Keys   # кнопки


from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


#browser.maximize_window()
#browser.get("https://ya.ru")


def make_screenshoot(browser):
    browser.maximize_window()
    browser.get("https://ya.ru")
    sleep(5)

    browser.save_screenshot('./a_'+browser.name+'.png')   # скриншот
    browser.quit()  # Закрыть окно браузера

ff = webdriver.Firefox()
chrome = webdriver.Chrome()

make_screenshoot(chrome)
make_screenshoot(ff)
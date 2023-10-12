from time import sleep
from selenium.webdriver.common.by import By    # Елементы
from selenium import webdriver   #  Браузер

driver = webdriver.Chrome()

driver.get("https://labirint.ru")

#driver.maximize_window()  # максимально большое окно
#driver.minimize_window()   # максимально маленькое окно
#driver.fullscreen_window()  # полностью развернуть окно
driver.set_window_size(1000, 600) # размер в ручную

sleep(3)
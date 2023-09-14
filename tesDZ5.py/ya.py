from time import sleep
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()
driver.maximize_window()   # увеличение окна

driver.get("https://my.sky.pro/student-cabinet/course/519/lesson/7462/theory/2")

sleep(2)

driver.fullscreen_window()   # развернуть окно
sleep(2)

driver.save_screenshot('./sky.png')   # сделать скриншот

#driver.get("https://vk.com")  # открыть страницу
#for x in range(1, 10):        #цикл
#    driver.back()           # назад 
#    driver.forward()         # вперед
#    driver.refresh()     # обновить страницу
#driver.set_window_size(640, 460)   # уменьшение окна



from time import sleep
from selenium.webdriver.common.by import By    # Елементы
from selenium import webdriver   #  Браузер

driver = webdriver.Chrome()
driver.get("https://demoqa.com/browser-windows")

driver.find_element(By.CSS_SELECTOR, "#tabButton").click()

sleep(3)
driver.close() # закрытие вкладки текущей
sleep(5)
#driver.quit()
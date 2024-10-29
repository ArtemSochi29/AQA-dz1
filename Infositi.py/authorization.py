from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys   # кнопк


driver = webdriver.Chrome()
driver.maximize_window()  
wait = WebDriverWait(driver, 10)

driver.get("https://stage5.infocity.me/")

#Авторизация
driver.find_element(By.CSS_SELECTOR, "#email").send_keys("Sochi")

driver.find_element(By.CSS_SELECTOR, "#password").send_keys("12345678")

driver.find_element(By.CSS_SELECTOR, "#main-container > div > div.mt-8.sm\:mx-auto.sm\:w-full.sm\:max-w-md > div > form > div:nth-child(4) > button").click()

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#datagrid > div > div.dx-datagrid-header-panel > div > div > div.dx-toolbar-before > div.dx-item.dx-toolbar-item.dx-toolbar-button.dx-toolbar-item-auto-hide.dx-toolbar-text-auto-hide > div > div > div")))

driver.find_element(By.CSS_SELECTOR, '#datagrid > div > div.dx-datagrid-header-panel > div > div > div.dx-toolbar-before > div.dx-item.dx-toolbar-item.dx-toolbar-button.dx-toolbar-item-auto-hide.dx-toolbar-text-auto-hide > div > div').click()
sleep(5)
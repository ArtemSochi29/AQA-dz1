from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys   # кнопк


driver = webdriver.Chrome()
driver.get("https://stage5.infocity.me/")

#Авторизация
driver.find_element(By.CSS_SELECTOR, "#email").send_keys("Sochi")

driver.find_element(By.CSS_SELECTOR, "#password").send_keys("12345678")

driver.find_element(By.CSS_SELECTOR, "#main-container > div > div.mt-8.sm\:mx-auto.sm\:w-full.sm\:max-w-md > div > form > div:nth-child(4) > button").click()

#Кнопка создать задачу
driver.find_element(By.CSS_SELECTOR, "#datagrid").click()
sleep(10)

#создание задачи
driver.find_element(By.CSS_SELECTOR, "#dx_dx-a1842c49-b229-99da-44ee-713c78d08924_serviceObjectTypeId").click()

driver.find_element(By.CSS_SELECTOR, "#dx-642a9ae5-f1c9-32db-1973-fbb8b7e58114 > div > div > div.dx-treelist-rowsview.dx-scrollable.dx-visibility-change-handler.dx-scrollable-both.dx-scrollable-native.dx-scrollable-native-generic > div > div > div > div > table > tbody > tr:nth-child(6) > td > div.dx-treelist-text-content").click()

driver.find_element(By.CSS_SELECTOR, "#dx_dx-a1842c49-b229-99da-44ee-713c78d08924_serviceObjectId").click()

driver.find_element(By.CSS_SELECTOR, "#dx-1304e9c3-4cee-e62f-748c-6825e4ede0e3 > div.dx-scrollable-wrapper > div > div > div.dx-scrollview-content > div:nth-child(1) > div").click()

driver.find_element(By.CSS_SELECTOR, "#dx_dx-a1842c49-b229-99da-44ee-713c78d08924_workTypeId").click()

driver.find_element(By.CSS_SELECTOR, "#dx-568a4239-b62e-8647-c924-c4b97ba26971 > div.dx-scrollable-wrapper > div > div > div.dx-scrollview-content > div:nth-child(2) > div").click()

driver.find_element(By.CSS_SELECTOR, "#dx_dx-a1842c49-b229-99da-44ee-713c78d08924_companyUserExecutorId").click()

driver.find_element(By.CSS_SELECTOR, "#dx-3da76b83-1c27-b4a9-842b-dc25bf1bd4d9 > div.dx-scrollable-wrapper > div > div > div.dx-scrollview-content > div:nth-child(4) > div").click()

driver.find_element(By.CSS_SELECTOR, "#dx_dx-a1842c49-b229-99da-44ee-713c78d08924_taskTypeId").click()

driver.find_element(By.CSS_SELECTOR, "#dx-c6149168-b331-72a4-b9de-3412a154a111 > div.dx-scrollable-wrapper > div > div > div.dx-scrollview-content > div:nth-child(4) > div").click()

driver.find_element(By.CSS_SELECTOR, "#btnSubmit > div > span").click()



sleep(10)
# . driver.find_element(By.CSS_SELECTOR, "").click()
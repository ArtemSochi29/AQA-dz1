from time import sleep
from selenium import webdriver
#from selenium.webdriver.chrome import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.implicitly_wait(20) # задержка на сайте будет ждать сколь дали времени


driver.get("http://uitestingplayground.com/ajax")

driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

content = driver.find_element(By.CSS_SELECTOR, "#content")
txt = content.find_element(By.CSS_SELECTOR, "p.bg-success").text

print(txt)
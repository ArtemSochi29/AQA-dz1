from time import sleep
from selenium.webdriver.common.by import By   
from selenium import webdriver  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
sleep(10)

waiter = WebDriverWait(driver, 20)

waiter.until(
    EC.element_to_be_selected((By.CSS_SELECTOR, "#award"), "srt")
)

print(waiter)





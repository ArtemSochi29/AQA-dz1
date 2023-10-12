from selenium.webdriver.common.by import By    # Елементы
from selenium import webdriver   #  Браузер

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()


driver.get("http://uitestingplayground.com/progressbar")

driver.find_element(By.CSS_SELECTOR, "#startButton").click()

waiter = WebDriverWait(driver, 40, 0.1) # ждет сколькото секунд

waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[aria-valuenow='75']"), "75%") # ждет когда будет 75% 
)

driver.find_element(By.CSS_SELECTOR, "#stopButton").click()

print(driver.find_element(By.CSS_SELECTOR, "#result").text)


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By   
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys   # кнопки

driver = webdriver.Chrome()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

wait = WebDriverWait(driver, 50)

driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(Keys.ARROW_LEFT, "4")

driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(1)").click()

driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(4)").click()

driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(2)").click()

driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span.btn.btn-outline-warning").click()


wait.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#calculator > div.top > div"), "15"))

def test_displayed_15():
    assert driver.find_element(By.CSS_SELECTOR, "#calculator > div.top > div").text == "15"
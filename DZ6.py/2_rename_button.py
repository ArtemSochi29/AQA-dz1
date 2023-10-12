from selenium.webdriver.common.by import By   
from selenium import webdriver  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/textinput")

waiter = WebDriverWait(driver, 20)

intry_field = driver.find_element(By.CSS_SELECTOR, "#newButtonName").send_keys("SkyPro")

get_text = driver.find_element(By.CSS_SELECTOR,  "#updatingButton").click()

waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#updatingButton"), "SkyPro")
)

print(driver.find_element(By.CSS_SELECTOR, "#updatingButton").text)
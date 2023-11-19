from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By   
from selenium import webdriver  

driver = webdriver.Chrome()

wait = WebDriverWait(driver, 20)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(1) > div:nth-child(1) > label > input").send_keys("Иван")

last = driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(1) > div:nth-child(2) > label > input").send_keys("Петров")

address = driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(2) > div.col-md-4.py-2 > label > input").send_keys("Ленина, 55-3")

e_mail = driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(3) > div:nth-child(1) > label > input").send_keys("test@skypro.com")

phone_num = driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(3) > div:nth-child(2) > label > input").send_keys("+7985899998787")

city = driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(2) > div:nth-child(3) > label > input").send_keys("Москва")

country = driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(2) > div:nth-child(4) > label > input").send_keys("Россия")

job = driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(4) > div:nth-child(1) > label > input").send_keys("QA")

company = driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(4) > div:nth-child(2) > label > input").send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, "body > main > div > form > div:nth-child(5) > div > button").click()

wait.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#company"), "SkyPro")
)

color_red = driver.find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property("color")
print(color_red)

def test_color_red():
    assert color_red == 'rgba(132, 32, 41, 1)'

color_green = driver.find_elements(By.CSS_SELECTOR, ".py-2.alert-success")
#color_green = driver.find_element(By.CSS_SELECTOR, ".py-2.alert-success").value_of_css_property("color")
color_green_count = len(color_green)
print(color_green_count)

def test_color_green():
    assert color_green_count == 'rgba(15, 81, 50, 1)'



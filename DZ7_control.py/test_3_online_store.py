from selenium.webdriver.common.by import By   
from selenium import webdriver  
driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

# Авторизация
driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")

driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")

driver.find_element(By.CSS_SELECTOR, "#login-button").click()

# Добавьте в корзину товары:

driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()

driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()

driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

# Перейдите в корзину.
driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container > a").click()

# Нажмите Checkout.
driver.find_element(By.CSS_SELECTOR, "#checkout").click()

# Заполните форму своими данными:
driver.find_element(By.CSS_SELECTOR, "#first-name" ).send_keys("Artem")

driver.find_element(By.CSS_SELECTOR, "#last-name" ).send_keys("Baranov")

driver.find_element(By.CSS_SELECTOR, "#postal-code" ).send_keys("600600")

# Нажмите кнопку Continue.
driver.find_element(By.CSS_SELECTOR, "#continue" ).click()

# Прочитайте со страницы итоговую стоимость ( Total ).
asa = driver.find_element(By.CSS_SELECTOR, "#checkout_summary_container" ).text
print(asa)

# Закройте браузер.
driver.find_element(By.CSS_SELECTOR, "#finish").click()
driver.quit()

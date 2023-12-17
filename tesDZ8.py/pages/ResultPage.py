from selenium.webdriver.common.by import By

class ResultPage:

    def __init__(self, browser):
        self._driver = browser

    def add_books(self):
        buy_buttons = self._driver.find_elements(By.CSS_SELECTOR, ".product-card__controls-container")
        counter = 0
        for btn in buy_buttons:
             btn.click() # Нажать на все кнопки в цикле
             counter += 1
    
        return counter
    
    def get_empty_result_message(self):
        div = self._driver.find_element(By.CSS_SELECTOR, "div.search-error")
        h1 = div.find_element(By.CSS_SELECTOR, "h1")
        return h1.text
from time import sleep
from selenium.webdriver.common.by import By    # Елементы
from selenium import webdriver   #  Браузер

driver = webdriver.Chrome()

driver.get("https://ya.ru")

#driver.find_elements()    # найти элементы

txt = driver.find_element(By.CSS_SELECTOR, 'a[title="USD MOEX"]').text
print(txt)

#tag = driver.find_element(By.CSS_SELECTOR, 'a[title="USD MOEX"]').tag_name
#print(tag)

#id = driver.find_element(By.CSS_SELECTOR, 'a[title="USD MOEX"]').id
#print(id)

#href = driver.find_element(By.CSS_SELECTOR, 'a[title="USD MOEX"]').get_attribute("href")
#print(href)


#ff = driver.find_element(By.CSS_SELECTOR, 'a[title="USD MOEX"]').value_of_css_property("font-family")
#print(ff)

#color = driver.find_element(By.CSS_SELECTOR, 'a[title="USD MOEX"]').value_of_css_property("color")
#print(color)
#txt = usd.text
#sleep(10)
#driver.get("http://uitestingplayground.com/visibility")
#is_displayed = driver.find_element(By.CSS_SELECTOR, "#transparentButton").is_displayed() #видно элемент или нет
#print(is_displayed)

#driver.find_element(By.CSS_SELECTOR, "#hideButton").click()

#is_displayed = driver.find_element(By.CSS_SELECTOR, "#transparentButton").is_displayed()  #видно элемент или нет
#print(is_displayed)
#sleep(3)

#driver.get("https://demoqa.com/radio-button")

#is_enabled = driver.find_element(By.CSS_SELECTOR, "#yesRadio").is_enabled() # активно или нет
#print(is_enabled)

#is_enabled = driver.find_element(By.CSS_SELECTOR, "#noRadio").is_enabled()
#print(is_enabled)

#driver.get("https://the-internet.herokuapp.com/checkboxes")

#cb = driver.find_element(By.CSS_SELECTOR,"input[type=checkbox]")

#is_selectod = cb.is_selected() # является активным
#print(is_selectod)

#cb.click()

#is_selectod = cb.is_selected()
#print(is_selectod)

#sleep(3)

#driver.get("https://the-internet.herokuapp.com/checkboxes")
#div = driver.find_element(By.CSS_SELECTOR, "#page-footer")

#a = div.find_element(By.CSS_SELECTOR, "a")

#print(a.get_attribute("href"))  # поиск ссылки

#driver.get("https://the-internet.herokuapp.com/checkboxes")
#divs = driver.find_elements(By.CSS_SELECTOR, 'div')

#l = len(divs) # строка

#print(l)

#div = divs[6]
#css_class = div.get_attribute("class")

#print(css_class)
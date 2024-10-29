from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys   # кнопк


driver = webdriver.Chrome()
driver.maximize_window()  
wait = WebDriverWait(driver, 10)

driver.get("https://numeroid.ru/")

driver.find_element(By.CSS_SELECTOR, '#__next > div > div > div.Container_layout__nFbzl.Home_container__BLI7G > section:nth-child(2) > div > div:nth-child(1) > a > div.OfferCard_cardMedia__m8xft > span > img').click()

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#__next > div > div > div > div.MuiGrid-root.MuiGrid-container.MuiGrid-spacing-xs-2.css-isbt42 > div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-xs-12.MuiGrid-grid-md-9.css-1xd5sck > div:nth-child(2) > div.HotelSearchCard_cardContent__yUW3J > div.HotelSearchCard_cardBottom__Z7b9M > button')))
driver.find_element(By.CSS_SELECTOR, '#__next > div > div > div > div.MuiGrid-root.MuiGrid-container.MuiGrid-spacing-xs-2.css-isbt42 > div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-xs-12.MuiGrid-grid-md-9.css-1xd5sck > div:nth-child(2) > div.HotelSearchCard_cardContent__yUW3J > div.HotelSearchCard_cardBottom__Z7b9M > button').click()

wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#__next > div > div > div > div.Hotel_content__Ln07U.MuiBox-root.css-0 > div > div.Hotel_hotelHeader__lWmQj.MuiBox-root.css-0 > div.Hotel_actionButtons__zTj53 > button.MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.css-trq7j6')))
driver.find_element(By.CSS_SELECTOR, '#__next > div > div > div > div.Hotel_content__Ln07U.MuiBox-root.css-0 > div > div.Hotel_hotelHeader__lWmQj.MuiBox-root.css-0 > div.Hotel_actionButtons__zTj53 > button.MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.css-trq7j6').click()

driver.find_element(By.CSS_SELECTOR, '#__next > div > div > div > div.Hotel_content__Ln07U.MuiBox-root.css-0 > div > div.HotelPhoto_previewsBlock__m5w4J > ul.HotelPhoto_photoGrid__l2XgG > li.HotelPhoto_photoGridItem__JGCL0.HotelPhoto_large__p5TYD > a > span > img').click()

wait.until(EC.presence_of_all_elements_located ((By.CSS_SELECTOR, 'body > div.MuiDialog-root.MuiModal-root.css-1tecg5t > div.MuiDialog-container.MuiDialog-scrollPaper.css-ekeie0 > div > div > div > div > div.ThumbsGallery_thumbsViewport__2LjY7 > div > ul > li:nth-child(6) > a > img')))
driver.find_element(By.CSS_SELECTOR, 'body > div.MuiDialog-root.MuiModal-root.css-1tecg5t > div.MuiDialog-container.MuiDialog-scrollPaper.css-ekeie0 > div > div > div > div > div.ThumbsGallery_thumbsViewport__2LjY7 > div > ul > li:nth-child(6) > a > img').click()


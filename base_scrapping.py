from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from classes.listings import Listing

driver = webdriver.Firefox()
driver.get('https://remax.com.br/PublicListingList.aspx?SelectedCountryID=55#mode=gallery&cur=BRL')

wait = WebDriverWait(driver, 10)
result = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'gallery-container')))
child_elements = result.find_elements(By.CLASS_NAME, 'gallery-item')

for element in child_elements:
  print(Listing(element))

driver.quit()

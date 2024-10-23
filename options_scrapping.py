from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()
driver.get('https://remax.com.br/PublicListingList.aspx?SelectedCountryID=55#mode=gallery&cur=BRL')

wait = WebDriverWait(driver, 10)

driver.find_element(By.CLASS_NAME, 'btn-rent').click()

results = driver.find_elements(By.XPATH, "//input[@class='js-geo-search']")
print(results)
print(len(results))

for result in results:
  print(result.get_attribute('innerHTML'))

driver.quit()

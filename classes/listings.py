from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class Listing:
  def __init__(self, element: WebElement):
    self.element = element
    self.price = self.query_price()
    self.place_type = self.query_place_type()
    self.granularity = ''
    self.query_adress()
    self.query_item_type()

  def query_item_type(self):
    for_sale = self.element.find_element(By.CLASS_NAME, 'card-trans-type').text
    self.for_sale = for_sale == 'For Sale'

    if self.for_sale == False:
      granularity = self.element.find_element(By.CLASS_NAME, 'gallery-price-granular').text
      if granularity == '[Monthly]':
        self.granularity = 'mês'
      else:
        self.granularity = 'ano'

  def display_price(self):
    if self.for_sale:
      return 'Preço: ' + self.price + ' reais'
    else:
      return 'Preço: ' + self.price + ' reais/' + self.granularity

  def query_price(self):
    return self.element.find_element(By.CLASS_NAME, 'proplist_price').text.split(' ')[1]

  def query_place_type(self):
    return self.element.find_element(By.CLASS_NAME, 'gallery-transtype').find_element(By.TAG_NAME, 'span').text
  
  def query_adress(self):
    location = self.element.find_element(By.CLASS_NAME, 'gallery-title').find_element(By.TAG_NAME, 'a').text
    parts = location.split(' - ')

    if len(parts) > 1:
      self.address = parts[0]
      self.location = parts[1]
    else:
      self.location = location
      self.address = ''

  def __str__(self):
    return 'Preço: ' + self.display_price() + '\n' + 'Tipo: ' + self.place_type + '\n' + 'Endereço: ' + self.location + '\n'

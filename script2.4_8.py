from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import os 
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)
    
button = WebDriverWait(browser, 20)
button.until( EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
button = browser.find_element_by_css_selector("#book")
button.click()
    
    
x_element = browser.find_element_by_css_selector("#input_value")
x =(x_element.text)
y = calc(x)
    
input1 = browser.find_element_by_css_selector(".form-group #answer")
input1.send_keys(y)
    
button = browser.find_element_by_css_selector("#solve")
button.click()
   
   
    

  


    # ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(50)
    # закрываем браузер после всех манипуляций
browser.quit()
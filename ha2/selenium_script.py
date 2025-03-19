from selenium.webdriver.common.by import By
from selenium import webdriver
import time


driver = webdriver.Chrome()

driver.get("https://itcareerhub.de/ru")

about_link = driver.find_element(By.LINK_TEXT, 'Способы оплаты')
about_link.click()
time.sleep(5)
driver.save_screenshot("./screen/file.png")


time.sleep(5)
driver.quit()
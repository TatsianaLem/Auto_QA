from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import  time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/droppable/")
driver.switch_to.frame(driver.find_element(By.TAG_NAME, 'iframe'))

source = driver.find_element(By.ID, 'draggable')
target = driver.find_element(By.ID, 'droppable')

action = ActionChains(driver)
action.drag_and_drop(source, target).perform()

droped_text = target.text
assert droped_text == "Dropped!"
time.sleep(3)
print("Тест пройден: Фотография успешно перемещена в корзину и в основной области осталось 3 фотографии.")

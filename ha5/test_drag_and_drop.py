import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_drag_and_drop(driver):
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")

    # Переключиться на iframe
    driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))

    # Найти элементы
    source_image = driver.find_element(By.XPATH, "//li[contains(@class, 'ui-widget-content')][1]")
    trash_area = driver.find_element(By.XPATH, "//div[@id='trash']")

    actions = ActionChains(driver)
    actions.drag_and_drop(source_image, trash_area).perform()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//li[contains(@class, 'ui-widget-content') and contains(text(), 'Photo')]"))
    )

    remaining_photos = driver.find_elements(By.XPATH, "//li[contains(@class, 'ui-widget-content')]")
    assert len(remaining_photos) == 3, "В основной области должно остаться 3 фотографии."

    print("Фотография успешно перемещена в корзину, и в основной области осталось 3 фотографии.")
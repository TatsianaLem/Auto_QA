import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_text_input(driver):
    driver.get("http://uitestingplayground.com/textinput")

    text_input = driver.find_element(By.ID, "newButtonName")
    text_input.clear()
    text_input.send_keys("ITCH")

    button = driver.find_element(By.XPATH, '//button[@id="updatingButton"]')
    button.click()

    time.sleep(2)
    button_text = button.text

    assert button_text == "ITCH", f"Ожидался 'ITCH', но найден '{button_text}'"
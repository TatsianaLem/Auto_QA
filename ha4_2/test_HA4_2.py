import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait



@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_loading_images(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")


    WebDriverWait(driver, 10).until(lambda d: len(d.find_elements(By.TAG_NAME, "img")) >= 3)


    images = driver.find_elements(By.TAG_NAME, "img")
    assert len(images) >= 3, f"Ожидалось 3 изображения, но найдено {len(images)}"


    for i, img in enumerate(images):
        print(f"Изображение {i+1}: alt='{img.get_attribute('alt')}', src='{img.get_attribute('src')}'")


    expected_alt = "calendar"
    calendar_image = next((img for img in images if img.get_attribute("alt") == expected_alt), None)

    assert calendar_image is not None, f"Изображение с alt='{expected_alt}' не найдено"

    print("✅ Тест успешно пройден!")
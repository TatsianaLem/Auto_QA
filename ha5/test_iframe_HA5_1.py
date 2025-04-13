import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


def test_iframe(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")

    iframe = browser.find_element(By.ID, "my-iframe")
    browser.switch_to.frame(iframe)
    paragraphs = browser.find_elements(By.CLASS_NAME, "Lead")
    assert paragraphs

    exp_text = 'doler sit amet consectetur adipiscing elit habitant metus, tincidunt maecenas'

    count = 0
    for i in paragraphs:
        if exp_text in i.text:
            count+=1

    assert count > 0




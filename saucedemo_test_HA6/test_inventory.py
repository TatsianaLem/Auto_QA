import pytest
from selenium import webdriver
from inventory_page import InventoryPage


class TestSauceDemo:
    @pytest.fixture(scope="class")
    def setup(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        yield driver
        driver.quit()

    def test_checkout(self, setup):
        inventory_page = InventoryPage(setup)
        inventory_page.open()
        inventory_page.login("standard_user", "secret_sauce")
        inventory_page.add_items_to_cart()
        inventory_page.go_to_cart()
        inventory_page.checkout()
        inventory_page.fill_checkout_form("John", "Doe", "12345")

        total = inventory_page.get_total()
        assert total == "Total: $58.29", f"Expected total to be $58.29 but got {total}"
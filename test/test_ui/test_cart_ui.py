import allure
import pytest

from pages.cart_page import CartPage


@allure.feature("Коризна")
@pytest.mark.ui
class TestCart:

    @staticmethod
    @allure.title("Пустая корзина для нового пользователя")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.cart
    def test_empty_cart(browser):
        cart_page = CartPage(browser)
        cart_page.empty_cart_test()

    @staticmethod
    @allure.title("Проверка стоимости корзины")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.cart
    def test_cart_price(browser):
        cart_page = CartPage(browser)
        cart_page.cart_price_test()

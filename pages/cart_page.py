from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from config import config
import allure


class CartPage(BasePage):
    cart_icon = (By.CSS_SELECTOR, '[class="header-cart sticky-header__controls-item"]')
    cart_text = (
        By.CSS_SELECTOR, '[class="app-title app-title--mounted cart-page__title app-title--header-1 app-title--caps"]')
    empty_cart_text = (By.CSS_SELECTOR, '[class="empty-title"]')
    added_item_title = (By.CSS_SELECTOR, '[class="app-title__append"]')
    checkout_button = (By.CSS_SELECTOR, '[class="button cart-sidebar__order-button blue"]')
    price_checkout = (By.CSS_SELECTOR, '[class="cart-sidebar__info-summary"]')
    cart_page_url = config.get('BASE_URL') + 'cart'

    def go_to_cart_from_menu(self):
        with allure.step("Переход в к корзине из меню"):
            cart_icon = self.find_element(self.cart_icon)
            cart_icon.click()
            self.make_screenshot('Переход к корзине из меню')

    def open_cart_page(self):
        with allure.step("Переход в к корзине по ссылке"):
            self.open(self.cart_page_url)
            self.make_screenshot('Страница корзины')

    def check_cart_loaded(self):
        with allure.step("Проверка загрузки корзины"):
            self.find_element(self.cart_text)
            current_url = self.get_current_url()
            self.make_screenshot('Проверка загрузки корзины')
            assert current_url == self.cart_page_url, 'Url корзины отличается от ожидаемого'

    def check_cart_empty(self):
        with allure.step("Проверка пустой корзины"):
            self.check_cart_loaded()
            empty_cart = self.find_element(self.empty_cart_text)
            assert empty_cart.text == 'В корзине ничего нет'

    def check_cart_price(self):
        with allure.step("Проверка стоимости корзины"):
            self.find_element(self.added_item_title)
            self.find_element(self.checkout_button)
            price = self.find_element(self.price_checkout)
            price = price.find_element(By.CSS_SELECTOR, '[class=info-item__value]')
            assert self.book_price == price.text

    def empty_cart_test(self):
        self.open_cart_page()
        self.click_im_here()
        self.check_cart_loaded()

    def cart_price_test(self):
        self.open_book_page()
        self.add_book()
        self.go_to_cart_from_menu()
        self.check_cart_price()

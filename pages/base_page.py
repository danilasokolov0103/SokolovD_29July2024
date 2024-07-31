import time

import allure

from driver import Driver
from config import config
from selenium.webdriver.common.by import By


class BasePage(Driver):
    button_im_here_yes = (By.CSS_SELECTOR, '[class*="button change-city__button change-city__button--accept"]')
    buy_books_button = (By.CSS_SELECTOR, '[class*="button action-button"]')
    buy_book_button = (By.CSS_SELECTOR,
                       '[class="product-offer-button chg-app-button chg-app-button--primary '
                       'chg-app-button--extra-large chg-app-button--brand-blue chg-app-button--block"]')

    book_url = "product/python-s-nulya-3028159?productShelf=&shelfIndex=0&productIndex=2"
    book_price_with_discount = (
        By.CSS_SELECTOR, '[class="product-offer-price__current product-offer-price__current--discount"]')
    book_price = ''

    def open_book_page(self):
        with allure.step("Переход на страницу с книгой"):
            self.open(config.get('BASE_URL') + self.book_url)
            self.make_screenshot('Открыть страницу с книгой')
        with allure.step("Получим стоимость книги со скидкой"):
            book_price_element = self.find_element(self.book_price_with_discount)
            book_price = book_price_element.text
            self.book_price = book_price

    def click_im_here(self):
        with allure.step("Клик на выбор города"):
            button = self.find_element(self.button_im_here_yes)
            button.click()
            self.make_screenshot('Клик на выбор города')

    def add_book(self):
        with allure.step("Добавление кинги в корзину"):
            book = self.find_element(self.buy_book_button)
            book.click()
            self.make_screenshot('Добавить книгу в корзину')

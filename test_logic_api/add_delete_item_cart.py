import allure

from helpers.utils import attach_data
from helpers.api_client.cart import get_cart, add_item, delete_item


def check_add_item_to_cart(goods_id):
    with allure.step("Получить информацию о товарах в корзине"):
        response = get_cart()
        assert response.status_code == 200, (
            f"Не удается получить информацию "
            f"о корзине"
            f" Ошибка {response.status_code}, "
            f"сообщение {response.text}"
        )
        attach_data(response, 'Информация о корзине')
        products_count = len(response.json()['products'])
    with allure.step("Добавим товар в корзину"):
        response = add_item(goods_id)
        assert response.status_code == 200, (
            f"Не удается добавить товар"
            f" Ошибка {response.status_code}, "
            f"сообщение {response.text}"
        )
    with allure.step("Получить информацию о товарах в корзине"):
        response = get_cart()
        assert response.status_code == 200, (
            f"Не удается получить информацию "
            f"о корзине"
            f" Ошибка {response.status_code}, "
            f"сообщение {response.text}"
        )
        attach_data(response, 'Информация о корзине')
        new_products_count = len(response.json()['products'])
        assert products_count + 1 == new_products_count, 'Число товаров в корзине не совпадает с ожидаемым результатом'
        assert response.json()['cost'], 'Стоимость корзины равна нулю'
        assert response.json()['costWithBonuses'], 'Стоимость корзины c учетом бонусов равна нулю'
        assert response.json()['costWithSale'], 'Стоимость корзины c учетом скидок равна нулю'
        cart_item_id = response.json()['products'][0]['id']

        return cart_item_id


def check_delete_item_from_cart(cart_item_id):
    with allure.step("Удалим товар из корзины"):
        response = delete_item(cart_item_id)
        assert response.status_code == 204, (
            f"Не удается получить информацию "
            f"о корзине"
            f" Ошибка {response.status_code}, "
            f"сообщение {response.text}"
        )
    with allure.step("Проверим что корзина пуста"):
        response = get_cart()
        assert response.status_code == 200, (
            f"Не удается получить информацию "
            f"о корзине"
            f" Ошибка {response.status_code}, "
            f"сообщение {response.text}"
        )
        attach_data(response, 'Информация о корзине')
        products_count = len(response.json()['products'])
        assert not products_count, "В корзине присутствуют товары"

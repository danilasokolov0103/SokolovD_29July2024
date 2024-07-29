import allure

from helpers.utils import attach_data
from helpers.api_client.cart import get_cart, delete_all_items_in_cart
from test_logic_api.add_delete_item_cart import check_add_item_to_cart


def add_multiple_items(list_of_item_ids):
    for item_id in list_of_item_ids:
        check_add_item_to_cart(item_id)


def check_delete_all_items_from_cart():
    with allure.step("Удалим товар из корзины"):
        response = delete_all_items_in_cart()
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

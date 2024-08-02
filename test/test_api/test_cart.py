import pytest
import allure
from test_logic_api.add_delete_item_cart import check_add_item_to_cart, check_delete_item_from_cart
from test_logic_api.delete_all_items_cart import add_multiple_items, check_delete_all_items_from_cart

test_goods_ids = [3043197, 3046928]


@allure.feature("Коризна")
@pytest.mark.api
class TestCart:
    @staticmethod
    @pytest.mark.parametrize('goods_id', test_goods_ids)
    @allure.title("Добавление и удаление товаров из корзины")
    def test_add_item_to_cart(goods_id):
        cart_item_id = check_add_item_to_cart(goods_id)
        check_delete_item_from_cart(cart_item_id)

    @staticmethod
    @allure.title("Удаление всех товаров из корзины")
    def test_delete_all_items_in_cart():
        add_multiple_items(test_goods_ids)
        check_delete_all_items_from_cart()

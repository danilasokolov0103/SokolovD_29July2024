from helpers.client.chitay_gorod_client import chitay_gorod_client


def get_cart():
    url = "cart"
    response = chitay_gorod_client.base_api("get", url=url)
    return response


def delete_item(item_id):
    url = f"cart/product/{item_id}"
    response = chitay_gorod_client.base_api("delete", url=url)
    return response


def add_item(goodsId):
    url = "cart/product"
    data = {"id": goodsId, "adData": {"item_list_name": "catalog-main", "product_shelf": ""}}
    response = chitay_gorod_client.base_api("post", url=url, data=data)
    return response


def delete_all_items_in_cart():
    url = "cart"
    response = chitay_gorod_client.base_api("delete", url=url)
    return response

from ssqaapitest.src.dao.products_dao import ProductDao
from ssqaapitest.src.utilities.requestsUtility import RequestsUtility
from ssqaapitest.src.helpers.products_helper import ProductsHelper
import pytest

def test_get_all_products():
    products_obj = RequestsUtility()
    # get email from the DB
    product_api_info = products_obj.get('products')

    # assert validation to the response
    assert product_api_info, "product list is empty"

def test_get_product_by_id():
    product_dao = ProductDao()
    product_api_info = RequestsUtility()
    product_helper = ProductsHelper()
    # get a product from DB
    product = product_dao.get_random_product_from_db(1)
    product_res = product_helper.get_product_by_id(product[0]['ID'])

    assert product_res['name'] == product[0]['post_title']



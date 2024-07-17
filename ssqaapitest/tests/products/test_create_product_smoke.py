from ssqaapitest.src.helpers.products_helper import ProductsHelper
from ssqaapitest.src.utilities.genericUtilities import generate_random_name
from ssqaapitest.src.dao.products_dao import ProductDao


def test_create_1_simple_product():

    pass
    #create data
    payload = {'name': generate_random_name(4), 'type':'simple', 'price': '29.22'}
    # create call
    product_helper = ProductsHelper()
    product_res = product_helper.create_product(payload)
    assert product_res['name'] == payload['name'], "the added product has the wrong name"

    product_dao = ProductDao()
    product = product_dao.get_product_from_db_by_id(product_res['id'])
    assert product_res['name'] == product[0]['post_title'], "the added product has the wrong name"




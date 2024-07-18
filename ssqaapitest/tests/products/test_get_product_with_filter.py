from pprint import pprint

import pytest
from datetime import datetime, timedelta
from ssqaapitest.src.helpers.products_helper import ProductsHelper
from ssqaapitest.src.dao.products_dao import ProductDao


class TestProductsWithFilter(object):

    def test_list_products_with_filter_after(self):
        x_days_from_today = 30

        after_created_days = datetime.now().replace(microsecond=0) - timedelta(days = x_days_from_today)
        after_created_days = after_created_days.isoformat()

        # after_created_days_2 = datetime.now().replace(microsecond=0) - timedelta(days = x_days_from_today)
        # after_created_days_2 = after_created_days_2.strftime('%Y-%M-%dT%H:%M:%S')

        payload = dict()
        payload['after'] =  after_created_days

        products = ProductsHelper()
        product_res = products.get_list_products(payload = payload)
        assert product_res

        product_dao = ProductDao()
        list_of_products_from_db = product_dao.get_list_of_product_by_dat_post(after_created_days)
        assert len(list_of_products_from_db) == len(product_res)

        db_ids = [x['ID'] for x in list_of_products_from_db ]
        api_ids = [x['id'] for x in product_res]

        assert set(db_ids) == set(api_ids)
        id_diff = list(set(db_ids) - set(api_ids))
        assert not id_diff




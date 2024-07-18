from ssqaapitest.src.utilities.requestsUtility import RequestsUtility
import logging as logger


class ProductsHelper(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()

    def get_product_by_id(self, id , **kwargs):

        return self.requests_utility.get(f'products/{id}')

    def get_list_products(self, payload = None):
        max_pages = 1000
        all_products = []
        for i in range(1, max_pages + 1):
            logger.debug(f"List products page: {i}")
            if not 'per_page' in payload.keys():
                payload['per_page'] = 100
            payload['page'] = i
            rs_api = self.requests_utility.get('products', payload = payload, expected_status_code=200)
            if not rs_api:
                break
            else:
                all_products.extend(rs_api)
        else:
            raise Exception(f"unable to fins all products after {max_pages} pages.")

        return all_products

    def create_product(self, payload):

        return self.requests_utility.post('products', payload = payload, expected_status_code=201)
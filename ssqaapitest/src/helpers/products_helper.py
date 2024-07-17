from ssqaapitest.src.utilities.requestsUtility import RequestsUtility



class ProductsHelper(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()

    def get_product_by_id(self, id , **kwargs):

        return self.requests_utility.post(f'products/{id}')


    def create_product(self, payload):
        return self.requests_utility.post('products', payload = payload, expected_status_code=201)
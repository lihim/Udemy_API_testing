from ssqaapitest.src.utilities.requestsUtility import CredentialsUtility
import os
from ssqaapitest.configs.hosts_config import WOO_API_HOSTS
from woocommerce import API
import logging as logger


class WooAPIUtility(object):
    def __init__(self):
        wc_creds = CredentialsUtility.get_wc_api_keys()
        self.env = os.environ.get('ENV', 'test')
        self.base_url = WOO_API_HOSTS[self.env]
        self.wcapi = API(
            url=self.base_url,
            consumer_key=wc_creds['wc_key'],
            consumer_secret=wc_creds['wc_secret'],
            version="wc/v3"
        )


    def get(self, wc_endpoint, params = None, expected_status_code=200):
        rs_api = self.wcapi.get(wc_endpoint, params=params)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()
        logger.info(f"POST API response: {rs_api.json()}")
        return self.rs_json

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, f"Bad Status code." \
                                                              f"Expected {self.expected_status_code}, Actual status code: {self.status_code}," \
                                                              f"URL: {self.url}, Response Json: {self.rs_json}"


if __name__ == '__main__':
    obj = WooAPIUtility()
    rs_api = obj.get('products')
    print(rs_api)
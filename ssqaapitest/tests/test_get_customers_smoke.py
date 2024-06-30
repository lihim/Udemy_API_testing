from pprint import pprint

import  pytest
from ssqaapitest.src.utilities.requestsUtility import RequestsUtility
import logging as logger


@pytest.mark.tcid30
def test_get_all_customers():
    req_hellper = RequestsUtility()
    rs_api = req_hellper.get('customers')

    pprint(rs_api)

    assert rs_api, f"Response of list all customers is empty."


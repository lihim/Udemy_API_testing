
import pytest
import logging
from ssqaapitest.src.utilities.genericUtilities import generate_random_email_and_password
from ssqaapitest.src.helpers.customers_helper import CustomerHelper
logger = logging.getLogger('MyLogger')
@pytest.mark.customers
@pytest.mark.tcid29
def test_create_customer_only_email_password():

    logger.info("TEST: Create new customer with email and password only.")

    rand_info = generate_random_email_and_password()
    email = rand_info['email']
    password = rand_info['password']

    cust_obj = CustomerHelper()
    cust_api_info = cust_obj.create_customer(email=email, password=password)
    assert cust_api_info['email'] == email, f"Create customer api return wrong email. Email: {email}"
    assert cust_api_info['first_name'] == '', f"Create customer api returned value for first_name" \
                                              f"but it should be empty. "

    logger.info(cust_api_info)
    print('\n' + str(rand_info))
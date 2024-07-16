import pytest
import logging
from ssqaapitest.src.utilities.genericUtilities import generate_random_email_and_password
from ssqaapitest.src.helpers.customers_helper import CustomerHelper
from ssqaapitest.src.utilities.requestsUtility import RequestsUtility

from ssqaapitest.src.dao.customers_dao import CustomersDAO

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

    customer_dao = CustomersDAO()
    cust_info = customer_dao.get_customer_by_email(email)

    id_in_api = cust_api_info['id']
    id_in_db = cust_info[0]['ID']
    assert id_in_api == id_in_db, f'Create customer response "id" not same as "ID" in database.' \
                                  f'Email: {email}'

    logger.info(cust_api_info)
    print('\n' + str(rand_info))


@pytest.mark.customers
def test_create_customer_fail_for_existing_email():
    # get email from the DB
    cust_dao = CustomersDAO()
    existing_cust = cust_dao.get_random_customer_from_db()
    existing_email = existing_cust[0]['user_email']

    # trying to create new user with existing email - To fail
    cust_obj = RequestsUtility()
    payload = {'email': existing_email, 'password': "Password"}
    cust_api_info = cust_obj.post('customers', payload=payload, expected_status_code=400)

    # assert validation to the response
    assert cust_api_info['code'] == 'registration-error-email-exists', f"Create customer with" \
                                                                       f"existing user error 'code' is not correct. Expected: 'registration-error-email-exists', " \
                                                                       f"Actual: {cust_api_info['code']}"

    assert cust_api_info[
               'message'] == 'An account is already registered with your email address. <a href="#" class="showlogin">Please log in.</a>', \
        f"Create customer with existing user error 'message' is not correct. " \
        f"Expected: 'An account is already registered with your email address. Please log in.', " \
        f"Actual: {cust_api_info['message']}"


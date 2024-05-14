import pytest
import logging as logger
from wooapitest.src.helpers.customers_helper import CustomersHelper
from wooapitest.src.utils.generic_utils import generate_random_email
from wooapitest.src.dao.customers_dao import CustomersDAO
from wooapitest.src.utils.request_utils import RequestsUtility


@pytest.fixture(scope="module")
def my_setup():
    print("Set Up Method")


@pytest.mark.customers
@pytest.mark.TC1
def test_create_new_customer(my_setup):
    logger.info("Create new customer")
    email = generate_random_email()

    logger.debug(f"Generated Email in test is: {email}")
    cust_obj = CustomersHelper()
    cust_api_info = cust_obj.create_customer(email)

    assert cust_api_info["email"] == email, f"Create customer api returns wrong email address."

    cust_dao = CustomersDAO()
    cust_db_info = cust_dao.get_customer_by_email(email)

    customer_id_api = cust_api_info['id']
    customer_id_db = cust_db_info[0]['ID']
    assert customer_id_api == customer_id_db, f"Created customer response from db not same as id " \
                                              f"in API for email {email}"


@pytest.mark.customers
@pytest.mark.TC2
def test_create_new_customer_with_existing_email(my_setup):
    logger.info("Create new customer with existing email address")

    cust_dao = CustomersDAO()
    existing_cust_db_info = cust_dao.get_random_customer_from_db()
    existing_email = existing_cust_db_info[0]['user_email']

    payload = {"email": existing_email}
    req_helper = RequestsUtility()
    rs_json = req_helper.post(endpoint='customers', payload=payload, expected_status_code=400)

    assert rs_json["code"] == "registration-error-email-exists", f"code value in response did not match"
    assert rs_json[
               "message"] == 'An account is already registered with your email address. <a href="#" class="showlogin">Please log in.</a>', f"message value in response did not match"
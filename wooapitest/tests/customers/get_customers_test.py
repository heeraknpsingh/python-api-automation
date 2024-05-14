import pytest
from wooapitest.src.utils.request_utils import RequestsUtility


@pytest.fixture(scope="module")
def my_setup():
    print("Set Up Method")


@pytest.mark.customers
@pytest.mark.TC3
def test_get_all_customers(my_setup):
    req_helper = RequestsUtility()
    rs_api = req_helper.get('customers')
    assert len(rs_api) > 1, f"Response of list of all customers is empty."

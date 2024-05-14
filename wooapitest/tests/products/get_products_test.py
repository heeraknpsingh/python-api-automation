import pytest
from wooapitest.src.utils.request_utils import RequestsUtility
from wooapitest.src.dao.products_dao import ProductsDAO
from wooapitest.src.helpers.products_helper import ProductsHelper


@pytest.fixture(scope="module")
def my_setup():
    print("Set Up Method")


@pytest.mark.products
@pytest.mark.TC4
def test_get_all_products(my_setup):
    req_helper = RequestsUtility()
    rs_api = req_helper.get('products')
    assert len(rs_api) > 1, f"Response of list of all products is empty."


@pytest.mark.products
@pytest.mark.TC5
def test_get_product_by_id(my_setup):
    rand_product_db = ProductsDAO().get_random_product_from_db(1)
    rand_product_id_db = rand_product_db[0]["ID"]
    rand_product_title_db = rand_product_db[0]["post_title"]

    product_helper = ProductsHelper()
    rs_api = product_helper.get_product_by_id(rand_product_id_db)
    product_name_api = rs_api['name']

    assert rand_product_title_db == product_name_api, f"name of product did not match" \
                                                      f"From db {rand_product_title_db}" \
                                                      f"From api {product_name_api}"

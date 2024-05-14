import logging as logger
from wooapitest.src.utils.request_utils import RequestsUtility
from wooapitest.src.utils.generic_utils import generate_random_email


class ProductsHelper:
    def __init__(self):
        self.req_utils = RequestsUtility()

    def get_product_by_id(self, product_id):
        return self.req_utils.get(endpoint=f'products/{product_id}')
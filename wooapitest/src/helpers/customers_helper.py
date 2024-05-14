import logging as logger
from wooapitest.src.utils.request_utils import RequestsUtility
from wooapitest.src.utils.generic_utils import generate_random_email


class CustomersHelper:
    def __init__(self):
        self.req_utils = RequestsUtility()

    def create_customer(self, email=None, **kwargs):
        logger.debug(f"Inside create_customer method: email is {email}")
        if not email:
            email = generate_random_email()

        payload = dict()
        payload['email'] = email

        payload.update(kwargs)
        logger.info(f"Passed payload for create customer: {payload}")

        return self.req_utils.post(endpoint='customers', payload=payload, expected_status_code=201)
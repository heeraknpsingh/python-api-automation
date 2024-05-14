import random
import string
import logging as logger


def generate_random_email(domain=None, email_prefix=None):
    logger.debug("Generating random email address for a new customer.")

    if not domain:
        domain = "mailinator.com"
    if not email_prefix:
        email_prefix = "qa_auto_api"

    random_email_string_length = 10
    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_length))
    email = email_prefix + '_' + random_string + "@" + domain

    logger.debug(f"Generated random customer email is: {email}")
    return email


def generate_random_string(length=10, prefix=None, suffix=None):
    random_string = ''.join(random.choices(string.ascii_lowercase, k=length))

    if prefix:
        random_string = prefix + random_string
    if suffix:
        random_string = random_string + suffix

    return random_string

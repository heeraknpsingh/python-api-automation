import random
from wooapitest.src.utils.db_utils import DBUtility


class CustomersDAO(object):
    def __init__(self):
        self.db_helper = DBUtility()

    def get_customer_by_email(self, email):
        sql = f"select * from coolsite.wp_users where user_email='{email}'"
        rs_sql = self.db_helper.execute_select_query(sql)
        return rs_sql

    def get_random_customer_from_db(self, qty=1):
        sql = f"select * from coolsite.wp_users order by id limit 10"
        rs_sql = self.db_helper.execute_select_query(sql)
        return random.sample(rs_sql, int(qty))
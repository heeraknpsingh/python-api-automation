import random
from wooapitest.src.utils.db_utils import DBUtility


class ProductsDAO(object):
    def __init__(self):
        self.db_helper = DBUtility()

    def get_random_product_from_db(self, qty=1):
        sql = f"select * from coolsite.wp_posts where post_type='product' limit 10"
        rs_sql = self.db_helper.execute_select_query(sql)
        return random.sample(rs_sql, int(qty))
import random

from ssqaapitest.src.utilities.dbUtility import DBUtility


class ProductDao(object):
    def __init__(self):
        self.db_helper = DBUtility()

    def get_random_product_from_db(self, quantity=1):
        sql = f"select * from `local`.wp_posts where post_type='product' order by rand() desc limit 5000"
        rs_sql = self.db_helper.execute_select(sql)
        return random.sample(rs_sql, int(quantity))

    def get_product_from_db_by_id(self, id=1):
        sql = f"select * from `local`.wp_posts where id='{id}'"
        rs_sql = self.db_helper.execute_select(sql)
        return rs_sql

    def get_list_of_product_by_dat_post(self, time):
        sql = f"select * from `local`.wp_posts where post_type = 'product' and post_date > '{time}'"
        return self.db_helper.execute_select(sql)
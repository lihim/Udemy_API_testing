import random

from ssqaapitest.src.utilities.dbUtility import DBUtility


class CustomersDAO(object):
    def __init__(self):
        self.db_helper = DBUtility()

    def get_customer_by_email(self, email):
        sql = f"select * from `local`.wp_users wu where user_email = '{email}'"
        rs_sql = self.db_helper.execute_select(sql)
        return rs_sql

    def get_random_customer_from_db(self, quantity=1):
        sql = "select * from `local`.wp_users order by rand() desc limit 5000"
        rs_sql = self.db_helper.execute_select(sql)
        return random.sample(rs_sql, int(quantity))

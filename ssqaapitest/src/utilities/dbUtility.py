import pymysql
from ssqaapitest.src.utilities.credentialsUtility import CredentialsUtility
import logging as logger


class DBUtility(object):
    def __init__(self):
        creds_helper = CredentialsUtility()
        self.creds = creds_helper.get_db_credentisls()
        self.host = 'localhost'

    def create_cnnection(self):
        connection = pymysql.connect(host=self.host, user=self.creds['db_user'], password=self.creds['db_password'],
                                     port=10006)
        return connection

    def execute_select(self, sql):
        conn = self.create_cnnection()
        try:
            logger.debug(f"Executing: {sql}")
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            rs_dict = cur.fetchall()
            cur.close()
        except Exception as e:
            raise Exception(f"Failed running sql: {sql} \n  Error: {str(e)}")
        finally:
            conn.close()

        return rs_dict



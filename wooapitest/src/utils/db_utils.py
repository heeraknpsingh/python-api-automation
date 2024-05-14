import pymysql
import logging as logger
from wooapitest.src.utils.credentials_utils import CredentialsUtility
from wooapitest.src.configs.hosts_config import DB_HOSTS


class DBUtility(object):
    def __init__(self):
        creds_helper = CredentialsUtility()
        self.host = DB_HOSTS["dev"]
        self.creds = creds_helper.get_db_credentials()
        self.socket = ''

    def create_connection(self):
        connection = pymysql.connect(host=self.host['host'],
                                     user=self.creds['db_user'],
                                     password=self.creds['db_password'],
                                     port=int(self.host['port']))
        return connection

    def execute_select_query(self, query):
        logger.debug(f"Executing query: {query}")
        conn = self.create_connection()
        try:
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(query)
            rs_dict = cur.fetchall()
            cur.close()
        except Exception as e:
            raise Exception(f"Error in running query: {query} \n Error is {str(e)}")
        finally:
            conn.close()
        logger.debug(f"DB query response is: {rs_dict}")
        return rs_dict


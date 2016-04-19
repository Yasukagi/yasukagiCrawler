# coding:utf-8
import Crowler
import DatabaseSetter
# constant
DB_USER = "root"
if __name__ == "__main__":

    appList = Crowler.crowlApp()
    response = DatabaseSetter.execute_sql(appList)
    print response


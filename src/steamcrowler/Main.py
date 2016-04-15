# coding:utf-8
import Crowler
import DatabaseSetter
# constant
DB_USER = "root"

appList = Crowler.crowlApp()
response = DatabaseSetter.execute_sql(appList)
print response


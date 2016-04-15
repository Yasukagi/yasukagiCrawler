# coding:utf-8
import MySQLdb
import json



# constant
DB_USER = "root"


def execute_sql(appList):
    connection = MySQLdb.connect(host='localhost', user="root", db="test", charset='utf8')
    print "success to connect"
    cursor = connection.cursor()
    print json.dumps(appList[0])
    #print json.dumps(appList[0])
    #header_string = 'game_title', 'game_price_steam', 'time_stamp'
    #print header_string
    #values = 'fuck', 0.0, timestring
    for app in appList:
        appid = json.dumps(app['appid'])
        name = json.dumps(app['name'])
        cursor.execute("INSERT INTO yasukagi_game ( game_id, game_title, game_price_steam, time_stamp) VALUES ( %s, %s, '1', CURRENT_TIMESTAMP )" % (appid, name))
    result = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return "inserted the data"




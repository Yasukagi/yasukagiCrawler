# coding:utf-8
import MySQLdb
import json



# constant
DB_USER = "root"

#appidとnameのキーのセット(api.steampowered)
def set_database(appList):
    print("データベースに接続しています...")
    connection = MySQLdb.connect(host='localhost', user="root", db="test", charset='utf8')
    print("success to connect")
    cursor = connection.cursor()

    #header_string = 'game_title', 'game_price_steam', 'time_stamp'
    #print header_string
    #values = 'fuck', 0.0, timestring
    print("データベースにappidおよびnameを登録しています")
    for app in appList:
        appid = json.dumps(app['appid'])
        name = json.dumps(app['name'])
        cursor.execute("INSERT INTO yasukagi_game ( game_id, game_title, game_price_steam, time_stamp ) VALUES ( %s, %s, 0, CURRENT_TIMESTAMP )" % (appid, name))
    result = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return "inserted the data"




# coding:utf-8

import MySQLdb

def getIds():
    connection = MySQLdb.connect(user='root',db='test')
    cursor = connection.cursor()

    cursor.execute("select game_id from yasukagi_game")
    result = cursor.fetchall()

    return result
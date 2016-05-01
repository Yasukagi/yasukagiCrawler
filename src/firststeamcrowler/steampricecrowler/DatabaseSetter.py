# coding:utf-8
import MySQLdb as msd

def set_database(row):
    connection = msd.connect(user='root', db='test')
    cursor = connection.cursor()

    cursor.execute("UPDATE yasukagi_game SET game_price_steam = %s , is_game = %s WHERE game_id = %s ", (row['initialPrice']/100, row['is_game'], row['appid'] ))
    connection.commit()


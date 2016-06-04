import MySQLdb as msd
import json
import urllib2 as ul2


connection = msd.connect(host='localhost', user='root', db='test')
cursor = connection.cursor()
sql = "SELECT game_id from yasukagi_game"
cursor.execute(sql)
app_List_before = cursor.fetchall()
response = ul2.urlopen("http://api.steampowered.com/ISteamApps/GetAppList/v0001/")
steamAppJson = json.load(response)
appList = steamAppJson['applist']['apps']['app']


for i in xrange(len(app_List_before)):
    sql = "UPDATE yasukagi_game SET steam_app_List_before "
    cursor.execute()


for i in range(len(app_List_before), len(appList)):



print len(app_List_before)
print len(appList)

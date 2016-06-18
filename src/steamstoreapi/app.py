import urllib.request as ulr
import json
import time
import steamstoreapi

class App:

    def applist(self):
        url = "http://api.steampowered.com/ISteamApps/GetAppList/v0001/"
        response = ulr.urlopen(url)
        applistjson = json.loads(response.read().decode('utf-8'))
        appList = applistjson['applist']['apps']['app']

        return appList

class AppList:
    def __init__(self, appList):
        self.appList = appList
        self.list = dict()
        for app in appList:
            self.list[app["appid"]] = app["name"]
        print(self.list)


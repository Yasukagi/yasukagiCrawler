import urllib.request as ulr
import json
import time

class App:

    def applist(self):
        url = "http://api.steampowered.com/ISteamApps/GetAppList/v0001/"
        response = ulr.urlopen(url)
        applistjson = json.loads(response.read())
        appList = applistjson['applist']['apps']['app']

        return AppList(appList)

class AppList:
    def __init__(self, appList):
        self.appList = appList
        self.list = {}
        for app in appList:
            self.list[app["appid"]] = app["name"]
        print(self.list)


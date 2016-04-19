# coding:utf-8
import urllib2 as ul2
import json
import time

#最初に走らせる
def crowlApp():
    #steamAppidと名前を取得
    steamAppResponse = open("steamAppResponse.json", 'r')
    #steamAppResponse = ul2.urlopen("http://api.steampowered.com/ISteamApps/GetAppList/v0001/")
    #steamAppResponseはapplist{apps{app[{appid,name},...]}}}となっている
    steamAppJson = json.load(steamAppResponse)
    appList = steamAppJson['applist']['apps']['app']
    print json.dumps(appList[0])
    return appList

    appids = []
    #steam
    appidspart = ""

    for i in xrange(len(appList)):
        if i % 500 == 0:
            appids.append(appidspart)
            appidspart = ""
        appidspart = appidspart + json.dumps(appList[i]['appid']) + ","

    for i in xrange(len(appids)):
        time.sleep(1)
        steamPriceResponse = ul2.urlopen('http://store.steampowered.com/api/appdetails/?appids='+ appids[i] +'&filters=price_overview')
        steamPriceJson = json.load(steamPriceResponse)
        print str(i) + steamPriceJson

    for i in xrange(len(appList)):
        print "fuck" + json.dumps(appList[i])
        appidjson = appList[i]['appid']
        appid = json.dumps(appidjson)

        appInformation = json.load(steamPriceResponse)
        #respomse is {{"730":{"success":true,"data":{"price_overview":{"currency":,"initial":,"final":,"discount_percent":}}}}}
        if appInformation[appid]['success'] == False:
            appList[i]['game_price_steam'] = 0
            appList[i]['is_game'] = False
        else:
            appDataInformations = appInformation[appid]['data']
            if 'price_overview' in appDataInformations:
                appPriceInformations = appDataInformations['price_overview']
                appList[i]['game_price_steam'] = appPriceInformations['initial']/100
                appList[i]['is_game'] = True
            else:
                appList[i]['game_price_steam'] = 0
                appList[i]['is_game'] = False
        print "shit" + json.dumps(appList[i])
    return appList


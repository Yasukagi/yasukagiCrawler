import steam
import json
import steamstoreapi
import steamapi
import time
import dao.steamdao as steamdb
import ast

def crowl():
    print("DB:dbに接続")
    f = open("/Users/TOSUKUi/ideaProject/yasukagiCrowler/src/crowlexecuter/prices", "r")
    db = steamdb.SteamDao(user="root", host="localhost")
    print("API:appListにアクセス")
    appList = crowlapps()
    #crowlprices(appList)
    store = steamstoreapi.store.Store()
    appids = []
    length = len(appList)
    for i in range(length):
        appids.append(appList[i]["appid"])
    print("価格情報を取得しています")
    #prices = crowlprices(appids)

    prices = ast.literal_eval(f.read())
    games = {}
    print("ゲームの情報を取得しています。")
    for appid in prices:
        if prices[appid]["success"] == True:
            appdetails = crowldetails([appid])
            db.insertDetails(appdetails[appid])
    db.commit()




    #appdetail = store.appdetails("730")
    #print(appList)
    #print(appdetail.developers)


def crowlapps():
    app = steamstoreapi.app.App()
    appList = app.applist()
    return appList

def crowlprices(appids):
    store = steamstoreapi.store.Store()
    appids_part = ""
    length = len(appids)
    prices = dict()
    for i in range(length):
        appids_part += str(appids[i]) + ","
        if length == 1:
            price = store.appprices(appids=appids_part)
            prices.update(price)
        elif i % 250 == 0 or i == length - 1:
            price = store.appprices(appids=appids_part)
            prices.update(price)
            appids_part = ""
    return prices



def crowldetails(appids):
    store = steamstoreapi.store.Store()
    details = {}
    for appid in appids:
        details[appid] = store.appdetails(appid)
    return details

def getDatabase():
    return
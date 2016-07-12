import steamstoreapi
import dao.steamdao as steamdb
import ast
import sys

def crowl():
    appids = []
    print("DB:dbに接続")
    db = steamdb.SteamDao(user="root", host="localhost")
    print("API:appListにアクセス")
    appList = crowlapps()
    #appListをつなげて，価格を取得するメソッドの引数に格納.
    length = len(appList)
    for i in range(length):
        appids.append(appList[i]["appid"])
    prices = crowlprices(appids)
    #pricesのうち，gameとして認識できるものに関して，情報を取得していく
    print("ゲームの情報を取得しています。")
    length = len(prices)
    count = 0
    for appid in prices:
        count += 1
        progress = count/length * 100
        sys.stdout.write("\r%d" % progress)
        sys.stdout.flush()
        if prices[appid]["success"]:
            if "price_overview" in prices[appid]["data"]:
                appdetails = crowldetails([appid])
                try:
                    db.insert_details(appdetails[appid])
                except Exception as e:
                    print("problem occured appid", appid, e, sep=":")
    db.commit()



def crowlapps():
    app = steamstoreapi.app.App()
    appList = app.applist()
    return appList
"""
価格を取得してくるメソッド.
@:param appids appidのリスト
@:return prices [appid:{priceデータ},...]の形のdictオブジェクト
"""
def crowlprices(appids):
    store = steamstoreapi.store.Store()
    appids_part = ""
    length = len(appids)
    prices = dict()
    for i in range(length):
        progress = i/length * 100
        sys.stdout.write("\r%d" % progress)
        sys.stdout.flush()
        appids_part += str(appids[i]) + ","
        if length == 1:
            price = store.appprices(appids=appids_part)
            prices.update(price)
        elif i % 250 == 0 or i == length - 1:
            price = store.appprices(appids=appids_part)
            prices.update(price)
            appids_part = ""

    return prices


"""
@:param appids appidのリスト
@:return details AppDetailsオブジェクト
appidをリストとして渡すと，appdetailsオブジェクトがリストとして返ってくる
"""
def crowldetails(appids):
    store = steamstoreapi.store.Store()
    details = {}
    for appid in appids:
        details[appid] = store.appdetails(appid)
    return details

def getDatabase():
    return
import steamstoreapi
import dao.steamdao as steamdb
import ast
import sys

def crowl():
    print("DB:dbに接続")
    #f = open("/Users/TOSUKUi/ideaProject/yasukagiCrowler/src/crowlexecuter/prices", "r")
    db = steamdb.SteamDao(user="root", host="localhost")
    print("API:appListにアクセス")
    appList = crowlapps()
    #crowlprices(appList)
    store = steamstoreapi.store.Store()
    appids = []
    #length = len(appList)
    #for i in range(length):
    #   appids.append(appList[i]["appid"])
    print("価格情報を取得しています")
    f = open("/Users/TOSUKUi/ideaProject/yasukagiCrowler/list.txt","r")

    for appid in f.readlines():
        appid = appid.strip()
        appids.append(appid)


    prices = crowlprices(appids)
    #f.write(str(prices))
    #f.close()
    #prices = ast.literal_eval(f.read())
    games = {}
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



def crowldetails(appids):
    store = steamstoreapi.store.Store()
    details = {}
    for appid in appids:
        details[appid] = store.appdetails(appid)
    return details

def getDatabase():
    return
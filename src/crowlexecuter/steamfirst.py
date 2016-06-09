import steam
import json
import steamstoreapi
import steamapi

def crowl():
    appList = crowlapps()
    store = steamstoreapi.store.Store()
    appdetail = store.appdetails("730")
    print(appList)
    print(appdetail.developers)


def crowlapps():
    app = steamapi.app.SteamApp()


    return app

def crowlprices(appids):
    store = steamstoreapi.store.Store()
    prices = store.appprices()
    return prices



def crowlheader_images(*appids):
    store = steamstoreapi.store.Store()
    header_images = {}
    for appid in appids:
        appdetail = store.appdetails(appid)
        header_images[appid] = appdetail.header_image

    return header_images


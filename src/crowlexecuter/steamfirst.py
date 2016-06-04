import steamapi
import json



def crowlapps():
    apps = steamapi.app.App()
    appList = apps.applist()
    return appList

def crowlprices(appids):
    store = steamapi.store.Store()
    prices = store.appprices()
    return prices

def crowlheader_images():
    return

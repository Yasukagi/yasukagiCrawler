# coding:utf-8
import firststeamcrowler.steamappcrowler.Crowler as appCrowler
import firststeamcrowler.steamappcrowler.DatabaseSetter as appDataSetter
import firststeamcrowler.steampricecrowler.Crowler as priceCrowler
import firststeamcrowler.steampricecrowler.DatabaseGetter as priceDataGetter
import firststeamcrowler.steampricecrowler.DatabaseSetter as priceDataSettera
#とりあえず最初に走らせるのがこのfirststeamcrowlerのMain.py
#これを走らせてdatabaseを初期化しよう
# constant
DB_USER = "root"
if __name__ == "__main__":

    appList = appCrowler.crowlApp()
    response = appDataSetter.set_database(appList)
    appIdList = priceDataGetter.getIds()
    for data in priceCrowler.crowl_prices(appIdList):
        priceDataSetter.set_database(data)



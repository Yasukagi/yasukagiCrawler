# coding:utf-8
import urllib2 as ul2
import json
import time
import firststeamcrowler

#steamのappidと商品もしくはappのnameの.組のjsonを返す.全部insertなのですでにdbにデータが入っている方は使ってはならない
def crowlApp():
    #steamAppidと名前を取得
    print "steamからappidと名前のリストを取得しています"
    steamAppResponse = ul2.urlopen("http://api.steampowered.com/ISteamApps/GetAppList/v0001/")
    #steamAppResponseはapplist{apps{app[{appid,name},...]}}}となっている
    steamAppJson = json.load(steamAppResponse)
    appList = steamAppJson['applist']['apps']['app' ]
    return appList



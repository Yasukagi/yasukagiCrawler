# coding:utf-8
import urllib2 as ul2
import json

#一日に一回か、1週間に一回くらい走らせるので良い
def crowlApp():
    steamAppResponse = ul2.urlopen("http://api.steampowered.com/ISteamApps/GetAppList/v0001/")
    #steamAppResponseはapplist{apps{app[{appid,name},...]}}}となっている
    steamAppJson = json.load(steamAppResponse)
    appList = steamAppJson['applist']['apps']['app']
    return appList


# coding:utf-8
import urllib2 as ul2
import json
import sys
import time


# steam

#この関数にアプリケーションIDのリストを((appid,),....)の形式のタプルで渡すと、そのすべての価格情報及びゲームかどうかを返してくれるメソッド.for文で回して下さい。一つのappidの情報ずつ帰ってきます
def crowl_prices(appList):

    #ローカルであまりsteamにクエリを出したくなかったのでjsonを一時保存していた
    #f = open()

    #諸々変数初期化
    appids = []
    appidspart = ""

    #steamのストアフロントapiのパラメータのappidはcsvに設定できるので、250個ほどのappidをcsvにまとめている。(500だと蹴られる)
    print "appidをまとめています"
    for i in xrange(len(appList)):
        if i % 250 == 0 or i == len(appList):
            appids.append(appidspart)
            appidspart = ""
        appidspart = appidspart + json.dumps(appList[i][0]) + ","
    print appids
    steamPriceJson = {}

    print "steamの価格を取り寄せています...."
    #steamのストアフロントapiからappの価格を取り寄せてくる部分
    for i in range(len(appids)):
        steamPriceResponse = ul2.urlopen('http://store.steampowered.com/api/appdetails/?appids=' + appids[i] + '&filters=price_overview')
        unko = json.load(steamPriceResponse)
        steamPriceJson.update(unko)
        #print unko
        #ディレイ不要
        # time.sleep(0)
        #  f.write(json.dumps(steamPriceJson))


    #steamPriceJson = json.load(f)
    #print f.read()

    #取り寄せたすべてのJsonをdata{'initialPrice':定価 ,'is_game':ゲームかどうか, 'appid':アプリケーションid}の形式でイテレイティブに返す
    for appid in steamPriceJson:
        steamPrice = steamPriceJson[appid]

        initialPrice = 0
        finalPrice = 0
        is_game = False
        if steamPrice['success'] == True:
            if 'price_overview' in steamPrice['data']:
                initialPrice = steamPrice['data']['price_overview']['initial']
                is_game = True
        data = {'initialPrice': initialPrice, 'is_game': is_game, 'appid': appid, }
        yield data


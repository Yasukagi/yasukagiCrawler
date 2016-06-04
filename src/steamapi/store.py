"""
steam app metadata
this file has two classes.
Store and AppDetails.
You usually use the class of Store.
AppDetails is called in Store class.
"""

import urllib.request as ulr
import json
import time

class Store:

    """
    steamの商品ページの情報を取得
    @param appid 文字列として単一のappidを挿入
    ["appid":{"success":, "data":{['supported_languages', 'categories', 'packages', 'metacritic', 'mac_requirements', 'steam_appid', 'recommendations', 'required_age', 'linux_requirements', 'is_free', 'background', 'name', 'release_date', 'support_info', 'developers', 's', 'publishers', 'type', 'achievements', 'pc_requirements', 'header_image', 'package_groups', 'about_the_game', 'screenshots', 'price_overview', 'detailed_description', 'website', 'controller_support', 'movies', 'genres']}}]
    """
    def appdetails(self, appid):
        url = 'http://store.steampowered.com/api/appdetails/?appids=' + appid
        try:
            response = ulr.urlopen(url)
        except:
            print("HTTP error")
            return
        try:
            appdetailsJson = json.loads(response.read().decode("utf-8"))
        except:
            print("... may be an args of appid is missed")
            return
        appdetail = None

        for appid in appdetailsJson:
            if appdetailsJson[appid]['success']:
                appdetail = appdetailsJson[appid]['data']
            else:
                appdetail = {}

        return AppDetails(appdetail)

    """
    steamの商品ページのうち、価格のみ取得できる
    これだけ何故かcsv形式でのappidsの指定が可能。
    @:param appids appidをcsv形式で入力
    """
    def appprices(self, appids):
        url = 'http://store.steampowered.com/api/appdetails/?appids=' + appids + '&filters=price_overview'
        try:
            response = ulr.urlopen(url)
        except:
            print("http error")
            return

        try:
            apppricesJson = json.loads(response.read().decode("utf-8"))
        except:
            print("json parse error")
        return apppricesJson

"""["appid":{"success":, "data":{['supported_languages', 'categories', 'packages', 'metacritic', 'mac_requirements', 'steam_appid', 'recommendations', 'required_age', 'linux_requirements', 'is_free', 'background', 'name', 'release_date', 'support_info', 'developers', 'platforms', 'publishers', 'type', 'achievements', 'pc_requirements', 'header_image', 'package_groups', 'about_the_game', 'screenshots', 'price_overview', 'detailed_description', 'website', 'controller_support', 'movies', 'genres']}}]"""
class AppDetails:
    def __init__(self,appdetails):
        if "supported_languages" in appdetails:
            self.supported_languages = appdetails["supported_languages"]
        else:
            self.supported_languages = {}
        if "categories" in appdetails:
            self.categories = appdetails["categories"]
        else:
            self.categories = {}
        if "packages" in appdetails:
            self.packages = appdetails["packages"]
        else:
            self.packages = {}
        if "metacritic" in appdetails:
            self.metacritic = appdetails["metacritic"]
        else:
            self.metacritic = {}
        if "mac_requirements" in appdetails:
            self.mac_requirements = appdetails["mac_requirements"]
        else:
            self.mac_requirements = {}
        if "steam_appid" in appdetails:
            self.steam_appid = appdetails["steam_appid"]
        else:
            self.steam_appid = {}
        if "recommendations" in appdetails:
            self.recommendations = appdetails["recommendations"]
        else:
            self.recommendations = {}
        if "required_age" in appdetails:
            self.required_age = appdetails["required_age"]
        else:
            self.required_age = {}
        if "platforms" in appdetails:
            self.platforms = appdetails["platforms"]
        else:
            self.platforms = {}
        if "linux_requirements" in appdetails:
            self.linux_requirements = appdetails["linux_requirements"]
        else:
            self.linux_requirements = {}
        if "is_free" in appdetails:
            self.is_free = appdetails["is_free"]
        else:
            self.is_free = {}
        if "background" in appdetails:
            self.background = appdetails["background"]
        else:
            self.background = {}
        if "name" in appdetails:
            self.name = appdetails["name"]
        else:
            self.name = {}
        if "release_date" in appdetails:
            self.release_date = appdetails["release_date"]
        else:
            self.release_date = {}
        if "support_info" in appdetails:
            self.support_info = appdetails["support_info"]
        else:
            self.support_info = {}
        if "developers" in appdetails:
            self.developers = appdetails["developers"]
        else:
            self.developers = {}
        if "publishers" in appdetails:
            self.publishers = appdetails["publishers"]
        else:
            self.publishers = {}
        if "achievements" in appdetails:
            self.achievements = appdetails["achievements"]
        else:
            self.achievements = {}
        if "pc_requirements" in appdetails:
            self.pc_requirements = appdetails["pc_requirements"]
        else:
            self.pc_requirements = {}
        if "header_image" in appdetails:
            self.header_image = appdetails["header_image"]
        else:
            self.header_image = {}
        if "package_groups" in appdetails:
            self.package_groups = appdetails["package_groups"]
        else:
            self.package_groups = {}
        if "about_the_game" in appdetails:
            self.about_the_game = appdetails["about_the_game"]
        else:
            self.about_the_game = {}
        if "screenshots" in appdetails:
            self.screenshots = appdetails["screenshots"]
        else:
            self.screenshots = {}
        if "price_overview" in appdetails:
            self.price_overview = appdetails["price_overview"]
        else:
            self.price_overview = {}
        if "detailed_description" in appdetails:
            self.detailed_description = appdetails["detailed_description"]
        else:
            self.detailed_description = {}
        if "website" in appdetails:
            self.website = appdetails["website"]
        else:
            self.website = {}
        if "controller_support" in appdetails:
            self.controller_support = appdetails["controller_support"]
        else:
            self.controller_support = {}
        if "movies" in appdetails:
            self.movies = appdetails["movies"]
        else:
            self.movies = {}
        if "genres" in appdetails:
            self.genres = appdetails["genres"]
        else:
            self.genres = {}
        if "type" in appdetails:
            self.type = appdetails["type"]
        else:
            self.type = {}
    """
    def __repr__(self):
        output =  ""%(self.supported_languages, self.categories, self.packages, self.metacritic, self.mac_requirements, self.steam_appid, self.recommendations, self.required_age, self.linux_requirements, self.is_free, self.background, self.name, self.release_date, self.support_info,self.developers, self.platforms, self.publishers, self.type, self.achievements, self.pc_requirements, self.header_image, self.package_groups, self.about_the_game, self.screenshots, self.price_overview, self.detailed_description, self.website, self.controller_support, self.movies, self.genres)
        return output
    """



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
"""
@param steamのappdetailsをとってきて、それをjsonでぱーすしたもの
appdetailsで返されるすべての値をそれぞれフィールドとして保持しているもの。
"""

class AppDetails:

    def __init__(self,appdetails):
        """
        対応している言語 csvで対応している国一覧
        例:'English, French, German, Italian, Japanese,'
        """
        if "supported_languages" in appdetails:
            self.supported_languages = appdetails["supported_languages"]
        else:
            self.supported_languages = {}
        """
        このゲームが含むsteam上の要素を示す。形式はjson。実績に対応しているか、マルチプレイヤーかなどを示す。
        例:[{'id': 1, 'description': 'Multi-player'}, {'id': 27, 'description': 'Cross-Platform Multiplayer'}, {'id': 22, 'description': 'Steam Achievements'}, {'id': 23, 'description': 'Steam Cloud'}, {'id': 8, 'description': 'Valve Anti-Cheat enabled'}, {'id': 15, 'description': 'Stats'}, {'id': 16, 'description': 'Includes Source SDK'}]
        categories用のデータベースを作ったほうがよいかもしれない。
        """
        if "categories" in appdetails:
            self.categories = appdetails["categories"]
        else:
            self.categories = {}
        """
        app側のidではなく、パッケージ側のidを返す
        例:[37]
        """
        if "packages" in appdetails:
            self.packages = appdetails["packages"]
        else:
            self.packages = {}
        """
        メタスコアを表示
        例:{'score': 88, 'url': 'http://www.metacritic.com/game/pc/counter-strike-source'}
        """
        if "metacritic" in appdetails:
            self.metacritic = appdetails["metacritic"]
        else:
            self.metacritic = {}
        """
        macの要求スペック
        例:{'minimum': '<strong>Minimum: </strong>OS X version Leopard 10.5.8, Snow Leopard 10.6.3, 1GB RAM, NVIDIA GeForce 8 or higher, ATI X1600 or higher, or Intel HD 3000 or higher Mouse, Keyboard, Internet Connection'}
        """
        if "mac_requirements" in appdetails:
            self.mac_requirements = appdetails["mac_requirements"]
        else:
            self.mac_requirements = {}
        """
        appidを表示
        int
        例:240
        """
        if "steam_appid" in appdetails:
            self.steam_appid = appdetails["steam_appid"]
        else:
            self.steam_appid = {}
        """
        好評価している数
        int
        [36]
        """
        if "recommendations" in appdetails:
            self.recommendations = appdetails["recommendations"]
        else:
            self.recommendations = {}
        """
        要求年齢
        int
        例:0
        """
        if "required_age" in appdetails:
            self.required_age = appdetails["required_age"]
        else:
            self.required_age = {}
        """
        各プラットフォームごとの利用可否を示す
        Boolean
        {'mac': True, 'windows': True, 'linux': True}
        """
        if "platforms" in appdetails:
            self.platforms = appdetails["platforms"]
        else:
            self.platforms = {}
        """
        linuxの要求スペックを表示
        String
        {'minimum': 'Minimum: 1.7 GHz Processor, 512MB RAM, Mouse, Keyboard, Internet Connection'}
        """
        if "linux_requirements" in appdetails:
            self.linux_requirements = appdetails["linux_requirements"]
        else:
            self.linux_requirements = {}
        if "is_free" in appdetails:
            self.is_free = appdetails["is_free"]
        else:
            self.is_free = {}
        """
        background image
        String
        'http://cdn.akamai.steamstatic.com/steam/apps/240/page_bg_generated_v6b.jpg?t=1448314295'
        """
        if "background" in appdetails:
            self.background = appdetails["background"]
        else:
            self.background = {}
        """
        game name
        String
        'Counter-Strike: Source'
        """
        if "name" in appdetails:
            self.name = appdetails["name"]
        else:
            self.name = {}
        """
        game release date
        String
        {'date': '1 Nov, 2004', 'coming_soon': False}
        """
        if "release_date" in appdetails:
            self.release_date = appdetails["release_date"]
        else:
            self.release_date = {}
        """
        this game page url and support email address
        String
        {'url': 'http://steamcommunity.com/app/240', 'email': ''}
        """
        if "support_info" in appdetails:
            self.support_info = appdetails["support_info"]
        else:
            self.support_info = {}
        """
        developer name array
        String
        ['Valve']
        """
        if "developers" in appdetails:
            self.developers = appdetails["developers"]
        else:
            self.developers = {}
        """
        publishers name array
        String
        ['Valve']
        """
        if "publishers" in appdetails:
            self.publishers = appdetails["publishers"]
        else:
            self.publishers = {}
        """
        all arcievements image url and name.
        String
        {'highlighted': [{'path': 'http://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/240/4711014791e4ae29408e8bc2fcae1ab61ca7c189.jpg', 'name': 'Someone Set Up Us The Bomb'}, {'path': 'http://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/240/5f689c20656716f2a8bf67bd26f3f7846786bca5.jpg', 'name': 'Boomala Boomala'}, {'path': 'http://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/240/6eda73149b29c897330a15e502eaee4ac8242c02.jpg', 'name': 'The Hurt Blocker'}, {'path': 'http://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/240/7bbd09bac4ebe17b84e8fb0eb5d9e3351fcb4bc0.jpg', 'name': 'Body Bagger'}, {'path': 'http://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/240/058b56fcc898b9bf893a6237ad233f677f8d48dd.jpg', 'name': 'Corpseman'}, {'path': 'http://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/240/908a8d1cdb376c401653e843fef8b4fe85156212.jpg', 'name': 'God of War'}, {'path': 'http://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/240/110782d2a043351f48c2e2bffac52db775ec573d.jpg', 'name': 'Second to None'}, {'path': 'http://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/240/892d00fc07c5dfa2f243d77722c6b9a176ac56c6.jpg', 'name': 'Combat Ready'}, {'path': 'http://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/240/10a0839b2f9bd60d8bb3a85b5a194573018fe24b.jpg', 'name': 'Counter-Counter-Terrorist'}, {'path': 'http://cdn.akamai.steamstatic.com/steamcommunity/public/images/apps/240/d156614d7d84bfdde80bdfb67b1f46cc9fb7d23e.jpg', 'name': 'Rite of First Defusal'}], 'total': 147}
        """
        if "achievements" in appdetails:
            self.achievements = appdetails["achievements"]
        else:
            self.achievements = {}
        """
        pc requriments.
        String
        {'minimum': '\r\n\t\t\t<p><strong>Minimum: </strong>1.7 GHz Processor, 512MB RAM, DirectX&reg; 8.1 level Graphics Card (Requires support for SSE), Windows&reg; 7 (32/64-bit)/Vista/XP, Mouse, Keyboard, Internet Connection</p>\r\n\t\t\t<p><strong>Recommended: </strong>Pentium 4 processor (3.0GHz, or better), 1GB RAM, DirectX&reg; 9 level Graphics Card, Windows&reg; 7 (32/64-bit)/Vista/XP, Mouse, Keyboard, Internet Connection</p>\r\n\t\t\t'}
        """
        if "pc_requirements" in appdetails:
            self.pc_requirements = appdetails["pc_requirements"]
        else:
            self.pc_requirements = {}
        """
        header_image url
        String
        'http://cdn.akamai.steamstatic.com/steam/apps/240/header.jpg?t=1448314295'
        """
        if "header_image" in appdetails:
            self.header_image = appdetails["header_image"]
        else:
            self.header_image = {}
        """
        package_groups : i dont understand what this return
        String
        [{'selection_text': 'Select a purchase option', 'save_text': '', 'name': 'default', 'title': 'Buy Counter-Strike: Source', 'subs': [{'packageid': 37, 'is_free_license': False, 'option_text': 'Counter-Strike: Source - ¥ 1,980', 'can_get_free_license': '0', 'option_description': '', 'percent_savings': 0, 'percent_savings_text': '', 'price_in_cents_with_discount': 198000}], 'display_type': 0, 'description': '', 'is_recurring_subscription': 'false'}]
        """
        if "package_groups" in appdetails:
            self.package_groups = appdetails["package_groups"]
        else:
            self.package_groups = {}
        """
        game description.
        String
        "THE NEXT INSTALLMENT OF THE WORLD'S # 1 ONLINE ACTION GAME <br>Counter-Strike: Source blends Counter-Strike's award-winning teamplay action with the advanced technology of Source&trade; technology. Featuring state of the art graphics, all new sounds, and introducing physics, Counter-Strike: Source is a must-have for every action gamer."
        """
        if "about_the_game" in appdetails:
            self.about_the_game = appdetails["about_the_game"]
        else:
            self.about_the_game = {}
        """
        screenshots url of game profile
        String
        [{'path_full': 'http://cdn.akamai.steamstatic.com/steam/apps/240/0000000027.1920x1080.jpg?t=1448314295', 'path_thumbnail': 'http://cdn.akamai.steamstatic.com/steam/apps/240/0000000027.600x338.jpg?t=1448314295', 'id': 0}, {'path_full': 'http://cdn.akamai.steamstatic.com/steam/apps/240/0000000028.1920x1080.jpg?t=1448314295', 'path_thumbnail': 'http://cdn.akamai.steamstatic.com/steam/apps/240/0000000028.600x338.jpg?t=1448314295', 'id': 1}, {'path_full': 'http://cdn.akamai.steamstatic.com/steam/apps/240/0000000029.1920x1080.jpg?t=1448314295', 'path_thumbnail': 'http://cdn.akamai.steamstatic.com/steam/apps/240/0000000029.600x338.jpg?t=1448314295', 'id': 2}, {'path_full': 'http://cdn.akamai.steamstatic.com/steam/apps/240/0000000030.1920x1080.jpg?t=1448314295', 'path_thumbnail': 'http://cdn.akamai.steamstatic.com/steam/apps/240/0000000030.600x338.jpg?t=1448314295', 'id': 3}, {'path_full': 'http://cdn.akamai.steamstatic.com/steam/apps/240/0000000031.1920x1080.jpg?t=1448314295', 'path_thumbnail': 'http://cdn.akamai.steamstatic.com/steam/apps/240/0000000031.600x338.jpg?t=1448314295', 'id': 4}]
        """
        if "screenshots" in appdetails:
            self.screenshots = appdetails["screenshots"]
        else:
            self.screenshots = {}
        """
        price data
        int
        {'final': 198000, 'currency': 'JPY', 'initial': 198000, 'discount_percent': 0}
        """
        if "price_overview" in appdetails:
            self.price_overview = appdetails["price_overview"]
        else:
            self.price_overview = {}
        """
        もっと細かい説明文章
        String
        "THE NEXT INSTALLMENT OF THE WORLD'S # 1 ONLINE ACTION GAME <br>Counter-Strike: Source blends Counter-Strike's award-winning teamplay action with the advanced technology of Source&trade; technology. Featuring state of the art graphics, all new sounds, and introducing physics, Counter-Strike: Source is a must-have for every action gamer."
        """
        if "detailed_description" in appdetails:
            self.detailed_description = appdetails["detailed_description"]
        else:
            self.detailed_description = {}
        """
        ウェブサイトのurl
        String

        """
        if "website" in appdetails:
            self.website = appdetails["website"]
        else:
            self.website = {}
        """
        コントローラーのサポートの有無
        String
        'full'
        """
        if "controller_support" in appdetails:
            self.controller_support = appdetails["controller_support"]
        else:
            self.controller_support = {}
        """
        プロフィールの映像のurl
        String
        [{'highlight': True, 'thumbnail': 'http://cdn.akamai.steamstatic.com/steam/apps/81958/movie.293x165.jpg?t=1459467902', 'webm': {'max': 'http://cdn.akamai.steamstatic.com/steam/apps/81958/movie_max.webm?t=1459467902', '480': 'http://cdn.akamai.steamstatic.com/steam/apps/81958/movie480.webm?t=1459467902'}, 'name': 'CS:GO Trailer Long', 'id': 81958}, {'highlight': False, 'thumbnail': 'http://cdn.akamai.steamstatic.com/steam/apps/2028288/movie.293x165.jpg?t=1459467945', 'webm': {'max': 'http://cdn.akamai.steamstatic.com/steam/apps/2028288/movie_max.webm?t=1459467945', '480': 'http://cdn.akamai.steamstatic.com/steam/apps/2028288/movie480.webm?t=1459467945'}, 'name': 'CS: GO Pro Tip Series: TM', 'id': 2028288}, {'highlight': False, 'thumbnail': 'http://cdn.akamai.steamstatic.com/steam/apps/2028287/movie.293x165.jpg?t=1459467936', 'webm': {'max': 'http://cdn.akamai.steamstatic.com/steam/apps/2028287/movie_max.webm?t=1459467936', '480': 'http://cdn.akamai.steamstatic.com/steam/apps/2028287/movie480.webm?t=1459467936'}, 'name': 'CS: GO Pro Tip Series: sapphiRe', 'id': 2028287}, {'highlight': False, 'thumbnail': 'http://cdn.akamai.steamstatic.com/steam/apps/2028286/movie.293x165.jpg?t=1459467927', 'webm': {'max': 'http://cdn.akamai.steamstatic.com/steam/apps/2028286/movie_max.webm?t=1459467927', '480': 'http://cdn.akamai.steamstatic.com/steam/apps/2028286/movie480.webm?t=1459467927'}, 'name': 'CS: GO Pro Tip Series: AZK', 'id': 2028286}, {'highlight': False, 'thumbnail': 'http://cdn.akamai.steamstatic.com/steam/apps/2028285/movie.293x165.jpg?t=1459467962', 'webm': {'max': 'http://cdn.akamai.steamstatic.com/steam/apps/2028285/movie_max.webm?t=1459467962', '480': 'http://cdn.akamai.steamstatic.com/steam/apps/2028285/movie480.webm?t=1459467962'}, 'name': 'CS: GO Pro Tip Series: Fifflaren', 'id': 2028285}, {'highlight': False, 'thumbnail': 'http://cdn.akamai.steamstatic.com/steam/apps/2028284/movie.293x165.jpg?t=1459467919', 'webm': {'max': 'http://cdn.akamai.steamstatic.com/steam/apps/2028284/movie_max.webm?t=1459467919', '480': 'http://cdn.akamai.steamstatic.com/steam/apps/2028284/movie480.webm?t=1459467919'}, 'name': 'CS: GO Pro Tip Series: ruggah', 'id': 2028284}, {'highlight': False, 'thumbnail': 'http://cdn.akamai.steamstatic.com/steam/apps/2028283/movie.293x165.jpg?t=1459467911', 'webm': {'max': 'http://cdn.akamai.steamstatic.com/steam/apps/2028283/movie_max.webm?t=1459467911', '480': 'http://cdn.akamai.steamstatic.com/steam/apps/2028283/movie480.webm?t=1459467911'}, 'name': 'CS: GO Pro Tip Series: nEiLZiNHo', 'id': 2028283}, {'highlight': False, 'thumbnail': 'http://cdn.akamai.steamstatic.com/steam/apps/2028289/movie.jpg?t=1459467954', 'webm': {'max': 'http://cdn.akamai.steamstatic.com/steam/apps/2028289/movie_max.webm?t=1459467954', '480': 'http://cdn.akamai.steamstatic.com/steam/apps/2028289/movie480.webm?t=1459467954'}, 'name': 'CS: GO Pro Tip Series: Semphis', 'id': 2028289}]
        """
        if "movies" in appdetails:
            self.movies = appdetails["movies"]
        else:
            self.movies = {}
        """
        ジャンルを返す
        [{'description': 'Action', 'id': '1'}]
        """
        if "genres" in appdetails:
            self.genres = appdetails["genres"]
        else:
            self.genres = {}
        """
        タイプを返す
        多分、packageだとか、DLCだとかを返すのだと思われる
        'game'
        """
        if "type" in appdetails:
            self.type = appdetails["type"]
        else:
            self.type = {}
    """
    def __repr__(self):
        output =  ""%(self.supported_languages, self.categories, self.packages, self.metacritic, self.mac_requirements, self.steam_appid, self.recommendations, self.required_age, self.linux_requirements, self.is_free, self.background, self.name, self.release_date, self.support_info,self.developers, self.platforms, self.publishers, self.type, self.achievements, self.pc_requirements, self.header_image, self.package_groups, self.about_the_game, self.screenshots, self.price_overview, self.detailed_description, self.website, self.controller_support, self.movies, self.genres)
        return output
    """



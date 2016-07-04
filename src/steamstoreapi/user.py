import urllib.request as ulr
import json
import time


class User:

    def __init__(self, API_KEY):
        self.API_KEY = API_KEY

    """
    @param steamid A steamid what you want to get friend list.
    @return frined list json.
    """
    def friend_list(self, steamid):
        url = "http://api.steampowered.com/ISteamUser/GetFriendList/v1/?key="+self.API_KEY+"&steamid="+steamid
        response = ""
        try:
            response = ulr.urlopen(url)
        except:
            print("this profile is set to private")
            return False
        response_str = response.read()
        friendlist = json.loads(response_str.decode('utf-8'))
        return friendlist["friendslist"]["friends"]

    """
    @param Be comma separated steam ids(limist 100).
    @return json of steam user summary
    """
    def user_summaries(self, steamids):
        url = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key="+self.API_KEY+"&steamids="+steamids
        try:
            response = ulr.urlopen(url)
        except:
            print("some profile is set to private")
            return
        response_str = response.read().decode('utf-8')
        user_summaries = json.loads(response_str)

        return user_summaries["response"]["players"]

    def user_game_stats(self, steamid):
        return

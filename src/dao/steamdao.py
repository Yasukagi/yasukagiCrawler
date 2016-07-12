import MySQLdb as msd
from datetime import datetime as d

"""
yasukagi.steamのデータベースアクセスオブジェクト
method insert_details, update_prices, create_table
"""
class SteamDao:
    def __init__(self, user, host, password):
        self.connect = msd.connect(user=user,passwd=password,host=host)
        self.cursor = self.connect.cursor()
        sql = "SHOW CREATE DATABASE yasukagi_db"
        try:
            self.cursor.execute(sql)
        except msd.Error:
            print("yasukagi_dbが無いから作りますよ")
            sql = "CREATE DATABASE yasukagi_db"
            self.cursor.execute(sql)
        sql = "SHOW CREATE TABLE yasukagi_db.steam"
        try:
            self.cursor.execute(sql)
            print(self.cursor.fetchall())
        except msd.ProgrammingError:
            print("テーブル：steamが無いですから作りますよ")
            self.create_table()


    """
    @:param AppDetails
    @:return SqlLog
    It insert AppDetails object.
    If same appid AppDetails object was exist, it delete one and insert.
    """
    def insert_details(self, appdetails):
        columns = "(steam_id," \
                  "steam_title,"\
                  "steam_initial_price," \
                  "steam_final_price," \
                  "steam_metacritic,"\
                  "steam_mac_requirements_minimum,"\
                  "steam_linux_requirements_minimum,"\
                  "steam_pc_requirements_minimum," \
                  "steam_mac_requirements_recommended," \
                  "steam_linux_requirements_recommended," \
                  "steam_pc_requirements_recommended," \
                  "steam_recommendations," \
                  "steam_required_age,"\
                  "steam_platforms_mac,"\
                  "steam_platforms_linux,"\
                  "steam_platforms_windows,"\
                  "steam_background_image,"\
                  "steam_release_date,"\
                  "steam_support_info_url,"\
                  "steam_header_image,"\
                  "steam_about_the_game,"\
                  "steam_detailed_description,"\
                  "steam_website,"\
                  "steam_controller_support,"\
                  "steam_type," \
                  "steam_is_free," \
                  "steam_url)"

        try:
            tdatetime = d.strptime(appdetails.release_date["date"], '%d %b, %Y')
            release_date = tdatetime.date()
        except ValueError:
            try:
                tdatetime = d.strptime(appdetails.release_date["date"], '%b, %Y')
                release_date = tdatetime.date()
            except:
                tdatetime = None
                release_date = None
        except :
            tdatetime = None
            release_date = None



        if appdetails.metacritic != {}:
            metascore = appdetails.metacritic["score"]
        else:
            metascore = None

        if appdetails.price_overview != {}:
            initial = appdetails.price_overview["initial"]
            final = appdetails.price_overview["final"]
            steam_is_free = False
        else:
            initial = None
            final = None
            steam_is_free = True

        try:
            mac_requirements_minimum = appdetails.mac_requirements["minimum"]
        except:
            mac_requirements_minimum = None

        try:
            pc_requirements_minimum = appdetails.pc_requirements["minimum"]
        except:
            pc_requirements_minimum = None

        try:
            linux_requirements_minimum = appdetails.mac_requirements["minimum"]
        except:
            linux_requirements_minimum = None


        try:
            mac_requirements_recommended = appdetails.mac_requirements["recommended"]
        except:
            mac_requirements_recommended = None

        try:
            pc_requirements_recommended = appdetails.pc_requirements["recommended"]
        except:
            pc_requirements_recommended = None

        try:
            linux_requirements_recommended = appdetails.mac_requirements["recommended"]
        except:
            linux_requirements_recommended = None


        if appdetails.recommendations != {}:
            recommendations = appdetails.recommendations["total"]
        else:
            recommendations = None


        sql = "INSERT INTO yasukagi_db.steam %s" % (columns)
        try:
            self.cursor.execute(sql + "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (appdetails.steam_appid,
                                                                                                                                              appdetails.name,
                                                                                                                                              initial/100,
                                                                                                                                              final/100,
                                                                                                                                              metascore,
                                                                                                                                              mac_requirements_minimum,
                                                                                                                                              linux_requirements_minimum,
                                                                                                                                              pc_requirements_minimum,
                                                                                                                                              mac_requirements_recommended,
                                                                                                                                              linux_requirements_recommended,
                                                                                                                                              pc_requirements_recommended,
                                                                                                                                              recommendations,
                                                                                                                                              appdetails.required_age,
                                                                                                                                              appdetails.platforms["mac"],
                                                                                                                                              appdetails.platforms["linux"],
                                                                                                                                              appdetails.platforms["windows"],
                                                                                                                                              appdetails.background,
                                                                                                                                              release_date,
                                                                                                                                              appdetails.support_info["url"],
                                                                                                                                              appdetails.header_image,
                                                                                                                                              appdetails.about_the_game,
                                                                                                                                              appdetails.detailed_description,
                                                                                                                                              appdetails.website,
                                                                                                                                              appdetails.controller_support,
                                                                                                                                              appdetails.type,
                                                                                                                                              steam_is_free,
                                                                                                                                              appdetails.pageurl))
        except :
            self.cursor.execute('DELETE FROM yasukagi_db.steam WHERE steam_id = %s' % appdetails.steam_appid)
            self.cursor.execute(sql + "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (appdetails.steam_appid,
                                                                                                                                              appdetails.name,
                                                                                                                                              initial/100,
                                                                                                                                              final/100,
                                                                                                                                              metascore,
                                                                                                                                              mac_requirements_minimum,
                                                                                                                                              linux_requirements_minimum,
                                                                                                                                              pc_requirements_minimum,
                                                                                                                                              mac_requirements_recommended,
                                                                                                                                              linux_requirements_recommended,
                                                                                                                                              pc_requirements_recommended,
                                                                                                                                              recommendations,
                                                                                                                                              appdetails.required_age,
                                                                                                                                              appdetails.platforms["mac"],
                                                                                                                                              appdetails.platforms["linux"],
                                                                                                                                              appdetails.platforms["windows"],
                                                                                                                                              appdetails.background,
                                                                                                                                              release_date,
                                                                                                                                              appdetails.support_info["url"],
                                                                                                                                              appdetails.header_image,
                                                                                                                                              appdetails.about_the_game,
                                                                                                                                              appdetails.detailed_description,
                                                                                                                                              appdetails.website,
                                                                                                                                              appdetails.controller_support,
                                                                                                                                              appdetails.type,
                                                                                                                                              steam_is_free,
                                                                                                                                              appdetails.pageurl))
        self.commit()


    def create_table(self):
        sql = "CREATE TABLE yasukagi_db.steam " \
              "(%s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" % \
              ("steam_id INTEGER PRIMARY KEY  NOT NULL",
               "steam_title TEXT NOT NULL",
               "steam_initial_price NUMERIC(15,2)",
               "steam_final_price NUMERIC(15,2)",
               "steam_metacritic INT",
               "steam_mac_requirements_minimum TEXT ",
               "steam_linux_requirements_minimum TEXT ",
               "steam_pc_requirements_minimum TEXT ",
               "steam_mac_requirements_recommended TEXT ",
               "steam_linux_requirements_recommended TEXT ",
               "steam_pc_requirements_recommended TEXT ",
               "steam_recommendations INT",
               "steam_required_age INT",
               "steam_platforms_mac BOOLEAN",
               "steam_platforms_linux BOOLEAN",
               "steam_platforms_windows BOOLEAN",
               "steam_background_image TEXT",
               "steam_release_date DATE",
               "steam_support_info_url TEXT",
               "steam_header_image TEXT",
               "steam_about_the_game TEXT ",
               "steam_detailed_description TEXT ",
               "steam_website TEXT",
               "steam_controller_support BOOLEAN",
               "steam_type TEXT",
               "steam_is_free BOOLEAN",
               "steam_url TEXT",
               "steam_timestamp timestamp NULL DEFAULT CURRENT_TIMESTAMP"
               )
        self.cursor.execute(sql)
        self.connect.commit()
        return self.cursor.fetchall()


    def update_prices(self, initial, final):
        sql = 'UPDATE yasukagi_db.steam SET steam_initial_price=%s,steam_final_price=%s' % (initial/100, final/100)
        self.cursor.execute(sql)
        return self.cursor.fetchall()


    def commit(self):
        self.connect.commit()


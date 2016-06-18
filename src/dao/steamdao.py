import MySQLdb as msd
from datetime import datetime as d
from datetime import date

class SteamDao:
    def __init__(self, user, host):
        self.connect = msd.connect(user=user,  host=host)
        self.cursor = self.connect.cursor()
        sql = "SHOW CREATE DATABASE yasukagi"
        try:
            self.cursor.execute(sql)
        except msd.Error:
            print("yasukagiが無いから作りますよ")
            sql = "CREATE DATABASE yasukagi"
            self.cursor.execute(sql)
        sql = "SHOW CREATE TABLE yasukagi.steam"
        try:
            self.cursor.execute(sql)
            print(self.cursor.fetchall())
        except msd.ProgrammingError:
            print("テーブル：steamが無いですから作りますよ")
            self.create_table()

    def insertDetails(self, appdetails):
        columns = "(steam_id," \
                  "steam_title,"\
                  "steam_initial_price," \
                  "steam_final_price," \
                  "steam_metacritic,"\
                  "steam_mac_requirements,"\
                  "steam_linux_requirements,"\
                  "steam_pc_requirements,"\
                  "steam_recommendations,"\
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
                  "steam_url)"


        tdatetime = d.strptime(appdetails.release_date["date"], '%d %b, %Y')
        release_date = tdatetime.date()



        if appdetails.metacritic != {}:
            metascore = appdetails.metacritic["score"]
        else:
            metascore = None

        if appdetails.price_overview != {}:
            initial = appdetails.price_overview["initial"]
            final = appdetails.price_overview["final"]
        else:
            initial = None
            final = None

        if appdetails.mac_requirements != {} and appdetails.mac_requirements != []:
            mac_requirements = appdetails.mac_requirements["minimum"]
        else:
            mac_requirements = None
        if appdetails.pc_requirements != {} and appdetails.pc_requirements != []:
            pc_requirements = appdetails.pc_requirements["minimum"]
        else:
            pc_requirements = None
        if appdetails.pc_requirements != {} and appdetails.linux_requirements != []:
            linux_requirements = appdetails.linux_requirements["minimum"]
        else:
            linux_requirements = None

        if appdetails.recommendations != {}:
            recommendations = appdetails.recommendations["total"]
        else:
            recommendations = None


        sql = "INSERT INTO yasukagi.steam %s" % (columns)

        self.cursor.execute(sql + "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (appdetails.steam_appid,
                                                                                                                                          appdetails.name,
                                                                                                                                          initial,
                                                                                                                                          final,
                                                                                                                                          metascore,
                                                                                                                                          mac_requirements,
                                                                                                                                          linux_requirements,
                                                                                                                                          pc_requirements,
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
                                                                                                                                          appdetails.pageurl
                                                                                                                  ))
        print("(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" %
              (appdetails.steam_appid,
               appdetails.name,
               initial,
               final,
               metascore,
               mac_requirements,
               linux_requirements,
               pc_requirements,
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
               appdetails.pageurl
               ))
    def create_table(self):
        sql = "CREATE TABLE yasukagi.steam " \
              "(%s, %s, %s,%s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s, %s)" % \
              ("steam_id INTEGER PRIMARY KEY  NOT NULL",
               "steam_title VARCHAR(255) NOT NULL",
               "steam_initial_price NUMERIC(15,2)",
               "steam_final_price NUMERIC(15,2)",
               "steam_metacritic INT",
               "steam_mac_requirements TEXT",
               "steam_linux_requirements TEXT",
               "steam_pc_requirements TEXT",
               "steam_recommendations INT",
               "steam_required_age INT",
               "steam_platforms_mac BOOLEAN",
               "steam_platforms_linux BOOLEAN",
               "steam_platforms_windows BOOLEAN",
               "steam_background_image VARCHAR(255)",
               "steam_release_date DATE",
               "steam_support_info_url VARCHAR(255)",
               "steam_header_image VARCHAR(255)",
               "steam_about_the_game TEXT",
               "steam_detailed_description TEXT",
               "steam_website VARCHAR(255)",
               "steam_controller_support BOOLEAN",
               "steam_type VARCHAR(255)",
               "steam_url VARCHAR(255)",
               "steam_timestamp timestamp NULL DEFAULT CURRENT_TIMESTAMP"
               )
        self.cursor.execute(sql)
        self.connect.commit()
        return self.cursor.fetchall()

    def commit(self):
        self.connect.commit()


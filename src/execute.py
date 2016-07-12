import crowlexecuter
import json


def execute():
    f = open("dbdata.json", "r")
    dbdata = json.load(f)
    crowlexecuter.steam_initialize.crowl(dbpasswd=dbdata["dbpasswd"], dbuser=dbdata["dbuser"])

    #crowlexecuter.kinguinfirst.crowl()
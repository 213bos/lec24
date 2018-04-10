#model.py
import csv

BB_FILE_NAME = 'umbball.csv'

bb_seasons = []
fb_seaons = []

def init_bball(csv_file_name="umbball.csv"):
    global bb_seasons
    with open(csv_file_name) as csvfile:
        reader = csv.reader(csvfile)
        next(reader) #throw away headers
        next(reader) #throw away headers
        global bb_seasons
        bb_seasons = [] #reset, start clean
        for r in reader:
            bb_seasons.append(r)

def get_bball_seasons(sortby='year', sortorder='desc'):
    if sortby == 'year':
        sortcol = 1
    elif sortby == 'wins':
        sortcol = 3
    elif sortby == 'pct':
        sortcol = 5
    else:
        sortcol = 0

    rev = (sortorder == 'desc')
    sorted_list = sorted(bb_seasons, key=lambda row: row[sortcol], reverse=rev)
    return sorted_list


def init_football(csv_file_name="umfootball.csv"):
    global fb_seasons
    with open(csv_file_name) as csvfile:
        reader = csv.reader(csvfile)
        next(reader) #throw away headers
        next(reader) #throw away headers
        global fb_seasons
        fb_seasons = [] #reset, start clean
        for r in reader:
            fb_seasons.append(r)

def get_fball_seasons(sortby='year', sortorder='desc'):
    if sortby == 'year':
        sortcol = 1
    elif sortby == 'wins':
        sortcol = 3
    elif sortby == 'pct':
        sortcol = 5
    else:
        sortcol = 0

    rev = (sortorder == 'desc')
    sorted_list = sorted(fb_seasons, key=lambda row: row[sortcol], reverse=rev)
    return sorted_list

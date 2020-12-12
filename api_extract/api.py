import json
import time
import datetime
import requests
import pandas as pd
from tqdm import tqdm

def get_data_api():
    list_rank = []
    list_artist = []
    list_title = []
    list_no_artiste = []
    date_day = []
    date_month = []
    date_year = []

    for i in tqdm(range (1,1001)):
        chaine = ("https://api.deezer.com/artist/{}/top".format(i))
        res = requests.get(chaine)
        response_json = (res.text)
        loaded_json = json.loads(response_json)

        try:
            tracks = loaded_json['data']
        except KeyError:
            i = i - 1
            time.sleep(2)

        for track in tracks:
            date_year.append((datetime.date.today().year))
            date_month.append((datetime.date.today().month))
            date_day.append((datetime.date.today().day))
            list_no_artiste.append(track['artist']['id'])
            list_rank.append(track['rank'])
            list_artist.append(track['artist']['name'])
            list_title.append(track['title'])

    df = pd.DataFrame({'Year':date_year,
                    'Month':date_month,
                    'Day': date_day,
                    'Numero Artist': list_no_artiste,
                    'Rank': list_rank,
                    'Artist': list_artist,
                    'Title': list_title})

    df.to_csv('./data/top_hits.csv', index=None)
    print(" (+) SUCCESFULLY CREATED \'./data/top_hits.csv\'!\n")

    df.to_parquet('./data/top_hits.parquet', engine='auto', index=None, partition_cols=None)
    print(" (+) SUCCESFULLY CREATED \'./data/top_hits.parquet\'!\n")

    resp = []
    for i in list_no_artiste:
        if i not in resp:
            resp.append(i)

    numero_artist = []
    name_artist = []
    nb_fan = []
    date_day = []
    date_month = []
    date_year = []

    for i in resp:
        chaine = ("https://api.deezer.com/artist/{}".format(i))
        res = requests.get(chaine)
        response_json = (res.text)
        loaded_json = json.loads(response_json)

        try:
            numero_artist.append(loaded_json['id'])
            name_artist.append(loaded_json['name'])
            nb_fan.append(loaded_json['nb_fan'])
        except KeyError:
            i = i
            time.sleep(2)

    for i in tqdm(range (0,len(numero_artist))):
        date_year.append((datetime.date.today().year))
        date_month.append((datetime.date.today().month))
        date_day.append((datetime.date.today().day))

    df2 = pd.DataFrame({'Year':date_year,
                        'Month':date_month,
                        'Day': date_day,
                        'ID':numero_artist,
                        'Name':name_artist,
                        'Number of Fan':nb_fan })

    df2.to_csv('./data/Artists.csv', index=None)

    df2.to_parquet('./data/Artists.parquet',engine='auto', index=None, partition_cols=None)
    print(" (+) SUCCESFULLY CREATED \'./data/Artists.parquet\'!\n")

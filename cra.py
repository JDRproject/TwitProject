#-*- coding:utf-8 -*-

from datetime import date
from encodings import utf_8
import sys
import requests
import os
import json
import pandas as pd
import re
import datetime
from datetime import timedelta
from django.utils import timezone
import twit_parser
print (sys.platform)


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "twitproject.settings")
import django
django.setup()
from collect.models import Tweet

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
#
#  bearer_token = os.environ.get("BEARER_TOKEN")

bearer_token = "AAAAAAAAAAAAAAAAAAAAANBuZQEAAAAAlevil2XBPe8QPX38bCqNL9a6wXI%3DgYGpD9PYq7SeOxU7UqC8ekGHk6pYSDQaQAK3mA0GLALHSpCwgh"
search_url = "https://api.twitter.com/2/tweets/search/recent"

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
# query_params = {'query': 'url:"1392450565741813760" retweets_of_1392450565741813760','tweet.fields': 'author_id'}


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

#'start_time' : '2022-02-20T20:59:58Z' ,'end_time' : '2022-02-20T20:59:59Z','query'
def search(start, end):
    query_params = { 'start_time' : start ,'end_time' : end,'query': '"5 맨날땡김" #트친과_입맛궁합_알아보기 -is:retweet','expansions':'author_id', 
 'tweet.fields': 'author_id,created_at','user.fields': 'username','max_results' : 100}

    json_response = connect_to_endpoint(search_url, query_params)

    
    print("result_count:",end='')
    print(json_response['meta']['result_count'])
    return json_response


def main():
    for i in range(12,13) :
        d = datetime.datetime(2022, 2, 20, hour=0, minute=0, second=0, microsecond=0)
        d = d + datetime.timedelta(hours=i)
        nd = d + datetime.timedelta(hours=1)
  
        result = d.strftime("%Y-%m-%dT%H:%M:%SZ")
        print(result)
        result2 = nd.strftime("%Y-%m-%dT%H:%M:%SZ")
        print(result2)
        json_response = search(result, result2)
        #print(json_response)
        if 'data' in json_response :
            for data, user in zip(json_response['data'],json_response['includes']['users']) :
                #print(user['name'])
                #print(data['text'])
                date = datetime.datetime.strptime(data['created_at'],"%Y-%m-%dT%H:%M:%S.%fZ")
                
                temp = twit_parser.parser(data['text'])
                setattr(temp,'name', str(user['name']).encode('utf8').decode('utf8'))
                setattr(temp,'text', str(data['text']).encode('utf8').decode('utf8'))
                setattr(temp,'time', date)
                
            if sys.platform != "win32" :
                    temp.save()

if __name__ == "__main__":
    main()
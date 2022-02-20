#-*- coding:utf-8 -*-

import requests
import os
import json
import pandas as pd
import re

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "twitproject.settings")
# 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
import django
django.setup()

from collect.models import Twits

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
#
#  bearer_token = os.environ.get("BEARER_TOKEN")

bearer_token = "AAAAAAAAAAAAAAAAAAAAANBuZQEAAAAAlevil2XBPe8QPX38bCqNL9a6wXI%3DgYGpD9PYq7SeOxU7UqC8ekGHk6pYSDQaQAK3mA0GLALHSpCwgh"
search_url = "https://api.twitter.com/2/tweets/search/recent"

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
# query_params = {'query': 'url:"1392450565741813760" retweets_of_1392450565741813760','tweet.fields': 'author_id'}
query_params = {'query': '#키에서_155를_뺀_만큼_말해보자 -is:retweet','tweet.fields': 'author_id','max_results' : 30}

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


def main():

    json_response = connect_to_endpoint(search_url, query_params)
    
    author_id = []
    id = []
    text = []

    for i in json_response['data'] :
        author_id.append(i['author_id'])
        id.append(i['id'])
        text.append(i['text'])

    total = 0
    sum_count = 0


    for i in text:
        print("---")
        temp = str(i).replace('#키에서_155를_뺀_만큼_말해보자','').replace('\n',' ')
        numbers = re.findall("-?\d+", temp)
        numbers = [item for item in numbers if int(item) >= -10 and int(item) <= 50]
        
        print(numbers , end='')
        if len(numbers)>=1 :
            height = 155+int(numbers[0])
            print(height)
            total += height
            sum_count += 1

            Twits(user_id = "none", text = i ).save()
        else :
            print()
        print(temp)
    print("result_count:",end='')
    print(json_response['meta']['result_count'])

    if sum_count != 0 :
        print("트위터 이용자가 주장하는 평균 키 : {0:0.2f} cm ".format(float(total/sum_count)))

    #data = json.dumps(json_response, indent=4, sort_keys=True)
    #print(type(data))
    #data = data.encode('utf-8').decode('utf-8')
    #print(data)

if __name__ == "__main__":
    main()
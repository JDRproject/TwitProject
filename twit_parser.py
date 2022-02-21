#-*- coding:utf-8 -*-
import re
import pandas
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "twitproject.settings")
import django
django.setup()
from collect.models import Tweet

input_str ="5 맨날땡김\n4 거의땡김\n2 내돈주고안먹기\n1 사줘도 잘안먹기\n0 못먹음\n\n육회: 3\n마라탕: 4\n간장게장: 4\n선지: 2\n민초: 4\n탄산수: 3\n커피: 5\n생굴: 4\n닭발: 4\n막창: 4\n곱창: 3\n닭똥집: 3\n알탕: 2\n산낙지: 3\n오뎅: 3\n양꼬치: 4\n떡볶이: 5"
input_str = input_str.replace('\n','')


def parser(input_str) :
    result = Tweet()

    colums = ["육회","마라탕","간장게장","선지","민초","탄산수","커피","생굴","닭발","막창","곱창","닭똥집","알탕","산낙지","오뎅","양꼬치","떡볶이"]
    db_colums =[
        "grade_rawmeat",  
        "grade_maratang", 
        "grade_crab" ,
        "grade_seonji" ,
        "grade_mincho",
        "grade_sparkling",
        "grade_coffee",
        "grade_oysters",
        "grade_chicken_foot" ,
        "grade_makchang" ,
        "grade_gobchang",
        "grade_chicken_coop",
        "grade_altang" ,
        "grade_nakgi" ,
        "grade_odeng" ,
        "grade_lamb" ,
        "grade_ddukboki" ,]
    input_str = input_str.replace('\n','')
    #print(input_str)
    for i in range(0,len(colums)-1):
        #print(colums[i])
        search_str = colums[i]+ ':(.*?)' + colums[i+1]
        data = re.search(search_str, input_str).group(1)
        numbers = re.findall("\d+", data)
        #print(numbers)
        if len(numbers) > 0 :
            setattr(result, db_colums[i], numbers[0])
        else:
            setattr(result, db_colums[i], -1)


    #print(result.grade_altang)
    return result

def main() :
    parser(input_str)

if __name__ == "__main__":
    main()
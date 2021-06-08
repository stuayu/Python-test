# -*- coding: utf-8 -*-
# しょぼいカレンダーのjsonよりアニメタイトルを取得する。
import json
import requests

url = "https://cal.syoboi.jp/json.php?Req=TitleMedium"
session = requests.Session()
data = session.get(url)
json_data = json.loads(data.text.encode("utf8"))

# list型ver


def search_title(year, AnimeTitleList):
    '''しょぼいカレンダーのjsonから指定された放送開始年のタイトルを取得してリストに代入する'''
    for i in range(1, len(json_data['Titles'])):
        try:
            if (json_data['Titles'][str(i)]['FirstYear'] == str(year)):
                # print(json_data['Titles'][str(i)]['Title'])  # debag
                AnimeTitleList.append(json_data['Titles'][str(i)]['Title'])
        except KeyError:
            pass
    return AnimeTitleList

# 辞書型ver


def search_title_dic(year, AnimeTitleDict):
    '''しょぼいカレンダーのjsonから指定された放送開始年のタイトルを取得してTIDとタイトル名を辞書型に代入する'''
    for i in range(1, len(json_data['Titles'])):
        try:
            if (json_data['Titles'][str(i)]['FirstYear'] == str(year)):
                # print(json_data['Titles'][str(i)]['Title'])  # debag
                AnimeTitleDict[json_data['Titles']
                               [str(i)]['TID']] = json_data['Titles'][str(i)]['Title']
        except KeyError:
            pass
    return AnimeTitleDict


def search_subTitle(source, SearchName):
    '''辞書型に入っているタイトル名を検索タイトル名(部分一致)で探し見つかったらTIDを返す
    TIDからサブタイトルを取得しサブタイトルリストを返す'''
    subTitle = []
    # print(source)
    title: str
    for k, v in source.items():
        # print(v)
        # print(SearchName)
        # print(v.find(SearchName))
        if v.find(SearchName) == 0:
            print(v)
            TID = k

    print(TID)
    subTitle = get_subTitle(TID)

    return subTitle


def get_subTitle(TID: str):
    '''TIDからサブタイトルを取得しリスト型で返す'''
    urlSub = "https://cal.syoboi.jp/json.php?Req=SubTitles&TID=" + TID
    print(urlSub)
    session = requests.Session()
    data = session.get(urlSub)
    json_data1 = json.loads(data.text)

    return json_data1


if __name__ == "__main__":
    anime = []  # listの初期化
    Dic = {}  # 辞書型の初期化
    SearchName = 'イジらないで、長瀞'
    #anime = search_title(2021, anime)
    # print(anime)

    search_title_dic(2021, Dic)
    # print(animeDic)

    subtitle = search_subTitle(Dic, SearchName)
    print(subtitle)

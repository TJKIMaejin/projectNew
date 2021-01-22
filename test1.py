import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.bob4

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}



# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
imgs = list(db.bob4.find({},{'_id':0,'dish':0,'add':0,'media':0,'area':0}))
for i, img in enumerate(imgs):
    print(i, img['name'])

    url = 'https://www.google.com/search?q=%EC%8B%9D%EB%8B%B9+'+img['name']
    print(url)
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    img1 = soup.select_one('#rhs > div > div.kp-blk.knowledge-panel.Wnoohf.OJXvsb > div > div.ifM9O > div > div.kp-header > div:nth-child(2) > div.fYOrjf.iB08Xb.kp-hc > div:nth-child(2) > div')
    if img1 is None:
        img1 = '-1'
    else:
        # img1 = img1['data-source']
        rank_num = img1.text.split('G')[0]



    1. 이미 첫장의url가져오기
    2.  udatee


# url = 'https://www.google.com/search?q=%EC%8B%9D%EB%8B%B9+%ED%99%8D%EC%97%B0'
# data = requests.get(url, headers=headers)
# soup = BeautifulSoup(data.text, 'html.parser')
#
# rank=soup.select_one('#rhs > div > div.kp-blk.knowledge-panel.Wnoohf.OJXvsb > div > div.ifM9O > div > div.kp-header > div:nth-child(2) > div.fYOrjf.iB08Xb.kp-hc > div:nth-child(2) > div')
# rank2=soup.select_one('#reviewSort > div.r-i3v9tkXRArNs > div.gws-localreviews__general-reviews-block > div.WMbnJf.gws-localreviews__google-review.r-irKzvM5siXY8 > div.jxjCjc')
# rank_num=rank.text.split('G')[0]
# rank_str=rank.text.split('5')[1]
#
# print(rank_num)
# print(rank_str)



# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# rank = list(db.bob.find({},{'_id':0,'dish':0,'add':0,'media':0,'area':0}))
# for i, ranks in enumerate(rank):
#
#     url = 'https://www.google.com/search?q=%EC%8B%9D%EB%8B%B9+'+ranks['name']
#     print(url)
#     data = requests.get(url, headers=headers)
#     soup = BeautifulSoup(data.text, 'html.parser')
#     rank1 = soup.select_one('#rhs > div > div.kp-blk.knowledge-panel.Wnoohf.OJXvsb > div > div.ifM9O > div > div.kp-header > div:nth-child(2) > div.fYOrjf.iB08Xb.kp-hc > div:nth-child(2) > div')
#     print(rank1)
#     rank_num=rank1.text.split('G')[0]
#
#     print(i, ranks['name'],rank_num)
#     if rank1 is None:
#         rank1 = '-1'
#     else:
#
#         db.bob.update_one({'name': ranks['name']}, {'$set': {'rank': rank_num}})
#








for imgs in imgs:

   print(img1['data-source'])






select를 이용해서, tr들을 불러오기
movies = soup.select('_sau_imageTab > div.photowall._photoGridWrapper > div.photo_grid._box > div:nth-child(1) > a.thumb._thumb > img')



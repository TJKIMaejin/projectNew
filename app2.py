
from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.pl
db2=client.K
pig_seoul = list(db.bob.find({'media': '맛있는 녀석들', 'area': '서울'}, {'_id': 0}))
print(pig_seoul)

num2 =list(db.K.find({},{'_id':0,'dish':0,'add':0,'media':0,'area':0}))

# 검색할 주소


from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client1 = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db1 = client1.last                      # 'dbsparta'라는 이름의 db를 만듭니다.


client2 = MongoClient('13.125.224.134', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db2 = client2.last                      # 'dbsparta'라는 이름의 db를 만듭니다.


docs =list(db1.last.find({},{'id':0}))

db2.last.insert_many(docs)
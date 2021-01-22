from flask import Flask, render_template, jsonify
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.last                      # 'dbsparta'라는 이름의 db를 만듭니다.



## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('main2.html')
@app.route('/test1')
def bob1():
   return render_template('index2.html')
# @app.route('/test2')
# def bob2():
#    return render_template('index.html')
# @app.route('/test3')
# def bob3():
#    return render_template('main2.html')












## API 역할을 하는 부분

@app.route('/api/find', methods=['GET'])
def test3():
    seoul = list(db.last.find({'area': '서울'}, {'_id': 0}))
    Jeolla = list(db.last.find({'area':'전라'},{'_id':0}))
    Gangwon= list(db.last.find({'area':'강원'},{'_id':0}))
    gyeongsang=list(db.last.find({'area':'경상'},{'_id':0}))




    print('확인')     


    return jsonify({'result':'sucess','seoul':seoul,'Jeolla':Jeolla,'Gangwon':Gangwon,'gyeongsang':gyeongsang})







if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)
import os
from flask.json import jsonify
from flask_pymongo import PyMongo
from flask import Flask, jsonify, render_template, request, redirect

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/local"
mongo = PyMongo(app)

@app.route('/detail')
def detail():
    product_db = mongo.db.product
    product = product_db.find_one({"title" : request.args.get('title')})
    
    return jsonify({
        'title':product.get('title'),
        'content' : product.get('content')}) 
    # detail부분은 내가 product를 클릭했을 때 모달이 제목,내용으로 뜨는 것
    # api를 호출하는 곳을 살펴봐야함 -> script.js파일 살펴보자

@app.route('/writepage')
def writepage():
    return render_template('write.html')

@app.route('/write', methods = ["POST"])
def write():
    fileinfo = request.files['image']
    filepath = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(filepath, 'static')

    fileinfo.save(os.path.join(filepath, fileinfo.filename))

    product_db = mongo.db.product
    
    product_db.insert_one({
        'title':request.form.get('title'),
        'content':request.form.get('content'),
        'price':request.form.get('price'),
        'location':request.form.get('location'),
        'image': fileinfo.filename   
    })

    return redirect('/')  #다시 /route로 가는 것

@app.route('/') # 첫번째 접속 했을 때
def main():
    product_db = mongo.db.product # mongodb에 접속, product라는 새 collection을 만듦
    products = product_db.find() # #find함수 : 전체를 가져다 줌
    return render_template('list.html', products = products) # 전체를 가져와 list.html 파일에 전달

if __name__ == '__main__':
    app.run() 
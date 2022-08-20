from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/abc',methods=['GET','POST'])
def test1():
    if(request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a+b
        return jsonify(str(result))

@app.route('/abc1/shab',methods=['GET','POST'])
def test2():
    if request.method == 'POST':
        a = request.json['num1']
        b = request.json['num2']
        return jsonify(str(a**b))

if __name__=='__main__':
    app.run()


def test(a,b):
    return a+b

'''
1. write a program to insert a record in a sql table via api
2. write a program to update a record via api
3. write a program to delete a record via api
4. write a program to fetch a record via api
5, all the above qtns has to be done in MongoDb also
'''
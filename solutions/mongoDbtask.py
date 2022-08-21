import pymongo

from flask import Flask, request, jsonify

app= Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://system:system@cluster0.0rtf2.mongodb.net/?retryWrites=true&w=majority")
database = client['api_task']  # connecting to database
collection = database['task']

@app.route("/insert/mongo",methods=["GET","POST"])
def insert_records():
    if request.method=='POST':
        name = request.json['name']
        number = request.json['number']
        collection.insert_one({name:number})
        return jsonify(str("Successfully inserted in collection"))

if __name__ == '__main__':
    app.run()
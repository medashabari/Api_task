# 8. write a program to fetch records in a MongoDB collection via api
import pymongo
import logging as log
from flask import Flask, request, jsonify

log.basicConfig(filename='qtn8.log',level=log.INFO)
# connecting to mongoDB
try:
    client = pymongo.MongoClient("mongodb+srv://system:system@cluster0.0rtf2.mongodb.net/?retryWrites=true&w=majority")
    db = client.test
    log.info("successfully connected to MongoDB")
except Exception as e:
    log.info(e)

database = client['api_task']  # connecting to database
collection = database['task']  # accessing the collection inside database


app = Flask(__name__)


@app.route("/fetch",methods=["GET","POST"])
def fetch_records():
    try:
        if request.method=='POST':
            user = request.json['user']
            d=collection.find({'user':user})
            l=[]
            for i in d:
                log.info(i)
                l.append(i)
            log.info('Successfully fetched from collection')
            return jsonify(str(l))
    except Exception as e:
        log.info(e)
    finally:
        client.close()


if __name__=='__main__':
    app.run()
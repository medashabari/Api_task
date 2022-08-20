# 7. write a program to delete a record in a MongoDB collection via api
import pymongo
import logging as log
from flask import Flask, request, jsonify

log.basicConfig(filename='qtn7.log',level=log.INFO)
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
@app.route("/delete",methods=["GET","POST"])
def delete_records():
    try:
        if request.method=='POST':
            user = request.json['user']
            collection.delete_one({'user':user})
            log.info('Successfully deleted in collection')
            return jsonify(str("Successfully deleted in collection"))
    except Exception as e:
        log.info(e)
    finally:
        client.close()

if __name__=='__main__':
    app.run()
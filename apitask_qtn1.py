# 1. write a program to insert a record in a sql table via api
import logging as log
from flask import Flask, request, jsonify

import mysql.connector as connection
log.basicConfig(filename='qtn1.log',level=log.INFO)
try:
    mydb= connection.connect(host='localhost',user='root',password='system')
    log.info('Database connection successfull')
    cursor = mydb.cursor()
    cursor.execute('use api_task')
except Exception as e:
    log.info(e)

app = Flask(__name__)


@app.route('/insert',methods=['GET','POST'])
def insert_records():
    try:
        if request.method == 'POST':
            user_name = request.json['user1']
            password = request.json['password1']
            cursor.execute("insert into task values('{0}','{1}')".format(user_name,password))
            mydb.commit()
            log.info('inserted records')
            log.info('successfully closed db connection')
            return jsonify(str("inserted 1 record"))
    except Exception as e:
        log.info(e)
    finally:
        mydb.close()


if __name__ =='__main__':
    app.run()

# 4. write a program to fetch a record via api
import logging as log
from flask import Flask, request, jsonify

import mysql.connector as connection
log.basicConfig(filename='qtn4.log',level=log.INFO)
try:
    mydb= connection.connect(host='localhost',user='root',password='system')
    log.info('Database connection successfull')
    cursor = mydb.cursor()
    cursor.execute('use api_task')
except Exception as e:
    log.info(e)

app = Flask(__name__)


@app.route('/fetch',methods=['GET','POST'])
def fetch_records():
    try:
        if request.method == 'POST':
            var1 = request.json['user']
            cursor.execute("select * from task where user = '{0}'".format(var1))
            l=[]
            for i in cursor.fetchall():
                log.info(i)
                l.append(i)
            mydb.commit()
            log.info('fetched records')
            log.info('successfully closed db connection')
            return jsonify(str(l))
    except Exception as e:
        log.info(e)
    finally:
        mydb.close()


if __name__ =='__main__':
    app.run()

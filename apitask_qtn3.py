# 3. write a program to delete a record via api
import logging as log
from flask import Flask, request, jsonify

import mysql.connector as connection
log.basicConfig(filename='qtn3.log',level=log.INFO)
try:
    mydb= connection.connect(host='localhost',user='root',password='system')
    log.info('Database connection successfull')
    cursor = mydb.cursor()
    cursor.execute('use api_task')
except Exception as e:
    log.info(e)

app = Flask(__name__)


@app.route('/delete',methods=['GET','POST'])
def delete_records():
    try:
        if request.method == 'POST':
            var1 = request.json['user']
            cursor.execute("delete from task where user ='{0}'".format(var1))
            mydb.commit()
            log.info('deleted records')
            log.info('successfully closed db connection')
            return jsonify(str("deleted record"))
    except Exception as e:
        log.info(e)
    finally:
        mydb.close()

if __name__ =='__main__':
    app.run()

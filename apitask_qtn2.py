# 2. write a program to update a record via api
import logging as log
from flask import Flask, request, jsonify

import mysql.connector as connection
log.basicConfig(filename='qtn2.log',level=log.INFO)
try:
    mydb= connection.connect(host='localhost',user='root',password='system')
    log.info('Database connection successfull')
    cursor = mydb.cursor()
    cursor.execute('use api_task')
except Exception as e:
    log.info(e)

app = Flask(__name__)


@app.route('/update',methods=['GET','POST'])
def update_records():
    try:
        if request.method == 'POST':
            var1 = request.json['old']
            var2 = request.json['new']
            cursor.execute("update task set user ='{1}' where user ='{0}' ".format(var1,var2))
            mydb.commit()
            log.info('updated records')
            log.info('successfully closed db connection')
            return jsonify(str("updated record"))
    except Exception as e:
        log.info(e)
    finally:
        mydb.close()


if __name__ =='__main__':
    app.run()

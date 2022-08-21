# 8/21/2022

from flask import Flask, request, jsonify
import mysql.connector as conn

app = Flask(__name__)
# mydb = conn.connect(host="localhost",user="root",password="system",database='shabarish')
mydb = conn.connect(host="localhost",user="root",password="system")
cursor = mydb.cursor()

@app.route('/db')
def taskdb():
    db_name = request.args.get("dn")
    table_name = request.args.get("tn")
    cursor.execute(f'use {db_name}')
    l=[]
    cursor.execute(f"select * from {table_name}")
    data=cursor.fetchall()
    mydb.close()
    return jsonify(data)


if __name__ == '__main__':
    app.run()
#!/usr/bin/python3
from flask import Flask
import mysql.connector
import sys
import alphaserver
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello():
    db_name = 'ssh_attempts'
    db_table = 'report'
    print ("Connecting to mysql")
    connection = alphaserver.mydb()

    print ("Getting data from database")
    query = 'SELECT * FROM %s.%s' %(db_name,db_table)
    response = alphaserver.db_execute(connection,query,True)
    return render_template('result.html', response=response)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8090', debug=True)
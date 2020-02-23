#!/usr/bin/env python3
import mysql.connector
import sys
import alphaserver

def main():
    db_name = 'ssh_attempts'
    db_table = 'report'
    print ("Connecting to mysql")
    connection = alphaserver.mydb()

    print ("Getting data from database")
    query = 'SELECT * FROM %s.%s' %(db_name,db_table)
    response = alphaserver.db_execute(connection,query,True)
    print (" --------------------------------")
    print ("| Metrics for ssh log-in attempts|")
    print ("|--------------------------------|")
    for row in response:
        print ("| * %s had %d attempt" %(row[1],row[2]))

    print (" --------------------------------")
main()

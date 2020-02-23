#!/usr/bin/python3
import socket,mysql.connector,select,sys
import sys
db_name = '{{ mysql_db }}'
db_table = '{{ mysql_table }}'

def mydb():
    connection=mysql.connector.connect(
                                    host="127.0.0.1",
                                    user="root",
                                    passwd="{{ mysql_root_password }}")
    return connection

def db_execute(connection,query,select=False):
    cursor = connection.cursor(buffered=True)
    cursor.execute(query)
    if select :
        response = cursor.fetchall()
        return response
    else:
        connection.commit()

def close_db_connection(connection):
    connection.close()


def db_update(client_ip,attempt):
    connection=mydb()
    query = 'SELECT COUNT(*) FROM %s.%s WHERE client_ip = "%s"' %(db_name,db_table,client_ip)
    response = db_execute(connection,query,True)
    print("response ",response)
    for row in response:
        host_exist = row[0]
        break
    print(host_exist)
    if host_exist == 0:
        print("Inserting data data.")
        query = 'INSERT INTO %s.%s (client_ip, attempt) VALUES ("%s", %d);' %(db_name, db_table, client_ip,attempt)
        db_execute(connection,query)
    else:
        print("Updating data data.")
        query = 'UPDATE %s.%s SET attempt = attempt+%d WHERE client_ip="%s";' %(db_name, db_table, attempt, client_ip)
        db_execute(connection,query)
    print("Closing database connection.")
    close_db_connection(connection)


def open_socket():
    connection=mydb()
    query = 'CREATE DATABASE IF NOT EXISTS %s' %db_name
    db_execute(connection,query)
    query = 'CREATE TABLE IF NOT EXISTS %s.%s ( ID int(16) NOT NULL AUTO_INCREMENT, client_ip varchar(255), attempt int, PRIMARY KEY (ID) );' %(db_name, db_table)
    db_execute(connection,query)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('', 8080)
    sock.bind(server_address)
    sock.listen(1)
    while True:
        connection, client_address = sock.accept()
        client_ip=client_address[0]
        attempt=int(connection.recv(4096))
        db_update(client_ip,attempt)
    sock.close()


if __name__ == "__main__":
    open_socket()

#!/usr/bin/python3
import os,re,socket
auth_file='/var/log/auth.log'

def tail_line(authlogfile):
    authlogfile.seek(0,2)
    while True:
        readline=authlogfile.readline()
        if not readline:
            continue
        yield readline


def report(attempt_count):
    server = "172.31.45.182"
    port = 8080
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server, port))
        s.sendall(attempt_count.encode('utf-8'))
        print ("Data sent to server")

    finally:
        s.close()




def attempt(auth_file):
    authlogfile=open(auth_file,"r")
    #print(dir(authlogfile))
    #print(authlogfile.read())
    lines=tail_line(authlogfile)
    for i in lines:
        print(i)
        if re.match('.*sshd.*?(Invalid\suser|Accepted).*',i) is not None:
            print("attempt 1")
            report('1')



attempt(auth_file)

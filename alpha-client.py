#!/usr/bin/python3
import os
auth_file='/var/log/auth.log'

def tail_line(authlogfile):
    authlogfile.seek(0,2)
    while True:
        readline=authlogfile.readline()
        if not readline:
            continue
        yield readline

def attempt(auth_file):
    authlogfile=open(auth_file,"r")
    #print(dir(authlogfile))
    #print(authlogfile.read())
    lines=tail_line(authlogfile)
    for i in lines:
        print(i)



attempt(auth_file)

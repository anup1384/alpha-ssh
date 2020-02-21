#!/usr/bin/python3
import os
auth_file='/var/log/auth.log'

def attempt(auth_file):
    authlogfile=open(auth_file,"r")
    print(authlogfile.read())

attempt(auth_file)

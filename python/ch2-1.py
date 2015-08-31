#!/usr/bin/python
import string
def encrypt(question):
    table = string.maketrans('abcdefghijklmnopqrstuvwxyz','cdefghijklmnopqrstuvwxyzab')
    return string.translate(question,table)

def encrypt2(question):
    table  = string.maketrans(string.ascii_lowercase,string.ascii_lowercase[2:]+string.ascii_lowercase[:2])
    return string.translate(question,table)

question = raw_input("please input the stirng:")
print encrypt2(question)

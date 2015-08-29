#!/usr/bin/python
import string
def encrypt(question):
    table = string.maketrans('abcdefghijklmnopqrstuvwxyz','cdefghijklmnopqrstuvwxyzab')
    return string.translate(question,table)
question = raw_input("please input the stirng:")
print encrypt(question)

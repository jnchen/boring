#!/usr/bin/python
question = open("123").read()
result = []
for i in range(4,len(question)-4):
    if question[i].islower() and question[i-1].isupper() and question[i-2].isupper() and question[i-3].isupper() and question[i-4].islower() and question[i+1].isupper() and question[i+4].islower() and question[i+2].isupper() and question[i+3].isupper():
        result.append(question[i])

print "".join(result)

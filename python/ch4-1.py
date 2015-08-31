#!/usr/bin/python
import re

question = open("123").read()

pattern = re.compile('[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]')
result = []
for i in pattern.finditer(question):
    result.append(i.group()[4])
print "".join(result)

#!/usr/bin/python
import re

question = open('123').read()
result = []
for i in re.finditer('[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]',question):
    result.append(i.group()[4])
print "".join(result)

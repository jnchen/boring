#!/usr/bin/python
#question = raw_input()
question = open('source.txt').read()


result = []
for ch in question:
   if ch.isalpha():
        result.append(ch)
print "".join(result)

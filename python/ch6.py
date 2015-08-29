#!/usr/bin/python
import urllib,pickle

txt = urllib.urlopen('http://www.pythonchallenge.com/pc/def/banner.p').read()

f = open('obj1','w+')

f.write(txt)

f.seek(0)

obj = pickle.load(f)

f.close()
line =[]
for i in obj:
 for k,v in i:
  for j in range(0,int(v)):
   line.append(k)
 print "".join(line)
 line =[]

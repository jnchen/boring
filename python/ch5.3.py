#!/usr/bin/env python
# -*- coding:utf-8 -*-

#pickle
import urllib.request,pickle
url = r'http://www.pythonchallenge.com/pc/def/banner.p'

#response = urllib.request.urlretrieve(url,"123")
#f = open("123","rb")
#python网页默认用bytes编码,读取时需要用bytes模式

response = urllib.request.urlopen(url)
f = open("123","wb+")
f.write(response.read())
f.seek(0)
#用bytes模式存储和直接urlretrieve效果是一样的

result = pickle.load(f)
for i in result:
	line =[]
	for k,v in i:
		for j in range(0,v):
			line.append(k)
	print("".join(line))
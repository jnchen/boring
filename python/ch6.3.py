#!/usr/bin/env python
#-*- coding:utf-8 -*-

import zipfile,urllib.request,re

url = r'http://www.pythonchallenge.com/pc/def/channel.zip'

urllib.request.urlretrieve(url,"data.zip")

zipf = zipfile.ZipFile("data.zip")
line = []
nothing = '90052'
ends = '.txt'
pattern = '(\d+)'
res = zipf.read(nothing+ends)
res = res.decode()
while True:
	if len(re.findall(pattern,res)) > 0 :
		#print(res)
		line.append(zipf.getinfo(nothing+ends).comment.decode())
		nothing = re.findall(pattern,res)[-1]
		#print("catch nothing is %s"%nothing)
		res = zipf.read(nothing+ends)
		res = res.decode()
	else:
		#print(res)
		break

line.append(zipf.getinfo(nothing+ends).comment.decode())
print("".join(line))
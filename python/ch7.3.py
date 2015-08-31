#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib.request
import PIL.Image

url = r'http://www.pythonchallenge.com/pc/def/oxygen.png'
cut = (0, 43, 608, 44)
urllib.request.urlretrieve(url, "oxygen.png")
img = PIL.Image.open("oxygen.png")
img = img.crop(cut)
img = img.convert("L")
line = []
data = list(img.getdata())
for i in range(0, 607, 7):
    line.append(chr(data[i]))
print("".join(line))

l = [105, 110, 116, 101, 103, 114, 105, 116, 121]
line = []
for i in l:
    line.append(chr(i))
print("".join(line))

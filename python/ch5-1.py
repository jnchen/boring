#!/usr/bin/env python
# -*- coding=utf-8 -*-

import re
import urllib.request
url_prefix = r"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
nothing = '12345'
pattern1 = r'(\d+)'
pattern2 = r'Yes'
response = urllib.request.urlopen(url_prefix+nothing)
res = response.read()
res = res.decode()
while True:
    print(res)
    if len(re.findall(pattern1, res)) > 0:
        nothing = re.findall(pattern1, res)[-1]
    elif len(re.findall(pattern2, res)) > 0:
        nothing = str(int(nothing)//2)
    else:
        print(res)
        break
    print("catch nothing is :%s"%nothing)
    response = urllib.request.urlopen(url_prefix+nothing)
    res = response.read()
    res = res.decode()

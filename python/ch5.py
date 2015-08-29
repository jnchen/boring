#!/usr/bin/python
import urllib,re

num = '12345'

url = r'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

regex = r'(\d+)'

regex1 = r'Yes'

conn = urllib.urlopen(url+num)

txt = conn.read()

while True:
    if len(re.findall(regex,txt)) > 0 :
        num = re.findall(regex,txt)[-1]
    elif len(re.findall(regex1,txt)) > 0 :
        num = str(int(num)/2)
    else:
	print 'The key is ',txt
        break;
    conn = urllib.urlopen(url+num)
    txt = conn.read()
    print 'this nothing  is',num,',',txt


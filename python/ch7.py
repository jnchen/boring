#!/usr/bin/python
import zipfile,urllib,re

zip = urllib.urlretrieve('http://pythonchallenge.com/pc/def/channel.zip','channel.zip')

question = zipfile.ZipFile('channel.zip')
pattern = '(\d+)'
num = '90052'
content = []
txt = question.open(num+'.txt').read()
content.append(question.getinfo(num+'.txt').comment)
print 'this nothing is ',num,',',txt

while True:
    if len(re.findall(pattern,txt)) >0 :
        num = re.findall(pattern,txt)[-1]
    else:
        break
    txt = question.open(num+'.txt').read()
    content.append(question.getinfo(num+'.txt').comment)
    print 'this nothing is ',num,',',txt

print "".join(content)

#!/usr/bin/python

question = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''
result =[]

for ch in question:
    if (ord(ch)>=ord('a'))and(ord(ch)<=ord('z')):
        result.append(chr((ord(ch)-ord('a')+2)%26+ord('a')))
    else:
        result.append(ch)

print ''.join(result)


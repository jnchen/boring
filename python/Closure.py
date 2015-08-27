#!/usr/bin/python
# -*-coding:utf-8-*-
def count():
	fs = []
	for i in range(1,4):
		def f(i):
			def func():
				return i*i
			return func
		r = f(i)
		fs.append(r)
	return fs
f1,f2,f3=count()
print(f1())
print(f2())
print(f3())


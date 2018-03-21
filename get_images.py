#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib

f = open("links.txt","r") #opens file with name of "test.txt"
line = f.readline()
line = f.readline()
for i in range(0,1000):
	print(line)
	uu = line.decode('utf8')
	urllib.urlretrieve(uu.encode('utf8'), "images/"+str(i)+".jpg")
	line = f.readline()

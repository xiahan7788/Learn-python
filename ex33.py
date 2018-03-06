#!/usr/bin/env
# -*- coding: utf-8 -*-

i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i
	# list numbers add i
	numbers.append(i)
	# i += 1 means i = i + 1; and while until i < 6
	i += 1
	print "Numbers: now: ", numbers
	print "At the bottom i is %d" % i
	
print "The numbers: "

# print list numbers one by one
for num in numbers:
	print num
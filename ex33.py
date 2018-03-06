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
	
def test(t):
	i = 0
	numbers = []
	while i < t:
		print "At the top i is %d" % i
		numbers.append(i)
		i += 1
		print "Numbers: now: ", numbers
		print "At the bottom i is %d" % i
	# notice the indent, because these are not in while	
	print "The numbers: "
	for nums in numbers:
		print nums

k = int(input("Numbers: "))
test(k)

print "The numbers: "
for i in range(0, k):
	print i
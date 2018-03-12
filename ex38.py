#!/usr/bin/env
# -*- coding: utf-8 -*-

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
print stuff
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# if len(stuff) != 10, loop it until len(stuff) = 10 and stop.
while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There's %d items now." % len(stuff)
	
print "There we go: ", stuff

print stuff[1]
print stuff[-1] # whoa! fancy
# get a argument from the list in the end
print stuff.pop()
print ' '.join(stuff) # what? cool!
print '#'.join(stuff[3:6]) # super stellar!

# let's review "while loop"
n = 5
sum = 0
# sum of n natural numbers
i = 1
while i <= n:
    sum += i
    i += 1
print sum
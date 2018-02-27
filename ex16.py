# -*- coding: utf-8 -*-
from sys import argv # import argument from sys file

script, filename = argv # provide two arguments

print "We're going to erase %r." % filename # notes
print "If you don't want that, hit CTRL-C (^C)." # sure?
print "If you want that, hit RETURN." # sure?

raw_input("?") # make the choice

print "Opening the file..." # notice: run
target = open(filename, 'w') # get file

print "Truncating the file. Goodbye!" # notice: truncate
target.truncate() # run truncate

print "Now I'm going to ask you for three lines."  # Notes

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "Let's read it:"
target = open(filename)
print target.read()

print "And finally, we close it."
target.close()

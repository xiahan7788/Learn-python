# -*- coding: utf-8 -*-
from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	print line_count, f.readline()

# open file that we input
current_file = open(input_file)

# read file that we input
print "First let's print the whole file:\n"
# run function print_all
print_all(current_file)

# how does seek work? seek read file lien by line.
print "Now let's rewind, kind of like a tape."
#run functions, read file from 0 byte
rewind(current_file)

# note
print "Let's print three line:\n"

# run functions
current_line = 1
print_a_line(current_line, current_file)

#run functions again
current_line = current_line + 1
print_a_line(current_line, current_file)

# run function more
current_line = current_line + 1
print_a_line(current_line, current_file)
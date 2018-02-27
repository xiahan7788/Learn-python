# -*- coding: utf-8 -*-
from sys import argv # import your lib

script, filename = argv # give two grguments

txt = open(filename) # get ex15_sample.txt

print "This is %r script." % script # output name
print "Here's your file %r:" % filename # output your filename
print txt.read() # open your filename
txt.close()

print "Type the filename again:" # output name
file_again = raw_input("> ") # input name again

txt_again = open(file_again) # get file again

print txt_again.read() # output file
txt_again.close()
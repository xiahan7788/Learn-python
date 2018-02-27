from sys import argv # import arguments from sys
from os.path import exists # import exists function

script, from_file, to_file = argv # provide two arguments

print "Copying from %s to %s" % (from_file, to_file) # notice

# we could do these two on one line too, how?
in_file = open(from_file); # get from_file
indata = in_file.read() # read from_file

print "The input file is %d bytes long" % len(indata) # output lens of from_file

print "Does the output file exist? %r" % exists(to_file) # exists?
print "Ready, hit RETURN to continue, CTRL-C to abort." # chose no
raw_input("> ") # user confirm?

out_file = open(to_file, 'w') # get to_file
out_file.write(indata) # write to_file

print "All right, all done." # notice

out_file = open(to_file) # get new to_file
print out_file.read() # output to_file

out_file.close() # close to_file
in_file.close() # close from_file
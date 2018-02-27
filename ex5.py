# -*- coding : utf-8 -*-
name = 'Zed A.Shaw'
age = 35 # not a lie
height = 75 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'Write'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches, %.2f cm tall." % (height, height * 2.54)
print "He's %d pounds, %.2f kg heavy ." % (weight, weight * 0.453)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try  to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)
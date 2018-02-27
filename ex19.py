# -*- coding: utf-8 -*-
def cheeses_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
print "We can just give the function numbers directly:"
cheeses_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amount_of_cheeses = 10
amount_of_crackers = 50

cheeses_and_crackers(amount_of_cheeses, amount_of_crackers)


print "We can even do math inside too:"
cheeses_and_crackers(10+20, 5+6)

print "And we can combine the two, variables and math:"
cheeses_and_crackers(amount_of_cheeses + 100, amount_of_crackers + 1000)

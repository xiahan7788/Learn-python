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

# use math 
print "We can even do math inside too:"
cheeses_and_crackers(10+20, 5+6)

# use variables and numbers inside as arguments
print "And we can combine the two, variables and math:"
cheeses_and_crackers(amount_of_cheeses + 100, amount_of_crackers + 1000)


def animals_legs(animals_count, legs_count):
	print "There are %d animals!" % animals_count
	print "And there are %d legs." % legs_count
	print "This is a funny question."
	print "Let's enjoy it, come on baby!\n"
	
print "How many legs do 20 chickens have?"
animals_legs(20, 20*4)


print "And, how many legs do 10 snake and 13 dogs have?"
snakes = 10
dogs = 13
animals_legs(snakes + dogs, snakes * 0 + dogs * 4)


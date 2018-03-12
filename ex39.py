#!/usr/bin/env
# -*- coding: utf-8 -*-

# create a basic set of states and some cities in them
cities = {'CA': 'San Franciso',
	'MI': 'Detriot',
	'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap, state):
	if state in themap:
		return themap[state]
	else:
		return "not found."
		
# ok pay attention!
cities['_find'] = find_city

print cities

while True:
	print ("State? (ENTER to quit)",)
	state = raw_input("> ")
	
	if not state: break
	
	# this line is the most important ever! study!
	city_found = cities['_find'](cities, state)
	print city_found
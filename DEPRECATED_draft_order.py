'''
Author:         @midnightslacker
Last Update:   07/6/2024
Description:    ECF Fantasy Football draft order.
'''

#!/usr/bin/env python3
import random

YEAR = 2024

# Make an array of Team Owners
OWNERS = ['Hiren', 'Gruver', 'Ressler', 'Christ', 'Shawn', 'Jairus', 'Void', 'Scuba', 'Nick A', 'Adam', 'Hunt', 'Donch']

# counter to change behavior for last pick
COUNTER = 1

# shuffle the list
random.shuffle(OWNERS)

# pick a random sample from the shuffled list
for name in random.sample(OWNERS, len(OWNERS)):
    print (str(COUNTER) + ": " + str(name))
    COUNTER+=1

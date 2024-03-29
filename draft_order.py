'''
Author:         @midnightslacker
Last Updatee:   03/06/2022
Description:    ECF Fantasy Football draft order.
'''

#!/usr/bin/env python3
import random

YEAR = 2022

# Make an array of Team Owners
OWNERS = ['Scuba', 'NickA', 'Hunt', 'Christ', 'Hiren', 'Jairus', 'Pal', 'Gruver', 'Ressler', 'Shawn', 'Void', 'Donch']

# counter to change behavior for last pick
COUNTER = 1

# shuffle the list
random.shuffle(OWNERS)

# pick a random sample from the shuffled list
for name in random.sample(OWNERS, len(OWNERS)):
    print (str(COUNTER) + ": " + str(name))
    COUNTER+=1

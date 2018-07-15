#!/usr/bin/env python3.4

import random
from subprocess import call

year = 2018

# Make an array of Team Owners
owners = ['Scuba', 'NickA', 'Hunt', 'Christ', 'Hiren', 'Jairus', 'Pal', 'Gruver', 'Ressler', 'Shawn', 'Void', 'Donch']

# counter to change behavior for last pick
counter = 1

for name in random.sample(owners, len(owners)):
    print (str(counter) + ": " + str(name))
    counter+=1

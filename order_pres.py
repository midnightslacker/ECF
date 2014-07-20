#!/usr/bin/env python3.4

import random
from subprocess import call

year = 2014

# Make an array of Team Owners
owners = ['Hunt', 'Void', 'Shawn', 'Jairus', 'Jake', 'Pal', 'Nick A', 'Scuba', 'Guver', 'Christ', 'Donch', 'Ressler']

# counter to change behavior for last pick
counter = 0

def pretty_print(pick):
    if pick == 0:
        print ("The first pick in the %i ECF Draft goes too:\n" %(year))
    elif pick == 1:
        print ("The second pick in the %i ECF Draft goes too:\n" %(year))
    elif pick == 2:
        print ("The third pick in the %i ECF Draft goes too:\n" %(year))
    elif pick == 3:
        print ("The fourth pick in the %i ECF Draft goes too:\n" %(year))
    elif pick == 4:
        print ("The fifth pick in the %i ECF Draft goes too:\n" %(year))
    elif pick == 5:
        print ("The sixth pick in the %i ECF Draft goes too:\n" %(year))
    elif pick == 6:
        print ("The seventh pick in the %i ECF Draft goes too:\n" %(year))
    elif pick == 7:
        print ("The eighth pick in the %i ECF Draft goes too:\n" %(year))
    elif pick == 8:
        print ("The ninth pick in the %i ECF Draft goes too:\n" %(year))
    elif pick == 9:
        print ("The tenth pick in the %i ECF Draft goes too:\n" %(year))
    elif pick == 10:
        print ("The eleventh pick in the %i ECF Draft goes too:\n" %(year))
    else:
        print ("The last pick in the %i ECF Draft goes too:\n" %(year))

for name in random.sample(owners, len(owners)):
    pretty_print(counter)
    input()
    call(["banner", str(name)])
    print("\n")
    counter+=1

'''
Created on: April 5, 2013
@author: midnightslacker
Description: Creates Schedule for ECF Fantasy Football League
'''

import sys, random

#Create a list for number of teams
seq = [1,2,3,4,5,6,7,8,9,10,11,12]

#Create the dictionary/hash of owners
owners = {1:"Christ",
          2:"Gruver",
          3:"Miller",
          4:"Millen",
          5:"Huntington",
          6:"Nick A.",
          7:"Ressler",
          8:"Pal",
          9:"Doncsecz",
          10:"Powell",
          11:"Sicher",
          12:"Void"}

#create lists for each week
week1 = random.sample(seq, 12)

for game in week1:
    print (game)

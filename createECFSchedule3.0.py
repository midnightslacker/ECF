'''
Created on: April 5, 2013
@author: midnightslacker
Description: Creates Schedule for ECF Fantasy Football League
Considerations: Weeks 1-3 and Weeks 11-13 are special cases.
                I want teams playing there division rivals first and last weeks

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

#Create divisions for excluding from remaining schedule
dNorth = ["Miller", "Millen", "Void"]
dEast  = ["Christ", "Sicher", "Doncsecz"]
dWest  = ["Nick A.", "Powell", "Huntington"]
dSouth = ["Ressler", "Pal", "Gruver"]


#create sequence for remaing games for each owner.
christ_seq = [3,4,6,7,8,10,12]

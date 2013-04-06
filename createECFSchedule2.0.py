import sys, random

#Create a list for number of teams
seq = [1,2,3,4,5,6,7,8,9,10,11,12]

#Create dictionary for Owners
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

owners2 = {}

#Create divisions for excluding from schedule
dNorth = ["Miller", "Millen", "Void"]
dEast  = ["Christ", "Sicher", "Doncsecz"]
dWest  = ["Nick A.", "Powell", "Huntington"]
dSouth = ["Ressler", "Pal", "Gruver"]

for key, value in owners.items():
    owners2.update( {value:random.sample(seq,9)} )

for key, value in owners2.items():
    if len(key) < 5:
        print ( repr(key), "\t\t\t\t", value )
    else:
        print ( repr(key), "\t\t\t", value  )

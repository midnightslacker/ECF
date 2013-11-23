
# @author:  midnightslacker
# @contact: midnightslacker11@gmail.com
# @version: 0.3.0 
# 
# Creates Schedule for ECF Fantasy Football League
# 

import sys, random

# Create the dictionary/hash of owners
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

# Create Divisions -- #'s correlate to owners #
North   = [3,4,12]
East    = [1,9,11]
West    = [5,6,10]
South   = [2,7,8]


# create sequence for ALL games for each owner
# -- Owners play everyone (except for themselves
# -- Owners play their divisional opponents 2x
christ_seq = [2,3,4,5,6,7,8,9,9,10,11,11,12]
gruver_seq = [1,3,4,5,6,7,7,8,8,9,10,11,12]
miller_seq = [1,2,4,4,5,6,7,8,9,10,11,12,12]
millen_seq = [1,2,3,3,5,6,7,8,9,10,11,12,12]
hunt_seq   = [1,2,3,4,6,6,7,8,9,10,10,11,12]
nickA_seq  = [1,2,3,4,5,5,7,8,9,10,10,11,12]
ressler_seq= [1,2,2,3,4,5,6,8,8,9,10,11,12]
pal_seq    = [1,2,2,3,4,5,6,7,7,9,10,11,12]
donch_seq  = [1,1,2,3,4,5,6,7,8,10,11,11,12]
powell_seq = [1,2,3,4,5,5,6,6,7,8,9,11,12]
sicher_seq = [1,1,2,3,4,5,6,7,8,9,9,10,12]
void_seq   = [1,2,3,3,4,4,5,6,7,8,9,10,11]

#create a list of lists
ownerSched = [christ_seq, gruver_seq, miller_seq, millen_seq, hunt_seq,
              nickA_seq, ressler_seq, pal_seq, donch_seq, powell_seq,
              sicher_seq, void_seq]

def uniqueGames( week ):
    print 'hello'

def checkOwnersSchedule ( owner_seq ):
    print 'hello'
    
    #Owner's must play everyone and their division rivals 2x


def RemainingSchedule( ownersName, seq ):
    print "** " + str(ownersName) + "'s" + " Schedule **"
    week = 1;

    for opp in random.sample( seq, 13):
        print "Week " + str(week) + ": " + str( owners.get(opp) )
        week += 1

def PrintSchedule():
    ownerVal = 0
    for owner in owners:
        RemainingSchedule( owners.get(owner) , ownerSched[ownerVal] )
        if ownerVal < 14:
            ownerVal += 1

PrintSchedule()








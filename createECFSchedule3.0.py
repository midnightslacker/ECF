'''
Created on: April 5, 2013
@author: midnightslacker
Description: Creates Schedule for ECF Fantasy Football League
Considerations: Weeks 1-3 and Weeks 11-13 are special cases.
                I want teams playing there division rivals first and last weeks

'''

import sys, random

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



#create sequence for remaing games for each owner.
christ_seq = [3,4,6,7,8,10,12]
gruver_seq = [3,4,5,9,10,11,12]
miller_seq = [1,2,5,7,8,9,11]
millen_seq = [1,2,6,8,9,10,11]
hunt_seq   = [2,3,7,8,9,11,12]
nickA_seq  = [1,4,7,8,9,11,12]
ressler_seq= [1,3,5,6,9,10,11]
pal_seq    = [1,3,4,5,6,10,12]
donch_seq  = [2,3,4,5,6,7,10]
powell_seq = [1,2,4,7,8,9,12]
sicher_seq = [2,3,4,5,6,7,12]
void_seq   = [1,2,5,6,8,10,11]

#create a list of lists
ownerSched = [christ_seq, gruver_seq, miller_seq, millen_seq, hunt_seq,
              nickA_seq, ressler_seq, pal_seq, donch_seq, powell_seq,
              sicher_seq, void_seq]


def RemainingSchedule( ownersName, seq ):
    print "** " + str(ownersName) + "'s" + " Schedule **"
    week = 4;

    for opp in random.sample( seq, 7):
        print "Week " + str(week) + ": " + str( owners.get(opp) )
        week += 1
        
def PrintSchedule():
    ownerVal = 0
    for owner in owners:
        RemainingSchedule( owners.get(owner) , ownerSched[ownerVal] )
        if ownerVal < 11:
            ownerVal += 1

PrintSchedule()








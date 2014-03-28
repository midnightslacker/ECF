import random

numOfEntries = 12
teamSequence = [1,2,3,4,5,6,7,8,9,10,11,12]
ownerList = []

def randomList (myList, numOfEntries):
    while len(ownerList) < 12:
        for opp in random.sample(myList, numOfEntries):
            ownerList.append(opp)
            if opp in ownerList:
                teamSequence.remove(opp)
                --numOfEntries
    print ownerList

randomList(teamSequence, numOfEntries)

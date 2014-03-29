North = [6,7,8]
team_6 = []
teamID = 6
scheduleLength = 13

def makeOppPop (emptyList, division, teamID):
    
    for i in range(12):
        # Can't play yourself, break out of the loop and don't add it to the list
        if i == teamID:
            continue
        
        emptyList.append(i)
        
        # You play your division rivals 2x, so add them to the list again.
        if i in division:
            emptyList.append(i)

    print emptyList

makeOppPop(team_6, North, teamID)


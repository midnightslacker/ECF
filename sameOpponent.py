teamList1 = [1,2,3,4,5,6,7,8,9]
teamList2 = [9,8,7,6,5,4,3,2,9]

# The only problem should be weeks 5 and 9

def checkOpponents(teamList1, teamList2):
    counter = 0
    while counter < len(teamList1):
        if teamList1[counter] == teamList2[counter]:
            print "There is a problem. These two teams are playing the same team during week " + str(counter+1)
        counter+=1

checkOpponents(teamList1, teamList2)

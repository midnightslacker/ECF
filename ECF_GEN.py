#!/usr/bin/env python
import random

# Owner's ID by division
North = [1,2,3]
East =  [4,5,6]
South = [7,8,9]
West = [10,11,12]

# Make an array of Team Owners -- Array index mathces Team ID in Divisions
owners = ['', 'Hunt', 'Void', 'Shawn', 'Jairus', 'Jake', 'Pal', 'Nick', 'Scuba', 'Guver', 'Christ', 'Donch', 'Ressler']

# Set up empty list for each week
week1 = []
week2 = []
week3 = []
week4 = []
week5 = []
week6 = []
week7 = []
week8 = []
week9 = []
week10 = []
week11 = []
week12 = []
week13 = []

def createFirst (div1, div2, weekA, weekB, weekC):
    ''' Generate games for first quarter '''
    opp = 0
    
    # week A
    game1 = (div1[opp], div1[opp+1])
    weekA.append(game1)
    game2 = (div1[opp+2], div2[opp])
    weekA.append(game2)
    game3 = (div2[opp+1], div2[opp+2])
    weekA.append(game3)

    # week B
    game1 = (div1[opp+1], div1[opp+2])
    weekB.append(game1)
    game2 = (div2[opp], div2[opp+1])
    weekB.append(game2)
    game3 = (div1[opp], div2[opp+2])
    weekB.append(game3)

    # week C
    game1 = (div1[opp], div1[opp+2])
    weekC.append(game1)
    game2 = (div2[opp], div2[opp+2])
    weekC.append(game2)
    game3 = (div1[opp+1], div2[opp+1])
    weekC.append(game3)


def createMiddle(div1, div2, weekA, weekB, weekC):
    ''' Generate games for middle quarter(s) '''
    opp = 0
    
    # Week A
    game1 = (div1[opp], div2[opp])
    weekA.append(game1)
    game2 = (div1[opp+1], div2[opp+1])
    weekA.append(game2)
    game3 = (div1[opp+2], div2[opp+2])
    weekA.append(game3)

    # Week B
    game1 = (div1[opp], div2[opp+1])
    weekB.append(game1)
    game2 = (div1[opp+1], div2[opp+2])
    weekB.append(game2)
    game3 = (div1[opp+2], div2[opp])
    weekB.append(game3)

    # Week C
    game1 = (div1[opp], div2[opp+2])
    weekC.append(game1)
    game2 = (div1[opp+1], div2[opp])
    weekC.append(game2)
    game3 = (div1[opp+2], div2[opp+1])
    weekC.append(game3)

def createLastAndRemainder(div1, div2, weekA, weekB, weekC, offWeek):
    ''' Generate games for last quarter + 1'''
    opp = 0
    
    # Week A
    game1 = (div1[opp], div1[opp+1])
    weekA.append(game1)
    game2 = (div1[opp+2], div2[opp+1])
    weekA.append(game2)
    game3 = (div2[opp], div2[opp+2])
    weekA.append(game3)

    # Week B
    game1 = (div1[opp+1], div1[opp+2])
    weekB.append(game1)
    game2 = (div1[opp], div2[opp])
    weekB.append(game2)
    game3 = (div2[opp+1], div2[opp+2])
    weekB.append(game3)

    # Week C
    game1 = (div1[opp], div1[opp+2])
    weekC.append(game1)
    game2 = (div1[opp+1], div2[opp+2])
    weekC.append(game2)
    game3 = (div2[opp], div2[opp+1])
    weekC.append(game3)

    # Create the outlier!
    game1 = (div1[opp], div2[opp+1])
    offWeek.append(game1)
    game2 = (div1[opp+1], div2[opp])
    offWeek.append(game2)
    game3 = (div1[opp+2], div2[opp+2])
    offWeek.append(game3)

def shuffleDivision(div):
    ''' shuffle order of division '''
    return random.sample(div, len(div))

def display(week):
    ''' Displays matchups '''
    for game in week:
        print(owners[game[0]] + str('\tvs.\t') + owners[game[1]])

def generateSchedule():
    seed = random.randint(1,120)
    if seed <= 19:
        createFirst(North, South, week1, week2, week3)
        createFirst(East, West, week1, week2, week3)
        
        createMiddle(North, East, week4, week5, week6)
        createMiddle(South, West, week4, week5, week6)
        createMiddle(North, West, week8, week9, week10)
        createMiddle(South, East, week8, week9, week10)
        
        createLastAndRemainder(North, South, week11, week12, week13, week7)
        createLastAndRemainder(East, West, week11, week12, week13, week7)
    
    elif seed > 19 and seed <= 39:
        createFirst(North, South, week1, week2, week3)
        createFirst(East, West, week1, week2, week3)

        createMiddle(North, West, week4, week5, week6)
        createMiddle(South, East, week4, week5, week6)
        createMiddle(North, East, week8, week9, week10)
        createMiddle(South, West, week8, week9, week10)

        createLastAndRemainder(North, South, week11, week12, week13, week7)
        createLastAndRemainder(East, West, week11, week12, week13, week7)

    elif seed > 39 and seed <= 59:
        createFirst(North, East, week1, week2, week3)
        createFirst(South, West, week1, week2, week3)

        createMiddle(North, West, week4, week5, week6)
        createMiddle(South, East, week4, week5, week6)
        createMiddle(North, South, week8, week9, week10)
        createMiddle(East, West, week8, week9, week10)

        createLastAndRemainder(North, East, week11, week12, week13, week7)
        createLastAndRemainder(South, West, week11, week12, week13, week7)

    elif seed > 59 and seed <= 79:
        createFirst(North, East, week1, week2, week3)
        createFirst(South, West, week1, week2, week3)

        createMiddle(North, South, week4, week5, week6)
        createMiddle(West, East, week4, week5, week6)
        createMiddle(North, West, week8, week9, week10)
        createMiddle(South, East, week8, week9, week10)

        createLastAndRemainder(North, East, week11, week12, week13, week7)
        createLastAndRemainder(South, West, week11, week12, week13, week7)

    elif seed > 79 and seed <= 99:
        createFirst(North, West, week1, week2, week3)
        createFirst(South, East, week1, week2, week3)

        createMiddle(North, East, week4, week5, week6)
        createMiddle(West, South, week4, week5, week6)
        createMiddle(North, South, week8, week9, week10)
        createMiddle(West, East, week8, week9, week10)

        createLastAndRemainder(North, West, week11, week12, week13, week7)
        createLastAndRemainder(South, East, week11, week12, week13, week7)
    else:
        createFirst(North, West, week1, week2, week3)
        createFirst(South, East, week1, week2, week3)

        createMiddle(North, South, week4, week5, week6)
        createMiddle(East, West, week4, week5, week6)
        createMiddle(North, East, week8, week9, week10)
        createMiddle(South, West, week8, week9, week10)

        createLastAndRemainder(North, West, week11, week12, week13, week7)
        createLastAndRemainder(South, East, week11, week12, week13, week7)


# Shuffle Divisions
North = shuffleDivision(North)
East = shuffleDivision(East)
South = shuffleDivision(South)
West = shuffleDivision(West)

# Generate the Schedules
generateSchedule()

# Display the Schedule

print('\n\tWeek1:\n')
display(week1)
print('\n\tWeek2:\n')
display(week2)
print('\n\tWeek3:\n')
display(week3)
print('\n\tWeek4:\n')
display(week4)
print('\n\tWeek5:\n')
display(week5)
print('\n\tWeek6:\n')
display(week6)
print('\n\tWeek7:\n')
display(week7)
print('\n\tWeek8:\n')
display(week8)
print('\n\tWeek9:\n')
display(week9)
print('\n\tWeek10:\n')
display(week10)
print('\n\tWeek11:\n')
display(week11)
print('\n\tWeek12:\n')
display(week12)
print('\n\tWeek13:\n')
display(week13)

print ("\n")


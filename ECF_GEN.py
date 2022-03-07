'''
Author:         @midnightslacker
Last Updatee:   03/06/2022
Description:    ECF Fantasy Football Schedule generator.
'''
#!/usr/bin/env python3
import random

# Owner's ID by division
North = [1,2,3]
East =  [4,5,6]
South = [7,8,9]
West = [10,11,12]

# Make an array of Team Owners -- Array index mathces Team ID in Divisions
owners = ['', 'Scuba', 'NickA', 'Hunt', 'Christ', 'Hiren', 'Jairus', 'Pal', 'Gruver', 'Ressler', 'Shawn', 'Void', 'Donch']

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
week14 = []
nonDivisionWeeks = [week4, week5, week6, week7, week8, week9, week10]

def create_first (div1, div2, weekA, weekB, weekC):
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


def create_middle(div1, div2, weekA, weekB, weekC):
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

def create_last_and_remainder(div1, div2, weekA, weekB, weekC, off_week):
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
    off_week.append(game1)
    game2 = (div1[opp+1], div2[opp])
    off_week.append(game2)
    game3 = (div1[opp+2], div2[opp+2])
    off_week.append(game3)

def shuffle_division(div):
    ''' shuffle order of division '''
    return random.sample(div, len(div))

def display(week):
    ''' Displays matchups '''
    for game in week:
        print(owners[game[0]] + str('\tvs.\t') + owners[game[1]])

def generate_schedule():
    '''Pseudo randomly (while following rules) generate the schedule '''
    seed = random.randint(1,120)
    if seed <= 19:
        create_first(North, South, week1, week2, week3)
        create_first(East, West, week1, week2, week3)

        create_middle(North, East, week4, week5, week6)
        create_middle(South, West, week4, week5, week6)
        create_middle(North, West, week8, week9, week10)
        create_middle(South, East, week8, week9, week10)

        create_last_and_remainder(North, South, week11, week12, week13, week7)
        create_last_and_remainder(East, West, week11, week12, week13, week7)

    elif seed > 19 and seed <= 39:
        create_first(North, South, week1, week2, week3)
        create_first(East, West, week1, week2, week3)

        create_middle(North, West, week4, week5, week6)
        create_middle(South, East, week4, week5, week6)
        create_middle(North, East, week8, week9, week10)
        create_middle(South, West, week8, week9, week10)

        create_last_and_remainder(North, South, week11, week12, week13, week7)
        create_last_and_remainder(East, West, week11, week12, week13, week7)

    elif seed > 39 and seed <= 59:
        create_first(North, East, week1, week2, week3)
        create_first(South, West, week1, week2, week3)

        create_middle(North, West, week4, week5, week6)
        create_middle(South, East, week4, week5, week6)
        create_middle(North, South, week8, week9, week10)
        create_middle(East, West, week8, week9, week10)

        create_last_and_remainder(North, East, week11, week12, week13, week7)
        create_last_and_remainder(South, West, week11, week12, week13, week7)

    elif seed > 59 and seed <= 79:
        create_first(North, East, week1, week2, week3)
        create_first(South, West, week1, week2, week3)

        create_middle(North, South, week4, week5, week6)
        create_middle(West, East, week4, week5, week6)
        create_middle(North, West, week8, week9, week10)
        create_middle(South, East, week8, week9, week10)

        create_last_and_remainder(North, East, week11, week12, week13, week7)
        create_last_and_remainder(South, West, week11, week12, week13, week7)

    elif seed > 79 and seed <= 99:
        create_first(North, West, week1, week2, week3)
        create_first(South, East, week1, week2, week3)

        create_middle(North, East, week4, week5, week6)
        create_middle(West, South, week4, week5, week6)
        create_middle(North, South, week8, week9, week10)
        create_middle(West, East, week8, week9, week10)

        create_last_and_remainder(North, West, week11, week12, week13, week7)
        create_last_and_remainder(South, East, week11, week12, week13, week7)
    else:
        create_first(North, West, week1, week2, week3)
        create_first(South, East, week1, week2, week3)

        create_middle(North, South, week4, week5, week6)
        create_middle(East, West, week4, week5, week6)
        create_middle(North, East, week8, week9, week10)
        create_middle(South, West, week8, week9, week10)

        create_last_and_remainder(North, West, week11, week12, week13, week7)
        create_last_and_remainder(South, East, week11, week12, week13, week7)

# Shuffle Divisions to add more randomness
North = shuffle_division(North)
East = shuffle_division(East)
South = shuffle_division(South)
West = shuffle_division(West)

# Generate the Schedules
generate_schedule()

# Display the Schedule
print('\n\tWeek 1:\n')
display(week1)
print('\n\tWeek 2:\n')
display(week2)
print('\n\tWeek 3:\n')
display(week3)
print('\n\tWeek 4:\n')
display(week4)
print('\n\tWeek 5:\n')
display(week5)
print('\n\tWeek 6:\n')
display(week6)
print('\n\tWeek 7:\n')
display(week7)
print('\n\tWeek 8:\n')
display(week8)
print('\n\tWeek 9:\n')
display(week9)
print('\n\tWeek 10:\n')
display(week10)
print('\n\tWeek 11:\n')
display(week11)
print('\n\tWeek 12:\n')
display(week12)
print('\n\tWeek 13:\n')
display(week13)
# create week 14 from random, non-division week
week14 = random.choice(nonDivisionWeeks)
print('\n\tWeek 14:\n')
display(week14)
print ("\n")

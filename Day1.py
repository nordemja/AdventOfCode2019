'''
Title: Advent of Code 2019 - Day 1
Creator: Justin Nordeman
'''

import math

#open file
fileName = open("C:\\Users\\justi\\Documents\\Python Programming\\AdventOfCode2019\\Day1Input.txt", "r")

#read the file and make list of int values for each value from file
intList = [int(x) for x in fileName.readlines()]


            ### PART 1 ###

#list to calculate final sum needed
fuelReq = []

#perform specified calculations and append to final list
for each in intList:
    fuelReq.append(math.floor(each/3) - 2)

print("Total Fuel Required part 1: " + str(sum(fuelReq)))


            ### PART 2 ###

'''
FUNCTION NAME: fuelRequirementSum

FUNCTION DESCRIPTION: recursively calculate the sum of fuel requirements for each module

ARGUMENTS: 
    num = value that is passed to function as the result of the first calculation
'''

def moduleFuelRequirementSum(num):
    if num <= 0:
        return 0
    else:
        return num + moduleFuelRequirementSum(math.floor(num/3) - 2)

#initalize grand total variable
totalSum = 0

#loop through each module to calculate modular fuel requirements
for each in intList:

    #need to perform first calculation outside of recursive function
    firstCalc = math.floor(each/3) - 2

    #call function to add each modular fuel requirement then add to grand total
    moduleFuelReq = moduleFuelRequirementSum(firstCalc)
    totalSum += moduleFuelReq

print("Total Fuel Requirement Part 2: " + str(totalSum))

fileName.close()

from collections import Counter

#puzzle inputs
start = 372037
end = 905157

#for list of strings in range of puzzle inputs in order to iterate
codeList = [str(each) for each in range(start, end+1)]

def isInOrder(lst):

    '''
    FUNCTION_NAME = isInOrder

    ARGUMENTS = lst

    DESCRIPTION = 

    '''

    previous = lst[0]

    for num in lst:
        if num < previous:
            return False
        previous = num
    return True

def twoConesecutiveEqualValues(lst):
    for i in range(len(lst) - 1):
        if lst[i] == lst[i+1]:
            return True
    return False

def meetRequirements(lst):
    fitsRequirements = 0
    for each in lst:
        for x in range(len(each)-1):
            if twoConesecutiveEqualValues(each) == True and isInOrder(each) == True:
                fitsRequirements += 1
                break

    return fitsRequirements

def partTwo(lst):
    a = Counter(lst)
    for letter in lst:
        if a[letter] == 2:
            return True
    return False


def meetRequirementsPartTwo(lst):
    fitsRequirements = 0
    for each in lst:
        for x in range(len(each)-1):
            if twoConesecutiveEqualValues(each) and isInOrder(each) and partTwo(each):
                fitsRequirements += 1
                break

    return fitsRequirements
            
print("Total Amount Fitting Requirements Part 1 = " + str(meetRequirements(codeList)))
print("Total Amount Fitting Requirements Part 2 = " +str(meetRequirementsPartTwo(codeList)))
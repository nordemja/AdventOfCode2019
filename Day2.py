filePath = open("C:\\Users\\justi\\Documents\\Python Programming\\Advent of Code\\Day2Input.txt", "r")
fileString = filePath.read()

def convertToList(fileName):
    #split at commas to create a list of numeric values
    splittedList = fileString.split(',')

    #loop through split list to convert strings to ints
    for each in range(0, len(splittedList)):
        splittedList[each] = int(splittedList[each])
    
    return splittedList

######################### PART 1 #########################

def intcodeFinder(lst):

    currentPositon = 0
    while True:
        if lst[currentPositon] == 1:
            lst[lst[currentPositon + 3]] = lst[lst[currentPositon + 1]] + lst[lst[currentPositon + 2]]
            currentPositon += 4
        elif lst[currentPositon] == 2:
            lst[lst[currentPositon + 3]] = lst[lst[currentPositon + 1]] * lst[lst[currentPositon + 2]]
            currentPositon += 4
        elif lst[currentPositon] == 99:
            break

    return lst[0]

workingList = convertToList(filePath)
workingList[1], workingList[2] = 12,2
print("Value at index 0 after running intcode finder = " + str(intcodeFinder(workingList)))

######################### PART 2 #########################

def taskTwo():
    
    target = 19690720
    initialMemory = convertToList(fileString)
    for x in range (1,100):
        initialMemory[1] = x
        for y in range (1,100):
            initialMemory[2] = y
            if intcodeFinder(initialMemory) == target:
                print("noun = " + str(initialMemory[1]))
                print("verb = " + str(initialMemory[2]))
                break
            initialMemory = convertToList(fileString)
            initialMemory[1] = x
        initialMemory = convertToList(fileString)
        
taskTwo()
filePath.close()
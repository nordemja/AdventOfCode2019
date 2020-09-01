fileName = open('C:\\Users\\justi\\Documents\\Python Programming\\AdventOfCode2019\\Day5Input.txt', 'r')

# read file and make into list of integers
fileStringList = fileName.read().split(',')
fileIntList = [int(each) for each in fileStringList]

print(fileIntList)


fileName.close()
import os

#Makes a variable called location to store the location of the py file
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = open(os.path.join(__location__, 'data.txt')) 

column1  = []
column2  = []
column3  = []
column4  = []
column5  = []
column6  = []
column7  = []
column8  = []
column9  = []
column10 = []
column11 = []
column12 = []

gamma = 0
epsilon = 0
def mostCommonNumber(column):
    mostCommon = 0
    numbers = {} #stores a dictionarty of the most common numbers
    for number in column:
        if number in numbers:
            numbers[number] += 1
        else:
            numbers[number] = 1
    print(numbers)
    if(numbers[1] > numbers[0]):
        mostCommon = 1 
    return mostCommon


def leastCommonNumber(column):
    leastCommon = 0
    numbers = {} #stores a dictionarty of the most common numbers
    for number in column:
        if number in numbers:
            numbers[number] += 1
        else:
            numbers[number] = 1
    print(numbers)
    if(numbers[1] < numbers[0]):
        leastCommon = 1 
    return leastCommon

for line in file.readlines():
    column1.append(int(line[0]))
    column2.append(int(line[1]))
    column3.append(int(line[2]))
    column4.append(int(line[3]))
    column5.append(int(line[4]))
    column6.append(int(line[5]))
    column7.append(int(line[6]))
    column8.append(int(line[7]))
    column9.append(int(line[8]))
    column10.append(int(line[9]))
    column11.append(int(line[10]))
    column12.append(int(line[11]))

gamma = str(mostCommonNumber(column1)) + str(mostCommonNumber(column2)) + str(mostCommonNumber(column3)) + str(mostCommonNumber(column4)) + str(mostCommonNumber(column5)) + str(mostCommonNumber(column6)) + str(mostCommonNumber(column7)) + str(mostCommonNumber(column8)) + str(mostCommonNumber(column9)) + str(mostCommonNumber(column10)) + str(mostCommonNumber(column11)) + str(mostCommonNumber(column12))
epsilon = str(leastCommonNumber(column1)) + str(leastCommonNumber(column2)) + str(leastCommonNumber(column3)) + str(leastCommonNumber(column4)) + str(leastCommonNumber(column5)) + str(leastCommonNumber(column6)) + str(leastCommonNumber(column7)) + str(leastCommonNumber(column8)) + str(leastCommonNumber(column9)) + str(leastCommonNumber(column10)) + str(leastCommonNumber(column11)) + str(leastCommonNumber(column12))
print(gamma)
print(epsilon)
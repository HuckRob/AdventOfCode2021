import os
import numpy

#Makes a variable called location to store the location of the py file
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = open(os.path.join(__location__, 'data.txt')) 

bingoNumbers = []
bingoBoards = []

numbersIn = file.readline().rstrip()
numbersIn = numbersIn.split(",")
for x in numbersIn:
    bingoNumbers.append(x)

for line in file.readlines():
    allNumbers = line.split(' ')
    currentBingoBoard = []
    if(line.startswith('\n')):
        line.strip()
        bingoBoards.append(currentBingoBoard)
        currentBingoBoard = []
    else:
       newRow = numpy.array(line)
       currentBingoBoard.append(newRow)
    print(allNumbers)
        
#print(bingoNumbers)
print(bingoBoards)
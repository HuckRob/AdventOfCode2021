import os

#Makes a variable called location to store the location of the py file
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

file = open(os.path.join(__location__, 'data.txt')) 

numbList = []
numbListGrouped = []
prevNumb = 0
tally = 0


for line in file.readlines():
    numbList.append(int(line))
    


#indexing starting at 1 so it can view 0 and 2
#indexing finishes at array length - 1 so it can get the average of the last 3 
    
for i in range(1,(len(numbList) - 1)):
    numOne = numbList[i-1]
    numTwo = numbList[i]
    numThree = numbList[i+1]
    numSum = numOne + numTwo + numThree
    numbListGrouped.append(numSum)


for i in range(0,len(numbListGrouped)):
    if(numbListGrouped[i] > numbListGrouped[i-1]):
        tally = tally + 1
    

print(tally)
import os

#Makes a variable called location to store the location of the py file
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = open(os.path.join(__location__, 'data.txt')) 
prevNumb = 0
tally = 0


for line in file.readlines():
    if(int(line) > prevNumb):
        prevNumb = int(line)
        tally = tally + 1
    else:
        prevNumb = int(line)

print(tally)
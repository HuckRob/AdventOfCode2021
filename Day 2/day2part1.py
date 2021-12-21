import os

#Makes a variable called location to store the location of the py file
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = open(os.path.join(__location__, 'data.txt')) 

depth = 0
horizontalPos = 0
for line in file.readlines():
    line = line.split(' ')
    if(line[0] == 'forward'):
        print('forward ' +  line[1])
        horizontalPos = horizontalPos + int(line[1])
    if(line[0] == 'down'):
        print('down ' + line[1])
        depth = depth + int(line[1])
    if(line[0] == 'up'):
        print('up ' + line[1])
        depth = depth - int(line[1])
print('depth: ' + str(depth))
print('horizontal position: ' + str(horizontalPos))
print('depth times horizontal position : ' + str((depth * horizontalPos)))
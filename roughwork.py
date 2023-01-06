import re

position=[]

with open('frameInfo.txt','r') as f:
    lines=f.readlines() 
for line in lines:
    position.append(int(re.sub("\D", "", line)))

position.sort()

i=0
while i<len(position)-1:
    if position[i]+5>position[i+1]:
        position.pop(i+1)
        print(position)
    else:
        i+=1
print(position)
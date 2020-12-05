input = [1,1,1,3,1,2,2,1,1,3]
output = []
currNum = 0
ctr = 0
currIndex = 0
for a in xrange(50):

    while currIndex <= len(input)-1:
        currNum = input[currIndex]
        ctr = 1
        #print(currIndex)
        if currIndex + ctr < len(input):
            while(input[currIndex+ctr] == currNum):
                #print(currNum, input[currIndex+ctr])
                ctr += 1
                if currIndex + ctr >= len(input):
                    break
        output.append(ctr)
        output.append(currNum)
    
        currIndex += ctr

    currIndex = 0
    ctr = 0
    input = output
    output = []
print(len(input))  
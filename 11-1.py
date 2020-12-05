# Must be 8 lower case letters
# Increment old PW until valid
# At least one 3 char straight
# Cannot contain i o or l
# Must contain 2 different pairs (non-overlapping)  (aa, bb, pp)

currPassword = 'cqjxjnds'
passwordKey = [2, 16, 9, 23, 9, 13, 3, 18]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 0, 0]
newPassword = ''
x = 0
pairs = 0
badPW = False
seqStart = 0
currLetter = ''
seqFound = False
noBadLetters = False
firstPasswordFound = False

while True:
    passwordKey[7] += 1
    if passwordKey[7] == 26:
        passwordKey[7] = 0
        passwordKey[6] += 1
        if passwordKey[6] == 26:
            passwordKey[6] = 0
            passwordKey[5] += 1
            if passwordKey[5] == 26:
                passwordKey[5] = 0
                passwordKey[4] += 1
                if passwordKey[4] == 26:
                    passwordKey[4] = 0
                    passwordKey[3] += 1
                    if passwordKey[3] == 26:
                        passwordKey[3] = 0
                        passwordKey[2] += 1
                        if passwordKey[2] == 26:
                            passwordKey[2] = 0
                            passwordKey[1] += 1
                            if passwordKey[1] == 26:
                                passwordKey[1] = 0
                                passwordKey[0] += 1
   
    newPassword = letters[passwordKey[0]] + letters[passwordKey[1]] + letters[passwordKey[2]] + letters[passwordKey[3]] + letters[passwordKey[4]] + letters[passwordKey[5]] + letters[passwordKey[6]] + letters[passwordKey[7]]


    if 'i' not in newPassword and 'o' not in newPassword and 'l' not in newPassword:
            noBadLetters = True
    
    if noBadLetters:
        while x < len(newPassword)-1:
            if newPassword[x] == newPassword[x+1]:
                pairs += 1
                x += 1
            x += 1
    x = 0

    if noBadLetters and pairs >= 2:
        while x < len(newPassword)-3:
            currLetter = newPassword[x]
            seqStart = letters.index(currLetter)
            if newPassword[x+1] == letters[seqStart+1] and newPassword[x+2] == letters[seqStart+2]:
                seqFound = True
            x += 1
    x = 0

    if noBadLetters and pairs >= 2 and seqFound:
        if firstPasswordFound:
            print("Second = ", newPassword)
            break
        else:
            print("first = ", newPassword)
            firstPasswordFound = True
        

    noBadLetters = False
    pairs = 0
    seqFound = False


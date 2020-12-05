file = open('12-2-In.txt', 'r') 
char = ''
num1 = 0
num2 = 0
num3 = 0
num1Ex = False
num2Ex = False
num3Ex = False
neg = False
lastChar = '+'
currNum = 0
sign = 1
totalizer = 0


while 1: 
    char = file.read(1)      
    print(char)    
    if not char:  
        break
    if char.isdigit() and char != '\"':
        #print(char) 
        if lastChar == '-':
            neg = True
        if num1Ex == False:
            num1Ex = True
            num1 = int(char)
        elif num2Ex == False:
            num2Ex = True
            num2 = int(char)
        elif num3Ex == False:
            num3Ex = True
            num3 = int(char)
    else:

        if neg == True:
            sign = -1
        else:
            sign = 1
        if num3Ex:
            currNum = (sign)*(num1*100+num2*10+num3)
            totalizer += currNum
        elif num2Ex:
            currNum = (sign)*(num1*10+num2)
            totalizer += currNum
        elif num1Ex:
            currNum = (sign)*(num1)
            totalizer += currNum
        if currNum != 0:
            print(currNum)
        neg = False
        num1Ex = False
        num2Ex = False
        num3Ex = False
        num1 = 0
        num2 = 0
        num3 = 0
    lastChar = char
    currNum = 0
            
print(totalizer)
file.close() 
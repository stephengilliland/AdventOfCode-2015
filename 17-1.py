from itertools import combinations

jars = [50,44,11,49,42,46,18,32,26,40,21,7,18,43,10,47,36,24,22,40]
#jars = [20, 5, 15, 10, 5, 10]

jarLen = 20
capacity = 150
currCombo = []
jarSets = []
jarSetsUnique = []
ozCtr = 0
goodSets = 0
print(jars)
ctr = 0
forties = 0
eighteens = 0
currSet = []
for x in xrange(0, jarLen):
    combos = combinations(jars, x)
    for combo in combos:
        currCombo = combo
        for y in xrange(len(currCombo)):
            ozCtr += currCombo[y]
            if ozCtr == capacity and currCombo[:y+1] not in jarSets:
                jarSets.append(currCombo[:y+1])
                currSet = currCombo[:y+1]
                if currSet.count(40) == 1:
                        goodSets += 1
                if currSet.count(18) == 1:
                        goodSets += 1
                if currSet.count(18) == 1 and currSet.count(40) == 1:
                    goodSets += 1
                goodSets += 1
                print(goodSets)
                break
            if ozCtr > capacity:
                break
        ozCtr = 0

print(goodSets)



        

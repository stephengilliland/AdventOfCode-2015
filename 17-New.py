from itertools import combinations
jars = [50,44,11,49,42,46,18,32,26,40,21,7,18,43,10,47,36,24,22,40]
jarLen = 20
capacity = 150
goodSets = 0
length = 100
for x in xrange(0, 20):
    combos = combinations(jars, x)
    for combo in combos:
        if sum(combo) == capacity and len(combo) == 4:
            if len(combo) < length:
                length = len(combo)
            goodSets += 1
print(goodSets)



        

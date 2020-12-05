
from itertools import permutations 

inpt = {"Alice-Bob": -57,
"Alice-Carol": -62,
"Alice-David": -75,
"Alice-Eric": 71,
"Alice-Frank": -22,
"Alice-George": -23,
"Alice-Mallory": -76,
"Bob-Alice": -14,
"Bob-Carol": 48,
"Bob-David": 89,
"Bob-Eric": 86,
"Bob-Frank": -2,
"Bob-George": 27,
"Bob-Mallory": 19,
"Carol-Alice": 37,
"Carol-Bob": 45,
"Carol-David": 24,
"Carol-Eric": 5,
"Carol-Frank": -68,
"Carol-George": -25,
"Carol-Mallory": 30,
"David-Alice": -51,
"David-Bob": 34,
"David-Carol": 99,
"David-Eric": 91,
"David-Frank": -38,
"David-George": 60,
"David-Mallory": -63,
"Eric-Alice": 23,
"Eric-Bob": -69,
"Eric-Carol": -33,
"Eric-David": -47,
"Eric-Frank": 75,
"Eric-George": 82,
"Eric-Mallory": 13,
"Frank-Alice": 77,
"Frank-Bob": 27,
"Frank-Carol": -87,
"Frank-David": 74,
"Frank-Eric": -41,
"Frank-George": -99,
"Frank-Mallory": 26,
"George-Alice": -63,
"George-Bob": -51,
"George-Carol": -60,
"George-David": 30,
"George-Eric": -100,
"George-Frank": -63,
"George-Mallory": 57,
"Mallory-Alice": -71,
"Mallory-Bob": -28,
"Mallory-Carol": -10,
"Mallory-David": 44,
"Mallory-Eric": 22,
"Mallory-Frank": 79,
"Mallory-George": -16,
"Steve-Alice": 0,
"Steve-Bob": 0,
"Steve-Carol": 0,
"Steve-David": 0,
"Steve-Eric": 0,
"Steve-Frank": 0,
"Steve-George": 0,
"Steve-Mallory": 0,
"Alice-Steve": 0,
"Bob-Steve": 0,
"Carol-Steve": 0,
"David-Steve": 0,
"Eric-Steve": 0,
"Frank-Steve": 0,
"George-Steve": 0,
"Mallory-Steve": 0}

people = ["Alice", "Mallory", "Bob", "Carol", "David", "Eric", "Frank", "George", "Steve"]

options = permutations(people)
happiness = []
currHappiness = 0
currNextTo = ""
currArrangement = []
print(options)
currNextToRev = ""

for option in options:
    currArrangement = list(option)
    currArrangement.append(currArrangement[0])
    print(currArrangement)
    for x in xrange(len(option)):
        currNextTo = currArrangement[x] + '-' + currArrangement[x+1]
        currNextToRev = currArrangement[x+1] + '-' + currArrangement[x]
        currHappiness += inpt[currNextTo] 
        currHappiness += inpt[currNextToRev] 
    happiness.append(currHappiness)
    currHappiness = 0

print(max(happiness))

# 527 too low
# 601 too low
        
from itertools import permutations

test = [1,2]

perm = permutations(test)
ctr = 1

for combo in perm:
    print(combo)
    print(combo[1])

# Dancer can fly 27 km/s for 5 seconds, but then must rest for 132 seconds.
# Cupid can fly 22 km/s for 2 seconds, but then must rest for 41 seconds.
# Rudolph can fly 11 km/s for 5 seconds, but then must rest for 48 seconds.
# Donner can fly 28 km/s for 5 seconds, but then must rest for 134 seconds.
# Dasher can fly 4 km/s for 16 seconds, but then must rest for 55 seconds.
# Blitzen can fly 14 km/s for 3 seconds, but then must rest for 38 seconds.
# Prancer can fly 3 km/s for 21 seconds, but then must rest for 40 seconds.
# Comet can fly 18 km/s for 6 seconds, but then must rest for 103 seconds.
# Vixen can fly 18 km/s for 5 seconds, but then must rest for 84 seconds.


dancer = [27, 27, 27, 27, 27]
cupid = [22, 22]
rudalph = [11, 11, 11, 11, 11]
donner = [28, 28, 28, 28, 28]
dasher = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
blitzen = [14, 14, 14]
prancer = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
comet = [18, 18, 18, 18, 18, 18]
vixen = [18, 18, 18, 18, 18]

dancerD = 0
cupidD = 0
rudalphD = 0
donnerD = 0
dasherD = 0
blitzenD = 0
prancerD = 0
cometD = 0
vixenD = 0

ctr = 0

for x in range(132):
    dancer.append(0)
for x in range(41):
    cupid.append(0)
for x in xrange(48):
    rudalph.append(0)
for x in xrange(134):
    donner.append(0)
for x in xrange(55):
    dasher.append(0)
for x in xrange(38):
    blitzen.append(0)
for x in xrange(40):
    prancer.append(0)
for x in xrange(103):
    comet.append(0)
for x in xrange(84):
    vixen.append(0)

for x in xrange(2503):
    print(dancer[ctr])
    dancerD += dancer[ctr]
    ctr += 1
    if ctr >= len(dancer):
        ctr = 0
ctr = 0
for x in xrange(2503):
    print(cupid[ctr])
    cupidD += cupid[ctr]
    ctr += 1
    if ctr >= len(cupid):
        ctr = 0
ctr = 0
for x in xrange(2503):
    print(rudalph[ctr])
    rudalphD += rudalph[ctr]
    ctr += 1
    if ctr >= len(rudalph):
        ctr = 0
ctr = 0
for x in xrange(2503):
    print(donner[ctr])
    donnerD += donner[ctr]
    ctr += 1
    if ctr >= len(donner):
        ctr = 0
ctr = 0
for x in xrange(2503):
    print(dasher[ctr])
    dasherD += dasher[ctr]
    ctr += 1
    if ctr >= len(dasher):
        ctr = 0
ctr = 0
for x in xrange(2503):
    print(blitzen[ctr])
    blitzenD += blitzen[ctr]
    ctr += 1
    if ctr >= len(blitzen):
        ctr = 0
ctr = 0
for x in xrange(2503):
    print(prancer[ctr])
    prancerD += prancer[ctr]
    ctr += 1
    if ctr >= len(prancer):
        ctr = 0
ctr = 0
for x in xrange(2503):
    print(comet[ctr])
    cometD += comet[ctr]
    ctr += 1
    if ctr >= len(comet):
        ctr = 0
ctr = 0
for x in xrange(2503):
    print(vixen[ctr])
    vixenD += vixen[ctr]
    ctr += 1
    if ctr >= len(vixen):
        ctr = 0

print(dancerD)
print(cupidD)
print(rudalphD)
print(donnerD)
print(dasherD)
print(blitzenD)
print(prancerD)
print(cometD)
print(vixenD)



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

dancerDl = []
cupidDl = []
rudalphDl = []
donnerDl = []
dasherDl = []
blitzenDl = []
prancerDl = []
cometDl = []
vixenDl = []

dancerP = 0
cupidP = 0
rudalphP = 0
donnerP = 0
dasherP = 0
blitzenP = 0
prancerP = 0
cometP = 0
vixenP = 0

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
    #print(dancer[ctr])
    dancerD += dancer[ctr]
    dancerDl.append(dancerD)
    ctr += 1
    if ctr >= len(dancer):
        ctr = 0
ctr = 0
for x in xrange(2503):
    #print(cupid[ctr])
    cupidD += cupid[ctr]
    cupidDl.append(cupidD)
    ctr += 1
    if ctr >= len(cupid):
        ctr = 0
ctr = 0
for x in xrange(2503):
    #print(rudalph[ctr])
    rudalphD += rudalph[ctr]
    rudalphDl.append(rudalphD)
    ctr += 1
    if ctr >= len(rudalph):
        ctr = 0
ctr = 0
for x in xrange(2503):
    #print(donner[ctr])
    donnerD += donner[ctr]
    donnerDl.append(donnerD)
    ctr += 1
    if ctr >= len(donner):
        ctr = 0
ctr = 0
for x in xrange(2503):
    #print(dasher[ctr])
    dasherD += dasher[ctr]
    dasherDl.append(dasherD)
    ctr += 1
    if ctr >= len(dasher):
        ctr = 0
ctr = 0
for x in xrange(2503):
    #print(blitzen[ctr])
    blitzenD += blitzen[ctr]
    blitzenDl.append(blitzenD)
    ctr += 1
    if ctr >= len(blitzen):
        ctr = 0
ctr = 0
for x in xrange(2503):
    #print(prancer[ctr])
    prancerD += prancer[ctr]
    prancerDl.append(prancerD)
    ctr += 1
    if ctr >= len(prancer):
        ctr = 0
ctr = 0
for x in xrange(2503):
    #print(comet[ctr])
    cometD += comet[ctr]
    cometDl.append(cometD)
    ctr += 1
    if ctr >= len(comet):
        ctr = 0
ctr = 0
for x in xrange(2503):
    #print(vixen[ctr])
    vixenD += vixen[ctr]
    vixenDl.append(vixenD)
    ctr += 1
    if ctr >= len(vixen):
        ctr = 0

for x in xrange(2503):
    if dancerDl[x] >= cupidDl[x] and dancerDl[x] >= rudalphDl[x] and dancerDl[x] >= donnerDl[x] and dancerDl[x] >= dasherDl[x] and dancerDl[x] >= blitzenDl[x] and dancerDl[x] >= prancerDl[x] and dancerDl[x] >= cometDl[x] and dancerDl[x] >= vixenDl[x]:
        dancerP += 1
    if cupidDl[x] >= dancerDl[x] and cupidDl[x] >= rudalphDl[x] and cupidDl[x] >= donnerDl[x] and cupidDl[x] >= dasherDl[x] and cupidDl[x] >= blitzenDl[x] and cupidDl[x] >= prancerDl[x] and cupidDl[x] >= cometDl[x] and cupidDl[x] >= vixenDl[x]:
        cupidP += 1
    if rudalphDl[x] >= cupidDl[x] and rudalphDl[x] >= dancerDl[x] and rudalphDl[x] >= donnerDl[x] and rudalphDl[x] >= dasherDl[x] and rudalphDl[x] >= blitzenDl[x] and rudalphDl[x] >= prancerDl[x] and rudalphDl[x] >= cometDl[x] and rudalphDl[x] >= vixenDl[x]:
        rudalphP += 1
    if donnerDl[x] >= cupidDl[x] and donnerDl[x] >= rudalphDl[x] and donnerDl[x] >= dancerDl[x] and donnerDl[x] >= dasherDl[x] and donnerDl[x] >= blitzenDl[x] and donnerDl[x] >= prancerDl[x] and donnerDl[x] >= cometDl[x] and donnerDl[x] >= vixenDl[x]:
        donnerP += 1
    if dasherDl[x] >= cupidDl[x] and dasherDl[x] >= rudalphDl[x] and dasherDl[x] >= donnerDl[x] and dasherDl[x] >= dancerDl[x] and dasherDl[x] >= blitzenDl[x] and dasherDl[x] >= prancerDl[x] and dasherDl[x] >= cometDl[x] and dasherDl[x] >= vixenDl[x]:
        dasherP += 1
    if blitzenDl[x] >= cupidDl[x] and blitzenDl[x] >= rudalphDl[x] and blitzenDl[x] >= donnerDl[x] and blitzenDl[x] >= dasherDl[x] and blitzenDl[x] >= dancerDl[x] and blitzenDl[x] >= prancerDl[x] and blitzenDl[x] >= cometDl[x] and blitzenDl[x] >= vixenDl[x]:
        blitzenP += 1
    if prancerDl[x] >= cupidDl[x] and prancerDl[x] >= rudalphDl[x] and prancerDl[x] >= donnerDl[x] and prancerDl[x] >= dasherDl[x] and prancerDl[x] >= blitzenDl[x] and prancerDl[x] >= dancerDl[x] and prancerDl[x] >= cometDl[x] and prancerDl[x] >= vixenDl[x]:
        prancerP += 1
    if cometDl[x] >= cupidDl[x] and cometDl[x] >= rudalphDl[x] and cometDl[x] >= donnerDl[x] and cometDl[x] >= dasherDl[x] and cometDl[x] >= blitzenDl[x] and cometDl[x] >= prancerDl[x] and cometDl[x] >= dancerDl[x] and cometDl[x] >= vixenDl[x]:
        cometP += 1
    if vixenDl[x] >= cupidDl[x] and vixenDl[x] >= rudalphDl[x] and vixenDl[x] >= donnerDl[x] and vixenDl[x] >= dasherDl[x] and vixenDl[x] >= blitzenDl[x] and vixenDl[x] >= prancerDl[x] and vixenDl[x] >= cometDl[x] and vixenDl[x] >= dancerDl[x]:
        vixenP += 1

print(dancerP)
print(cupidP)
print(rudalphP)
print(donnerP)
print(dasherP)
print(blitzenP)
print(prancerP)
print(cometP)
print(vixenP)



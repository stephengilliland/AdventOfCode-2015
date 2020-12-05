x = 600000
housePresents = 0
while(1):
    x += 1
    housePresents = x*11
    for y in xrange(1, x):
        if x%y == 0:
            housePresents += 11*y
    if housePresents >= 29000000:
        print("House Number =", x)
        print("Presents =", housePresents)
        break
    print(x)
# 800280 too high
# 900120 too high

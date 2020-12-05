from itertools import permutations 

dists = {"AlphaCentauri-Snowdin": 66,
"AlphaCentauri-Tambi": 28,
"AlphaCentauri-Faerun": 60,
"AlphaCentauri-Norrath": 34,
"AlphaCentauri-Straylight": 34,
"AlphaCentauri-Tristram": 3,
"AlphaCentauri-Arbre": 108,
"Snowdin-Tambi": 22,
"Snowdin-Faerun": 12,
"Snowdin-Norrath": 91,
"Snowdin-Straylight": 121,
"Snowdin-Tristram": 111,
"Snowdin-Arbre": 71,
"Tambi-Faerun": 39,
"Tambi-Norrath": 113,
"Tambi-Straylight": 130,
"Tambi-Tristram": 35,
"Tambi-Arbre": 40,
"Faerun-Norrath": 63,
"Faerun-Straylight": 21,
"Faerun-Tristram": 57,
"Faerun-Arbre": 83,
"Norrath-Straylight": 9,
"Norrath-Tristram": 50,
"Norrath-Arbre": 60,
"Straylight-Tristram": 27,
"Straylight-Arbre": 81,
"Tristram-Arbre": 90}

places = ["AlphaCentauri", "Tambi", "Snowdin", "Faerun", "Norrath", "Straylight", "Tristram", "Arbre"]

trips = permutations(places)
currTown = ""
nextTown = ""
currDist = 0
distances = []
road = ""
shortest = 0
roadReverse = ""

for trip in trips:
    for x in xrange(len(trip)-1):
        currTown = trip[x]
        nextTown = trip[x+1]
        road = currTown + '-' + nextTown
        roadReverse = nextTown + '-' + currTown
        if road in dists:
            print("Road =", road)
            currDist += dists[road]
        else:
            print("Road =", road)
            currDist += dists[roadReverse]
    distances.append(currDist)
    currDist = 0

shortest = min(distances)
print(shortest)

    



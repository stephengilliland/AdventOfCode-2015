import md5
import hashlib 

result = ""
print(result)
ending = 0
endingStr = []
  
# initializing string 
#input = ['b','g','v','y','z','d','s','v']
input = ['a', 'b', 'c', 'd', 'e', 'f']
firstHalf = []
ending = []
ctr = 0
datas = []
hashData = ""
answer = []
zeroCtr = 0

while(1):
    firstHalf = ['b', 'g', 'v', 'y', 'z', 'd', 's', 'v']
    ending = list(str(ctr))
    #print(firstHalf)
    firstHalf.extend(ending)
    datas = firstHalf
    print(datas)
    hashData = ''.join(datas)
    result = hashlib.md5(hashData.encode()) 
    result = str(result.hexdigest())
    ctr += 1
    for x in xrange(10):
        if result[x] == '0':
            zeroCtr += 1
        else:
            break
    if zeroCtr >= 6:
        print(zeroCtr)
        print(result)
        break
    print(ctr)
    zeroCtr = 0
    datas = []
    del firstHalf[:]
    ending = []
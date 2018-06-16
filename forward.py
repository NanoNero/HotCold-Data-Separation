
import linecache
import re
import copy
from decimal import Decimal
import timeit


alpha = 0.15
#______________________________________________________________
def calculateNewEstimation(Tuple, otime) :
    t_prev = Tuple[0]
    t = otime
    
    newEst = alpha + Tuple[1] * pow((1 - alpha), (t_prev-t))
    newEst = round(newEst, 7)
    #print 'newEst = '+ str(newEst)
    Tuple2 = (t, newEst, t_prev)
    #print 'Tuple2 = ' + str(Tuple2)
    return Tuple2
#_______________________________________________________________
freq = 0
store = {}
K = 40
start = timeit.default_timer()
#Txt with all the oids accessed
with open('storelog.txt', "r") as f:
    array = f.read().split(' ')

#forward algorithm
for OID in array:
    freq = freq + 1
    if store.has_key(OID):
        Tuple2 = calculateNewEstimation(store[OID], freq)
        store[OID] = Tuple2
    else:
        store[OID] = (freq, 0, freq)
#print 'store'
#print store.items()

hashTable = {}
for OID in store.keys():
    if len(hashTable) < K:
        hashTable[OID] = store[OID][1]
    else:
        est_min = min(hashTable.values())
        if store[OID][1] > est_min:
            for key, value in hashTable.copy().items():  
                if value == est_min:
                    del hashTable[key]                    
            hashTable[OID] = store[OID][1]

print 'hash :'
print hashTable.items()


stop = timeit.default_timer()
print stop-start




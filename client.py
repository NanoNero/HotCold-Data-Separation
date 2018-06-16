import socket
import time
import re
import hotcoldN

HOST = '192.168.233.52'    # The remote host
PORT = 5000          # The same port as used by the server

cachedTriples={}
newAccessTriple={}
TOTAL_ACCESSES = 0
time = 0
records = {}
CACHESIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print ('Connected to server...')

while 1:
    data = s.recv(1024)
    TOTAL_ACCESSES += 1
    time += 1
    tab = re.findall(r'\d+', data)
    tuplex = [for x in tab if int(x) > 1000]
    for oid in tuplex:        
        newAccessTriple={oid:(time,0)}
        accKey = newAccessTriple.keys()[0]
        #time.sleep()
        #print 'Need to run hot-cold algo \n'
        if(len(cachedTriples) < CACHESIZE):
            if accKey not in Records.keys() :
                cachedTriples.update(newAccessTriple)
                records.update(newAccessTriple)
            else:
                cachedTriples[accKey] = calculateNewEstimation(newAccTriple[accKey], t_earliest)
                records[accKey] = calculateNewEstimation(newAccTriple[accKey], t_earliest)

        else:
            hotcoldN.Algo(records,cachedTriples,newAccessTriple)

  
s.close()

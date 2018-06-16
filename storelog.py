#RUN THIS PROGRAM BEFORE RUNNING FORWARD.PY
#RECORD OIDS ARE STORED IN THE FILE STORELOG.TXT
#THIS FILE IS THEN READ BY THE CODE IN THE
#FORWARD ALGORITHM

import re
import psycopg2
from itertools import islice
import linecache


# Database details
hostname = '10.100.71.21' 
username = '201501207's
password = '201501207'
database = '201501207'

#________________________________________________________________________________________

file1 = open('E:/storelog.txt',"w")
  
with open('E:/Weatherlog.txt', "r") as f:
    array = f.read().split(' ')
                            
for QID in array:               
    if QID != '':
        # Read the query at line number lineNum
        with open('WeatherQueries.txt') as f:
            try:                            
                line = next(islice(f, int(QID)-1, int(QID) ))
                            
            except StopIteration:
                print('No lines in file')
                            
    
    myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database )
              
    cur = myConnection.cursor()
    cur.execute(line)
    
    
    #Add OIDs to the storefile 
    for row in cur :
        st = str(row)

        
        tab = re.findall(r'\d+', st)
        tuplex = [x for x in tab if int(x) > 2017]
        
        #write oid into text file
        for oid in tuplex:
            file1.write(str(oid)+ ' ')      
                
    myConnection.close()        
  
file1.close()

print 'Done'


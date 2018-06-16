
import operator
import copy
from decimal import Decimal

cachedTriples = {'2': (21, 2.3),
         '3': (20, 1.3),
         '4': (12, 1.1),
         '10': (27, 2.7),
         '12': (11, 1.4),
         '13': (13, 4.3),
         '14': (16, 4.1),
         '18': (25, 1.45)}
# rid : (time, est)
Records = {'1': (22, 3.3),
       '2': (21, 2.3),
       '3': (20, 1.3),
       '4': (12, 1.1),
       '5': (19, 1.6),
       '6': (18, 1.5),
       '7': (17, 2.5),
       '8': (23, 1.7),
       '9': (24, 2.4),
       '10': (27, 2.7),
       '11': (28, 7.5),
       '12': (11, 1.4),
       '13': (13, 4.3),
       '14': (16, 4.1),
       '15': (35, 2.9),
       '16': (33,3.2),
       '17': (22, 2.0),
       '18': (25, 1.45),
       '19': (26, 2.6),
       '20': (30,3.8)}


copy.deepcopy(cachedTriples)
newAccTriple = {'19': (26, 1.8)}
alpha = 0.05
#__________________________________________________________________________________
def getPartialRecords(t_latest, t_earliest, Records):
    for key, value in Records.copy().items():        
        if value[0] < t_earliest or value[0] > t_latest :
            del Records[key]
      
    return Records


#__________________________________________________________________________________
def calculateNewEstimation(Tuple, t_earliest) :
    t_prev = t_earliest
    t = Tuple[0]
    newEst = alpha + Tuple[1] * pow((1 - alpha), (t_prev-t))
    newEst = round(newEst, 3)
    Tuple2 = (t, newEst)    
    return Tuple2

#__________________________________________________________________________________
def Algo (Records, cachedTriples, newAccTriple) :
    t_latest = max(cachedTriples.iteritems(), key=operator.itemgetter(1))[1][0]
    t_earliest = min(cachedTriples.iteritems(), key=operator.itemgetter(1))[1][0]
    est_max = max(cachedTriples.values(), key=operator.itemgetter(1))[1]
    est_min = min(cachedTriples.values(), key=operator.itemgetter(1))[1]

    accKey = newAccTriple.keys()[0]    
    Records = getPartialRecords(t_latest, t_earliest, Records)
    
    if  accKey in cachedTriples.keys():
        #Update est, last_acc_time in Records
        newAccTriple[accKey] = calculateNewEstimation(newAccTriple[accKey], t_earliest)      

        t_latest = newAccTriple[accKey][0]
        cachedTriples[accKey] = newAccTriple[accKey]
                                                      
        t_earliest = min(cachedTriples.iteritems(), key=operator.itemgetter(1))[1][0]
        #remove from Records the records with last_acc_time less than t_earliest
        for key, value in Records.copy().items():  
            if value[0] < t_earliest:
                del Records[key]
    
    else:
        if accKey in Records.keys() :
                #Update est, last_acc_time in Records
                newAccTriple[accKey] = calculateNewEstimation(newAccTriple[accKey], t_earliest)
                Records[accKey] = newAccTriple[accKey]
                 
                if newAccTriple[accKey][1] >= est_min and newAccTriple[accKey][1] <= est_max :
                     #remove from cachedTriples the records with est_min with minimum last_acc_time
                     
                     for key, value in cachedTriples.copy().items():  
                         if value[1] < est_min:
                             del cachedTriples[key]                
                     #addToCached(newAccTriple)
                     cachedTriples.update(newAccTriple)
                     t_latest = newAccTriple[accKey][0]
                     t_earliest = min(cachedTriples.iteritems(), key=operator.itemgetter(1))[1][0]
                     #remove from Records the records with last_acc_time less than t_earliest
                     
                     for key, value in Records.copy().items():  
                         if value[0] < t_earliest:
                            del Records[key]
        else:
            # addToRecords(newAccTriple)
            Records.update(newAccTriple)
    print 'Cached Triples: \n'
    print cachedTriples.items()
    print 'Records : \n'
    print Records.items()
#__________________________________________________________________________________

print 'hi'
Algo (Records, cachedTriples, newAccTriple)
print 'done'

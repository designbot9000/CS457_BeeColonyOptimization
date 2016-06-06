from ListGen import *
from ScoutBee import *
from EliteBee import *
from WorkerBee import *


import time
import random

'''

'''

classListPermutations = 10

scouts = None
elites = None 
workers = None

populationSize=100
optimumFitness=0.0
limit=0
MAX_LIMIT=100
count=0

#generate pop of classListPermutations
classList=ListGen(classListPermutations)
classList.run()

elitePopulation=0
eliteRatio=0
scoutPopulation=0
scoutRatio=0
workerPopulation=0
workerRatio=0

while (optimumFitness != 1.0) and (limit<MAX_LIMIT):
    chance=random.random()
    
    if count==0 :
        #first iteration has 100%scouts to find schedules
        scoutRatio = 1.0
        eliteRatio = 0.0
        workerRatio = 0.0
    else:
        #generate normal ratios
        scoutRatio = populationSize/scout_schedules.qsize()
        remaining = 1.0-scoutRatio
        eliteRatio = (1-optimumFitness)*remaining
        
    
    scoutPopulation = round(populationSize*scoutRatio)
    elitePopulation = round(populationSize*eliteRatio)
    workerPopulation = 100 - scoutPopulation - elitePopulation
    
    scouts=ScoutBee(scoutPopulation)
    scouts.run()
    elites=EliteBee(elitePopulation)
    workers=WorkerBee(workerPopulation)
    limit += 1
    
    

    
    
print scout_schedules.qsize()
top_sched =  scout_schedules.get(False)
sched  = top_sched.get_schedule()
for item in sched:
    print item



#TODO - generate world (lists)

#TODO - generate initial bee pop

#TODO - run sim
    
# while True:
#     print scout_schedules.qsize()
#     if scout_schedules.qsize() == 0:
#         break
#     output_schedule = scout_schedules.get()
#     for session in output_schedule.get_sessions():
#         print session
#     print "\n\n"


print "Exiting main thread!", time.ctime()

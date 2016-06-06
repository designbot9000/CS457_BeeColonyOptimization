from ListGen import *
from ScoutBee import *
from EliteBee import *
from WorkerBee import *


import time
import random

'''

'''

classList_permutations = 50

scouts = None
elites = None 
workers = None

population_size=100
optimum_fitness=0.0
limit=0
MAX_LIMIT=100
count=0

#generate pop of classListPermutations
classList=ListGen(classList_permutations)
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
        
    
    scoutPopulation = round(population_size*scoutRatio)
    elitePopulation = round(population_size*eliteRatio)
    workerPopulation = 100 - scoutPopulation - elitePopulation
    
    scouts=ScoutBee()
    scouts.run(scoutPopulation)
    elites=EliteBee()
    elites.run(elitePopulation)
    workers=WorkerBee()
    workers.run(workerPopulation, optimum_fitness)
    limit += 1
    
    

    
    
print scout_schedules.qsize()
print "..."
loop = 10
while loop > 0:
    
    
    if scout_schedules.qsize() > 0:
        top_sched = scout_schedules.get(False)
        sched  = top_sched.get_schedule()
        print "fitness: {}".format(top_sched.fitness)
        credit = top_sched.creditsFulfilled
        if credit >= 106:            
            print "scheduled credits: {}".format(credit)
            
            for item in sched:
                print item
            loop -= 1
    else:
        break



#TODO - generate world (lists)

#TODO - generate initial bee pop

#TODO - run sim
    



#print "Exiting main thread!", time.ctime()

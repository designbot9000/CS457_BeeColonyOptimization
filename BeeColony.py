from ListGen import *
from ScoutBee import *
from EliteBee import *
from WorkerBee import *


import time
import random

'''

'''


classList_permutations = 1000

scouts = None
elites = None 
workers = None

population_size=100
optimum_fitness=0.0
optimum_schedule=None
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

while (optimum_fitness != 1.0) and (limit<MAX_LIMIT):
    chance=random.random()
    
    if count==0 :
        #first iteration has 100%scouts to find schedules
        scoutRatio = 1.0
        eliteRatio = 0.0
        workerRatio = 0.0
    else:
        #generate normal ratios
        scoutRatio = (population_size + 0.0)/(scout_schedules.qsize() + 0.0)
        remaining = 1.0-scoutRatio
        eliteRatio = (1-optimum_fitness)*remaining
        #pass
        
        
    
    scoutPopulation = round(population_size*scoutRatio)
    elitePopulation = round(population_size*eliteRatio)
    workerPopulation = population_size - scoutPopulation - elitePopulation
    print "Scout: {} Elite: {} Worker {}".format(scoutPopulation,elitePopulation,workerPopulation)
    
    scouts=ScoutBee()
    scouts.run(scoutPopulation)
    elites=EliteBee()
    elites.run(elitePopulation)
    workers=WorkerBee()
    workers.run(workerPopulation, optimum_fitness)
    limit += 1
    print scout_schedules.qsize()
    print "..."
    loop = 100
    scheduleQueue=Queue.Queue()
    while scout_schedules.qsize() > 0:   
        if scout_schedules.qsize() > 0:
            top_sched = scout_schedules.get(False)
            #scout_schedules.put(top_sched)
            scheduleQueue.put(top_sched)
            #print "fitness: {}".format(top_sched.fitness)
            credit = top_sched.creditsFulfilled
        
            if credit >= 10:            
                #print "fitness:"+str(top_sched.fitness)
                if(top_sched.fitness>=optimum_fitness):
                    optimum_fitness=top_sched.fitness
                    optimum_schedule=top_sched
                    for item in top_sched.get_schedule():
                        #print item
                        pass
                    loop -= 1
        
            #print "scheduled credits: {}".format(credit)
            #for item in sched:
               # print item
            loop -= 1
        else:
            break
    print scout_schedules.qsize()
    while scheduleQueue.qsize()>0:
        scout_schedules.put(scheduleQueue.get(False))
    
    count +=1
    
    


print "optimum_schedule"
print optimum_schedule.fitness
for item in optimum_schedule.get_schedule():
        print item

#TODO - generate world (lists)

#TODO - generate initial bee pop

#TODO - run sim
    



#print "Exiting main thread!", time.ctime()

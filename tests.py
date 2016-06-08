# -*- coding: utf-8 -*-
"""
Created on Sun Jun 05 14:37:26 2016

@author: jhamm
"""
from ListGen import *
from ScoutBee import *
from EliteBee import *
from WorkerBee import *
from Course import *



#generate pop of classListPermutations
classList=ListGen(100)
classList.run()

print list_schedules.get(False)
sessions = list_schedules.get(False)
print ""
#for item in sessions:
 #   print item
  #  sess = item.get_sessions()
   # for item in sess:
    #    print item
     #   print item.get_quarter()

bees=ScoutBee() 
bees.run(50)
i=0  
while i<5:
    item=scout_schedules.queue[i]
    item.check_fitness(4,3,2,1)
    print item.fitness
    i+=1
print scout_schedules.qsize()

elite=EliteBee() 
elite.run(30)



worker=WorkerBee()
worker.run(30,elite_schedules[0].fitness)
i=0

while i<5:
    item=scout_schedules.queue[i]
    item.check_fitness(4,3,2,1)
    print item.fitness
    i+=1
print scout_schedules.qsize()

for sessions in scout_schedules.queue[0].get_schedule():
    print sessions
print scout_schedules.queue[0].creditsFulfilled

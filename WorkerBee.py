# -*- coding: utf-8 -*-
"""
Created on Sat Jun 04 15:34:10 2016

@author: jhamm
"""

'''
Work Bee's follow the Elite bee's decision and try to optimize the schedule. 
'''

from ScoutBee import *
from EliteBee import *
import random
import Queue
'''
Worker Bee takes a schedule, and swaps out schedule sessions in attempt to 
improve fitness
'''
# selects an Elite Bee from the Population to modify a schedule that it holds

#randomness constant, allows bees to choose randomly, within a certain range
class WorkerBee():
    def __init__(self):
        self.iterations = 0

    def run(self, iterations, optimum_fitness):
        global elite_schedules
        self.iterations = iterations
        selection_size=round(len(elite_schedules)*(1-optimum_fitness),0)

        #while there are still Worker Bees in the Population
        while self.iterations > 0:
            #Randomly select Elite bee based on proportional score
            if(selection_size==0):
                break
            else:
                index=random.randint(0,selection_size-1)
                schedule=elite_schedules[index]        
                #optimize the schedule
                optimum_schedule=optimize_schedule(schedule)
                #place in ready queue for elites to pull from
                optimum_schedule.check_fitness(4,2,1)
                scout_schedules.append(optimum_schedule)
                self.iterations-=1
    
    def optimize_schedule(schedule):
        global optimum_fitness
        attempts=0
        for course in schedule:
                if(attempts<MAX_ATTEMPTS):
                    schedule.sort()
                    if(random.random()>0.5):
                        session_options=course.get_sessions()
                        schedule.drop_session(course)
                        #choose random session from available sessions
                        randIndex=random.randint(0,len(session_options))
                        new_course=session_options[randIndex]
                        meets_prereqs=schedule.add_session(new_course)
                        if(meets_prereqs==False):
                            schedule.drop_session(new_course)
                            schedule.add_session(course)
                            optimize_schedule(schedule)
                else:
                    break              
                        
        return schedule

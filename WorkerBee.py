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
                
                #generate a schedule
                MAX_ATTEMPTS=5
                optimum_schedule=self.optimize_schedule(schedule,MAX_ATTEMPTS)
                #place in ready queue for elites to pull from
                optimum_schedule.check_fitness(prof_weight, time_to_complete_weight, avg_credits_per_q_weight)
                if optimum_schedule.creditsFulfilled >= 106:
                    '''
                    for course in optimum_schedule.get_schedule():
                        print course
                    '''
                    optimum_schedule.modified_by = "worker"
                    
                    if optimum_schedule.fitness>optimum_fitness:
                        scout_schedules.put(optimum_schedule)
                    else:
                         scout_schedules.put(schedule)
                         scout_schedules.put(optimum_schedule)
                else:
                    scout_schedules.put(schedule) 
                    
                    
               
                self.iterations-=1
    
    def optimize_schedule(self,schedule,attempts):
        global optimum_fitness
        for classItem in schedule.get_schedule():
                if(attempts>=0):
                                     
                    if(random.random()>0.5):                        
                        session_options=classItem.course.get_sessions()                        
                        
                        #choose random session from available sessions *** note this needs to switch with a session of the same quarter
                        s_min = -1
                        s_max = -1
                        index = 0
                        while index < len(session_options):
                            if session_options[index].quarter == classItem.quarter and s_min != -1:
                                s_min, s_max = index
                            elif session_options[index].quarter == classItem.quarter:
                                s_max = index
                            index += 1
                        if s_min > -1 and s_max > -1:
                            schedule.drop_session(classItem)
                            randIndex=random.randint(s_min,s_max)
                            new_class=session_options[randIndex]
                            meets_prereqs=schedule.add_session(new_class)
                            '''
                            if(meets_prereqs==False):
                                schedule.add_session(classItem)
                                self.optimize_schedule(schedule,attempts-1)
                                '''
                        else:
                            break
                else:
                    break              
                        
        return schedule

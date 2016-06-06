from Schedule import *
import random
import Queue
'''
Elite Bee's job is to pick, at random, a schedule that the scouts "find"
'''

elite_schedules = list()

class EliteBee():
    
    def __init__(self, iterations):
        self.iterations = iterations

    def run(self):
        global scout_schedules
        #while there are still Elite Bees in the Population
        while self.iterations > 0:
            #check the total amount of credits taken
            selected_schedule=scout_schedules.get(False)
            selected_schedule.check_fitness()            
            insert_schedule(selected_schedule);
            self.iterations -= 1
    
    def insert_schedule(self,schedule):
        #checks if selected schedule is higher fitness than the next schedule, and inserts it
        global elite_schedules
        index=0
        for item in elite_schedules:
            if(schedule.fitness<item.fitness):
                index+=1
            else:
                insert(index,self.elite_schedule)
    
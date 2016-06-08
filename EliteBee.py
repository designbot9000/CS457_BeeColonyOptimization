from Schedule import *
from ScoutBee import *
import random
import Queue
'''
Elite Bee's job is to pick, at random, a schedule that the scouts "find"
'''

elite_schedules= list()

class EliteBee():
    
    def __init__(self):
        self.iterations = 0
        self.elite_schedules=[]

    def run(self, iterations):
        global scout_schedules
        self.iterations = iterations
        #while there are still Elite Bees in the Population
        while self.iterations > 0:
            #check the total amount of credits taken
            selected_schedule=scout_schedules.get(False)
                       
            # self.insert_schedule(selected_schedule);
            elite_schedules.append(selected_schedule)
            self.iterations -= 1
    

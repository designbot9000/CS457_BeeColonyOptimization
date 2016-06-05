

import Queue
from collections import deque
import time
import random
'''
Scout bee generates schedule (a possible solution) from randomly chosen lists  
'''
scout_schedules = Queue.PriorityQueue()
MAX_SCOUT_ATTEMPTS = 3000


class ScoutBee():
    def __init__(self, iterations):
        self.iterations = iterations

    def run(self):
        time.sleep(0.5)
        while True:
            #check if list is empty; true = do nothing, or prompt ListGenerator to make new List
            if list_schedules.empty():
                break
            #grab a schedule from the list queue
            designated_schedule = deque(list_schedules.get())
            #create a new schedule based off of class list
            new_schedule = Schedule(2016, 1)
            attempts = 0
            #check if schedule is valid, and if it wont validate after MAX times, give up            
            while (attempts < MAX_SCOUT_ATTEMPTS) & (len(designated_schedule) > 0):
                #select course to check  prereqs
                course_to_evaluate = designated_schedule.pop()
                if new_schedule.check_prereqs(course_to_evaluate) == 0:
                    new_schedule.add_session(course_to_evaluate.get_sessions()[0])
                else:
                    designated_schedule.appendleft(course_to_evaluate)
                attempts += 1

            #sort new schedule based on time taken
            new_schedule.sort()
            #add to Schedule queue
            scout_schedules.put(new_schedule)


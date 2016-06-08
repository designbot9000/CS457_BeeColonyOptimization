
from Schedule import *
from ListGen import *
import Queue
from collections import deque
import time
import random
'''
Scout bee generates schedule (a possible solution) from randomly chosen lists  
'''
scout_schedules = Queue.PriorityQueue()
MAX_SCOUT_ATTEMPTS = 3000 

prof_weight = 9
time_to_complete_weight = 1
avg_credits_per_q_weight = 6

class ScoutBee():
    def __init__(self):
        self.iterations = 0

    def run(self, iterations):
        #time.sleep(0.5)
        self.iterations = iterations
        global list_schedules
        
        while iterations > 0:
            #time.sleep(20)
            #check if list is empty; true = do nothing, or prompt ListGenerator to make new List
            if list_schedules.empty():
                break
            #grab a course list from the list queue
            sched = list_schedules.get()
            designated_schedule = deque(sched)
            #print "starting schedule generation on list:"
            msg = ""
            '''
            for item in sched:
                print item
            '''
            #print msg
            #create a new schedule based off of class list
            new_schedule = Schedule(2016, 1)
            attempts = 0
            #check if schedule is valid, and if it wont validate after MAX times, give up            
            while (attempts < MAX_SCOUT_ATTEMPTS) & (len(designated_schedule) > 0):
                
                #select course to check  prereqs
                course_to_evaluate = designated_schedule.pop()
                #only adding the 1st inputted session regardless of being the right quarter
                i = 0
                pre_unmet = new_schedule.check_prereqs(course_to_evaluate)
                #flag to make sure we have a successful insert
                success = False
                while (pre_unmet == 0 and i < len(course_to_evaluate.get_sessions())):
                    #print "trying {}".format(course_to_evaluate.get_sessions()[i])
                    response = new_schedule.add_session(course_to_evaluate.get_sessions()[i])
                    if response == True:
                        success = True
                        break
                    else:
                        i += 1  
                if success == False:                        
                    designated_schedule.appendleft(course_to_evaluate)
                attempts += 1
                #time.sleep(5)
            '''
            #print "adding new sched to list"
            #set the fitness for the sched
            new_schedule.check_fitness(4, 2, 1)  
            #sort new schedule based on time taken
            new_schedule.sort()
            #add to Schedule queue
            scout_schedules.put(new_schedule)
            '''            
            #print "new sched len : {} courses left {}".format(len(new_schedule.schedule), len(designated_schedule))
            if new_schedule.creditsFulfilled >= 106:
                print "adding new sched to list"
                #set the fitness for the sched
                new_schedule.check_fitness(prof_weight, time_to_complete_weight, avg_credits_per_q_weight)  
                new_schedule.modified_by = "scout"
                #sort new schedule based on time taken
                new_schedule.sort()
                '''
                s = new_schedule.schedule
                for item in s:
                    print item
                    '''
                #add to Schedule queue
                scout_schedules.put(new_schedule)
            else:
                pass #print "sched not enough credits {}".format(new_schedule.creditsFulfilled)
                
            iterations -= 1


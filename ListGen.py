from Schedule import *

import random
import Queue
'''
effectively "the world" or nature. World generates possible lists of classes (aka. sources of food).
'''

list_schedules = Queue.Queue()

class ListGen():
    #ListGen(<num of itr>)
    def __init__(self, iterations):
        
        self.iterations = iterations

    def run(self):
        while self.iterations > 0:
            #defines a list of courses starting with required courses
            selected_courses = list(Course.requiredCourses)
            #defines a list of elective courses
            electives_available = list(Course.electiveCourses)
            ##of credits
            credit_count = 0
            
            #sum of credits of selected courses(required courses)
            for course in selected_courses:
                credit_count += course.credits

            #loop until enough electives have been added
            while credit_count < REQUIRED_CREDITS:
                #shuffle the electives so they're pulled at random
                random.shuffle(electives_available)
                #pop the top elective off the shuffled list
                selected_elective_course = electives_available.pop()
                #update the credit count
                credit_count += selected_elective_course.credits
                #add the course to the list
                selected_courses.append(selected_elective_course)
            #add the newly generated list to the queue
            list_schedules.put(selected_courses)
            
            self.iterations -= 1

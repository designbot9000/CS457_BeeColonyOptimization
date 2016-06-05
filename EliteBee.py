from Schedule import *
import random
import Queue
'''
Elite Bee's job is to pick, at random, a schedule that the scouts "find"
'''

elite_schedules = Queue.Queue()

class EliteBee():
    def __init__(self, iterations):
        self.iterations = iterations

    def run(self):
        #while there are still Elite Bees in the Population
        while self.iterations > 0:
            #check the total amount of credits taken
            selected_courses = list(Course.requiredCourses)
            electives_available = list(Course.electiveCourses)
            credit_count = 0

            for course in selected_courses:
                credit_count += course.credits

            
            while credit_count < REQUIRED_CREDITS:
                random.shuffle(electives_available)
                selected_elective_course = electives_available.pop()
                credit_count += selected_elective_course.credits
                selected_courses.append(selected_elective_course)

            elite_schedules.put(selected_courses)
            self.iterations -= 1

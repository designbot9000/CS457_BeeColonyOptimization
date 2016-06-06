from Course import *

REQUIRED_CREDITS = 106

class Schedule:
    def __init__(self, startYear, startQuarter):
        self.startYear = startYear
        self.startQuarter = startQuarter
        self.maxCreditsPerQuarter = 18
        self.maxQuarters = 9
        self.quarter = 1
        self.fitness = 0
        self.schedule = list()

    def check_fitness(self, weightProfessor, weightCourse, weightCompletion, weightCredit):
        """Check the fitness of the current configuration

        Args:
            weightProfessor (int): How important is the professor rating
            weightCourse (int): How important is the class's rating
            weightCompletion (int): How important is finishing faster
            weightCredit (int): How important is having a low credit load

        Returns:
            int: returns an int with higher numbers representing a higher satisfaction
            based on the provided weights.
        """
        return 0

    def check_prereqs(self, course):
        #checks to see if course has a prereq
        if course.prereq_codes is None:
            return 0
        #get the prereqs
        prereqs_unmet = len(course.prereq_codes)
        for prereq in course.prereq_codes:
            for session in self.schedule:
                if session.course == prereq:
                    prereqs_unmet -= 1
                    break
        return prereqs_unmet
    
    def get_quarter(self):
        return self.quarter

    def add_session(self, session):
        print "trying to add {}".format(session)
        print session.course.credits
        sessions = self.get_sessions(self.quarter)
        print sessions[0].course.credits
        creds = 0
        for item in sessions:
            creds += item.course.credits
        print creds
        if  (self.maxCreditsPerQuarter - creds) <= session.course.credits:
            self.schedule.append(session)
            return True
        else:
            return False

    def drop_session(self, session):
        self.schedule.remove(session)

    def get_sessions(self, quarter=None):
        output = list()
        if quarter is not None:
            for session in self.schedule:
                if session.get_quarter() == quarter:
                    output.append(session)
        else:
            output = self.schedule
        return output

    def sort(self):
        self.schedule.sort(key=lambda x: x.quarter, reverse=False)

    def swap_course(self, course_one, course_two):
        return 0
        
    def get_schedule(self):
        return self.schedule


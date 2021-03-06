from Course import *
import time

REQUIRED_CREDITS = 106

class Schedule:
    def __init__(self, startYear, startQuarter):
        self.startYear = startYear
        self.startQuarter = startQuarter
        self.maxCreditsPerQuarter = 18
        self.maxQuarters = 9
        self.quarter = 1
        self.creditsFulfilled = 0
        self.fitness = 0
        self.schedule = list()
        self.modified_by = None
    def __lt__( self, other):
        return self.fitness > other.fitness

    def check_fitness(self, weightProfessor, weightCompletion, weightCredit):
        """Check the fitness of the current configuration

        Args:
            weightProfessor (int): How important is the professor rating
            weightCompletion (int): How important is finishing faster
            weightCredit (int): How important is having a low credit load

        Returns:
            int: returns an int with higher numbers representing a higher satisfaction
            based on the provided weights.
        """
        if len(self.schedule) > 0:
            weightProfessor = weightProfessor + 0.0
            weightCompletion = weightCompletion + 0.0
            weightCredit = weightCredit + 0.0
            total_score = 0
            weight = weightProfessor + weightCompletion + weightCredit
            complete_ = 0
            prof_ = 0
            credit_ = 0
        
            for item in self.schedule:
                prof_ += item.get_professor().get_rating()
                if item.get_quarter() > self.quarter:
                    self.quarter = item.get_quarter()
                
            complete_ = (7 / (self.quarter + 0.0)) 
        
            prof_ = ((prof_/len(self.schedule))/5.0 ) 
        
            credit_ = (1/(((self.creditsFulfilled + 0.0) / (self.quarter + 0.0)) * 11.7777777777)) 

            prof_ = prof_ * (weightProfessor/weight)
            complete_ = complete_ * (weightCompletion/weight)
            credit_ = credit_ * (weightCredit/weight)
        
            total_score = prof_ + credit_ + complete_
            #print "total_score"
            self.fitness = total_score#/1000
            return total_score
        else:
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
        
    def check_prereqs_bool(self, course, quarter):
        #checks to see if course has a prereq
        #print "checking {} for quarter {}".format(course.code, quarter)
        if course.prereq_codes is None:
            #print "good to go"
            return True
        #get the prereqs
        prereqs_unmet = len(course.prereq_codes)
        #print "#of prereqs {}".format(prereqs_unmet)
        #get every prereq code
        for prereq in course.prereq_codes:
            #get every session in the schedule
            for session in self.schedule:
                #check if the schedule has the prereq and if the prereq comes before the quarter being looked at
                #print "checking if {} == {} , and session q {} < q {}".format(session.course, prereq, session.quarter, quarter)
                if session.course == prereq and session.quarter < quarter:
                    prereqs_unmet -= 1
                    break
        #print "#of prereqs {}".format(prereqs_unmet)
        if prereqs_unmet > 0:
            #print "try again"
            return False
        else:
            #print "good to go"
            return True
    
    def get_quarter(self):
        return self.quarter

    def add_session(self, session):
        #time.sleep(1)
        #start at quarter 1
        quarter = session.quarter
        
        #current quarter's credits
        '''
        while quarter <= self.maxQuarters:
            #print "checking quarter {} for session {} q {}".format(quarter, session, session.quarter)
            creds = 0
            #getall the session in a given quarter
            sessions = self.get_sessions(quarter)
            #print "existing sessions {}".format(len(sessions))
            #check if there are any sessions for said quarter. if there are, count the credits
            if len(sessions) > 0:
                for item in sessions:
                    creds += item.course.credits
            #print "credits {}".format(creds)
            #check to see if quarter has room for a session left
            #also check to make sure the session being added is at the current quarter or later
            if  (self.maxCreditsPerQuarter - creds) >= session.course.credits and session.get_quarter() >= quarter:
                #print "entering 1st check"
                #now check if prereqs are fulfilled for the quarter being checked
                if self.check_prereqs_bool(session.course, quarter):
                    #print "passed 2nd check, adding course"
                    #add to total credits fulfilled
                    self.creditsFulfilled += session.course.credits
                    #add session to schedule
                    self.schedule.append(session)
                    return True
                #print "failed 1st check"
            #if self.maxCreditsPerQuarter - creds < 4:
           #     pass                
            quarter += 1
            '''
            #print "checking quarter {} for session {} q {}".format(quarter, session, session.quarter)
        creds = 0
        #getall the session in a given quarter
        sessions = self.get_sessions(quarter)
        #print "existing sessions {}".format(len(sessions))
        #check if there are any sessions for said quarter. if there are, count the credits
        if len(sessions) > 0:
            for item in sessions:
                creds += item.course.credits
        #print "credits {}".format(creds)
        #check to see if quarter has room for a session left
        #also check to make sure the session being added is at the current quarter or later
        if  (self.maxCreditsPerQuarter - creds) >= session.course.credits and session.get_quarter() >= quarter:
            #print "entering 1st check"
            #now check if prereqs are fulfilled for the quarter being checked
            if self.check_prereqs_bool(session.course, quarter):
                #print "passed 2nd check, adding course"
                #add to total credits fulfilled
                self.creditsFulfilled += session.course.credits
                #add session to schedule
                self.schedule.append(session)
                return True
        return False

    def drop_session(self, session):
        print "credits before drop {}".format(self.creditsFulfilled)
        self.creditsFulfilled -= session.course.credits
        print "credits after drop {}".format(self.creditsFulfilled)
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
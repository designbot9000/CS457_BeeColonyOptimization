# -*- coding: utf-8 -*-
"""
Created on Sat Jun 04 15:34:10 2016

@author: jhamm
"""

'''
Work Bee's follow the Elite bee's decision and try to optimize the schedule. 
'''



import random
import Queue
'''
Elite Bee's job is to pick, at random, a schedule that the scouts "find"
'''
# selects an Elite Bee from the Population to modify a schedule that it holds

class WorkerBee():
    def __init__(self, iterations):
        
        self.iterations = iterations

    def run(self):
        #while there are still Worker Bees in the Population
        while self.iterations > 0:
            #Randomly select Elite bee based on proportional score
            #Pull a schedule from Elite Bee
            #Swap Sessions in a schedule with other sessions in that course
            #Validate if the schedule works
            #place in ready queue for elites to pull from
            pass
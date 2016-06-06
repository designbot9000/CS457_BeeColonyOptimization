# -*- coding: utf-8 -*-
"""
Created on Sun Jun 05 14:37:26 2016

@author: jhamm
"""
from ListGen import *



#generate pop of classListPermutations
classList=ListGen(10)
classList.run()

print list_schedules.get(False)
sessions = list_schedules.get(False)
print ""
for item in sessions:
    print item
    sess = item.get_sessions()
    for item in sess:
        print item
        print item.get_quarter()






# -*- coding: utf-8 -*-
#ffc - functions for classes
import random

#for classes to choose a random item form list and remove it(to avoid repeatition)
def chooseFromList(li):
        rand = random.randint(0, len(li) - 1)
        
        returnValue = li[rand]
        li.remove(li[rand])
        return returnValue
    
#for classes to choose a random item for a list(without removal)
def chooseFromListDR(li):
        rand = random.randint(0, len(li) - 1)
        return li[rand]


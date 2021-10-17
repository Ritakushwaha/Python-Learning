# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 13:46:15 2021

@author: rikushwa
"""

'''
Exercise 10: Generate a random date between given start and end dates
'''
import random
import time

def getRandomDate(startDate, endDate ):
    print("Printing random date between", startDate, " and ", endDate)
    randomGenerator = random.random()
    dateFormat = '%d/%m/%Y'

    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))

    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate

print ("Random Date = ", getRandomDate("1/1/2021", "13/10/2021"))

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 16:42:57 2019

@author: muham
"""

import datetime

first = datetime.datetime.now()

input ("Press a button to continue")


second = datetime.datetime.now()

print ("First time was ", first)
print ("Second time was ",  second)

difference = second - first

print ("Difference is ",  difference)

print(first.second)
print(second.second)

 #Need to add value to counter for corresponding second of the day.
 
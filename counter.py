# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 19:42:08 2020

@author: muham
"""

import datetime

class counter(object):
        
    #These are variables to save the start time and end time of a time wasting session
    startTime = 0
    endTime = 0
    
    def saveSession(self): #this function saves the startTime and endTime to a text file.
        x = open(str(self.startTime.year)+"-"+str(self.startTime.month)+"-"+str(self.startTime.day)+".txt", "a+")
        x.write("start time: " + str(self.startTime) + "\n")
        x.write("end time: " + str(self.endTime) +"\n")
        x.close()
        
    def recordTimeWasted(self): #this function records the time wasted and will save it to a text file
        input("Press enter to start session")
       
        #this marks the beginning of the procrastination session
        self.startTime = datetime.datetime.now() 
        
        input ("Press enter to end session") #just press enter on the keyboard when the procrastination session is over
       
        #this marks the ending of the procrastination session
        self.endTime = datetime.datetime.now()
        
        self.saveSession()
        
    
    def printTime(self): #this prints the most recently saved startTime and endTime variables
        print(self.startTime)
        print(self.endTime)
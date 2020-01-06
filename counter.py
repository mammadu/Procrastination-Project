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
        with open(str(self.startTime.year)+"-"+str(self.startTime.month)+"-"+str(self.startTime.day)+".txt", "a+") as x:
            x.write("start time: " + str(self.startTime) + "\n")
            x.write("end time: " + str(self.endTime))

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
        
    def sessionInfo(self): # this function will show the periods of time wasted and show the total time wasted for the user inputted date
        year = input("enter year \n")
        month = input("enter month \n")
        day = input("enter day \n")
        
        try:
            with open(str(year) + "-" + str(month) + "-" + str(day) + ".txt", 'r') as x:
                print("\nfile opened") #use this line for debugging purposes
                data = x.readlines()
                formattedData = []
                
                for i in range(0,len(data)):
                    formattedData.append(data[i].split(': '))
                    formattedData[i][1] = formattedData[i][1][:-2]
                    
                for i in range(0,len(data),2):
                    print("\nTime waste session:", i/2+1)
                    print(formattedData[i][0] + ": " + formattedData[i][1])
                    print(formattedData[i+1][0] + ": " + formattedData[i+1][1])

        except FileNotFoundError:
            print("file was not found")


#i need to add a way to show the total time wasted in the sessionInfo section
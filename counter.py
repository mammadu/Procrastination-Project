# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 19:42:08 2020

@author: muham
"""

import datetime
import pandas as pd
import csv

class counter(object):
        
    #These are variables to save the start time and end time of a time wasting session
    startTime = 0
    endTime = 0
    sessionTimes = {'start':[] ,'end':[]}

    def saveSession(self): #this function saves the startTime and endTime to a text file.
        # with open(str(self.startTime.year)+"-"+str(self.startTime.month)+"-"+str(self.startTime.day)+".txt", "a+") as x:
        #     x.write("start time: " + str(self.startTime) + "\n")
        #     x.write("end time: " + str(self.endTime) + "\n")
        self.sessionTimes['start'].append(self.startTime) #adding start time to sessionTimes dictionary
        self.sessionTimes['end'].append(self.endTime) #adding end time to sessionTimes dictionary
        df = pd.DataFrame(self.sessionTimes) #creating dataframe from sessionTimes
        data = df.iloc[-1:,0:] #this stores stores the last added value of the dataframe df
        with open(str(self.startTime.year)+"-"+str(self.startTime.month)+"-"+str(self.startTime.day)+".csv",  mode ='a+') as csv:
            data.to_csv(csv, mode ='a', header=csv.tell()==0, line_terminator = "\n") #Here we insert the data dataframe into the csv file

    def recordTimeWasted(self): #this function records the time wasted and will save it to a text file
        input("Press enter to start session")
       
        #this marks the beginning of the procrastination session
        self.startTime = datetime.datetime.now()
        
        input ("Press enter to end session") #just press enter on the keyboard when the procrastination session is over
       
        #this marks the ending of the procrastination session
        self.endTime = datetime.datetime.now()
        
        self.saveSession()
        
    
    def printTime(self): #this prints the most recently saved startTime and endTime variables
        print('start time is ', self.startTime)
        print('end time is ', self.endTime)
        
    def sessionInfo(self): # this function will show the periods of time wasted and show the total time wasted for the user inputted date
       
        #first it prompts the user for a year, month, and day to find a text file
        year = input("enter year \n")
        month = input("enter month \n")
        day = input("enter day \n")
        self.timeWastedOnDay(year,month,day)
        

    def timeWastedOnDay(self, year, month, day):
        try:
            with open(str(year) + "-" + str(month) + "-" + str(day) + ".csv", 'r') as x: #this opens the file for the day specified
                print("\nfile opened") #use this line for debugging purposes
                data = x.readlines() #this stores the information on the text file in a list. Each element is a line of the text file.
                formattedData = [] #this empty list will store the information in data in a nested list
                totalTimeWasted = []
                
                for i in range(0,len(data)):
                    formattedData.append(data[i].split(',')) #this separates each line into the index, start time, and end time.
                    formattedData[i][2] = formattedData[i][2][:-2] #This removes the newline character (\n) in each line.
                    
                for i in range(1,len(data)): #this loop shows the time waste session number, the start time, and the end time.
                    print("\nTime waste session:", i)
                    print("start: " + formattedData[i][1])
                    print("end :" + formattedData[i][2])
                    
                    starts = datetime.datetime.strptime(formattedData[i][1], '%Y-%m-%d %H:%M:%S.%f')
                    ends = datetime.datetime.strptime(formattedData[i][2], '%Y-%m-%d %H:%M:%S.%f')
                    timeWasted = ends - starts
                    totalTimeWasted.append(timeWasted)
                    print("Time wasted this session: ", timeWasted)
                
                print("\nYour total time wasted is ", sum(totalTimeWasted, datetime.timedelta(0,0)))

        except FileNotFoundError: #this is just in case the date the user entered doesn't have data.
            print("file was not found")


#2020-3-9 todo
#complete option 3
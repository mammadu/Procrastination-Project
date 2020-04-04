# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 19:42:08 2020

@author: muham
"""

import datetime
import pandas as pd
from dateutil.rrule import rrule, DAILY

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
        self.startTime = datetime.datetime.now() #this marks the beginning of the procrastination session
        input ("Press enter to end session") #just press enter on the keyboard when the procrastination session is over
        self.endTime = datetime.datetime.now()#this marks the ending of the procrastination session
        self.saveSession()
        
    
    def printTime(self): #this prints the most recently saved startTime and endTime variables
        print('start time is ', self.startTime)
        print('end time is ', self.endTime)

        

    def getDate(self): #this function creates a tuple of the date from the user input
        year = input("enter year \n")
        month = input("enter month \n")
        day = input("enter day \n")
        
        return int(year), int(month), int(day)

    def formatData(self, year, month, day): #This function opens and formats save data for later use.
        try:
            with open(str(year) + "-" + str(month) + "-" + str(day) + ".csv", 'r') as x: #this opens the file for the day specified
                    #use the next line for debugging purposes
                    # print("\nfile opened") #use this line for debugging purposes
                    data = x.readlines() #this stores the information on the text file in a list. Each element is a line of the text file.
                    formattedData = [] #this empty list will store the information in data in a nested list
                    
                    for i in range(0,len(data)):
                        formattedData.append(data[i].split(',')) #this separates each line into the index, start time, and end time.
                        formattedData[i][2] = formattedData[i][2][:-2] #This removes the newline character (\n) in each line.
                        
                    return formattedData #This returns a 2D list in the form [index, [txt file index, start time, end time]]
        except FileNotFoundError: #this is just in case the date the user entered doesn't have data.
            #the next line is for debugging pur
            # print("file was not found") 
            return None
            


    def timeWastedOnDay(self, fileData): #this function determines how much time was wasted in a day. The fileData argument comes from the formatData function
        totalTimeWasted = []

        for i in range(1,len(fileData)): #this loop shows the time waste session number, the start time, and the end time.

            starts = datetime.datetime.strptime(fileData[i][1], '%Y-%m-%d %H:%M:%S.%f') #converts starts string data into dateTime object
            ends = datetime.datetime.strptime(fileData[i][2], '%Y-%m-%d %H:%M:%S.%f') #converts ends string data into dateTime object
            timeWasted = ends - starts #this creates timeDelta objects with the time wasted.
            totalTimeWasted.append(timeWasted) #adds the time wasted data in the loop to the end of the list.
        
        return totalTimeWasted #returns a list in the form [time wasted during a session]. Each element is a timedelta object
        

    def sessionInfo(self,date): # this function will show the periods of time wasted for a given date. The date must be in the form (int(year), int(month), int(day)). The function getDate supplies dates in this form.

        data = self.formatData(date[0],date[1],date[2])
        timeWastedList = self.timeWastedOnDay(data)
        for i in range(1,len(data)):
            print("\nTime waste session:", i)
            print("start: " + data[i][1])
            print("end :" + data[i][2])
            print("Time wasted this session: ",timeWastedList[i-1])
        print("\nYour total time wasted is ", sum(timeWastedList, datetime.timedelta(0,0))) #the sum function takes an iterable and the starting value and adds up all the elements inside it. datetime.timedelta(0,0) is 0:00:00 and 0 days. This allows the function to work, otherwise it'll try to add a timedela to an integer



    def timePeriodWasted(self): #this function shows how much time was wasted over a time period
        print("enter beginning of range ") #the next four lines get the date from the user
        begRange = self.getDate()
        print("\nenter end of range")
        endRange = self.getDate()
        begDate = datetime.date(begRange[0],begRange[1],begRange[2]) #the next two lines convert the dates into datetime objects.
        endDate = datetime.date(endRange[0],endRange[1],endRange[2])
        diff = endDate - begDate #this is a timeDelta object. It tells the differnce in days and seconds between datetime objects
        timePeriod = list(rrule(freq = DAILY, dtstart = begDate, count = diff.days+1)) #this function creates a list of dateTime objects from the beginning date to the end date.
        timesWasted = []
        for i in timePeriod:
            iData = self.formatData(i.year,i.month,i.day)
            if (iData is not None):
                x = self.timeWastedOnDay(iData)
                for j in x:
                    timesWasted.append(j)
        t = sum(timesWasted, datetime.timedelta(0,0))
        print("\nYour total time wasted is ", t)


#2020-4-3 todo
# Create functions for each of the main file options.
# rewrite sessionInfo to have data as an argument
# Develop a way to show most common time waste periods in a day.
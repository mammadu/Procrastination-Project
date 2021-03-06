# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from counter import counter

cn = counter()

exit = False

while exit == False:
    
    
    #the first option records start time, stop time, and date for time wasted sessions
    #The second option shows each period of time wasted on a specific day along with the total time wasted
    #the third option allows the user to input a time range. It then shows the total time wasted over the time period, 
        #the specifics time periods that were wasted, and which parts of the day had the most occurance of time being wasted.
    #The fourth option closes the program.
    
    choice = input("""
Please select option number:\n
1) record time wasted\n
2) display time wasted on day\n 
3) display time wasted over period of time\n
4) exit
""")
    
    if choice == '1':
        print("you chose option 1")
        cn.recordTimeWasted()
        cn.printTime()
    elif choice == '2':
        print("you chose option 2")
        cn.sessionInfo(cn.getDate())
    elif choice == '3':
        print("you chose option 3")
        cn.timePeriodWasted()
    elif choice == '4':
        print("you chose option 4. Goodbye")
        exit = True



#2020-3-9 todo
#options 1,2 have been completed.
#option 3 still has been completed but may possibly need to split into different functions
# Create functions for each of the main file options.
# Develop way to show time wasted during each session in option 3
# Develop a way to show most common time waste periods in a day.
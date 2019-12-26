# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# import counter

# cn = counter()

exit = False

while exit == False:
    
    choice = input("""
    Please select option number:\n
    1) record time wasted\n
    2) display time wasted on day\n
    3) display time wasted over period of time\n
    4) exit
    """)
    
    if choice == '1':
        print("you chose option 1")
        # cn.recordTimeWasted
    elif choice == '2':
        print("you chose option 2")
        # cn.sessionInfo()
    elif choice == '3':
        print("you chose option 3")
        # cn.timePeriodWasted()
    elif choice == '4':
        print("you chose option 4. Goodbye")
        exit = True



# counter.recordTimeWasted

# counter .
        
# Need to properly make the counter class
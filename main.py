from dataclasses import dataclass
from matplotlib import *
from bakery import assert_equal
import csv
# imports for functionality
'''
CHECKLIST:
    BASICS:
            Imports [X]
            ? []
            ? []
    DATA:
        Formatting []

'''
'''
    funcName:
    
    Arg(s):
        blah (type):
    
    Returns:
        type:

'''

# constants vvv
trafficData = [open('Data/trafficDataMon.csv'),
         open('Data/trafficDataTue.csv'),
         open('Data/trafficDataWed.csv'),
         open('Data/trafficDataThu.csv'),
         open('Data/trafficDataFri.csv'),
         ]#All of the traffic data in .csv format

# dataclasses vvv

#functions vvv



def toTime (time : str,amPm : str) -> int:
    '''
    toTime: when given a string and a time of day (AM/PM), the function returns the time as an int as army time
    
    Arg(s):
        time (str): the time as a string in the format "hour:minute"
        amPm (str): whether or not the time is in the morning or afternoon
    
    Returns:
        int: the current time in military time
    
'''
    timeHours = int(time.split(":")[0])
    timeMinutes = int(time.split(":")[1])
    #initializations of local variables
    
    if(amPm.lower() == "pm" and timeHours < 12):
        timeHours += 12
    elif(amPm.lower() == "am" and timeHours == 12):
        timeHours = 0#midnight
    #end of if statement
    
    return (timeHours * 100) + timeMinutes

'''
TEST CASES:
    assert_equal(toTime("11:59","AM"),1159)#basic returning
    assert_equal(toTime("11:59","PM"),2359)#PM case
    assert_equal(toTime("12:59","PM"),1259)#Noon case
    assert_equal(toTime("12:59","AM"),59)#Midnight case
'''
#end of function toTime

# start of actual code lol

print("Hello :D")
print()
print("=======================")
print("#    TransitTracer    #")
print("=======================")
print()
print("Made by: D3CL4NZ, DopoTSLol, Haiya-P, and ggellebazi")
choice = input("Please enter your choice: ")
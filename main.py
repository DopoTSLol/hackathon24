from dataclasses import dataclass
from matplotlib import *
#from bakery import assert_equal
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
#trafficData = [open('data/trafficDataMon.csv'),
#         open('data/trafficDataTue.csv'),
#         open('data/trafficDataWed.csv'),
#         open('data/trafficDataThu.csv'),
#         open('data/trafficDataFri.csv'),
#         ]#All of the traffic data in .csv format

# dataclasses vvv

#functions vvv

def getTraffic(d:str, t:int, s:str) -> float:
    """
    getTraffic: Gets the traffic for the specified day, time, and street.
    
    Example usage: getTraffic("Mon", 6, "Academy St")
    
    Arg(s):
        d (str): abbreviated day as a string (e.g. Mon, Tue, Wed, etc.)
        t (int): the hour as an int
        s (str): the street as a string
        
    Returns:
        float: the traffic as a float
    """
    
    row = 0
    col = 0
    
    # Set the row according to the street
    if(s == "S College Ave"):
        row = 1
    elif(s == "W DE Ave"):
        row = 2
    elif(s == "W Main St"):
        row = 3
    elif(s == "E Main St"):
        row = 4
    elif(s == "S Main St"):
        row = 5
    elif(s == "E DE Ave"):
        row = 6
    elif(s == "Academy St"):
        row = 7
    elif(s == "N College Ave"):
        row = 8
    elif(s == "David Hollowell Dr"):
        row = 9
    elif(s == "New London Road"):
        row = 10
    elif(s == "New London Ave"):
        row = 11
    elif(s == "E Park Pl"):
        row = 12
    else:
        print("[ERROR] Invalid street!")
        return -2.0
        
    if((t >= 6) and (t <= 17)):
        col = t - 5
    else:
        print("[ERROR] Invalid time!")
        return -3.0
    
    # Set the column number according to the time
    
    
    if(d == "Mon"):
        with open('data/trafficDataMon.csv', 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            
            #for row in reader:
            #    print(row)
            data = list(reader)
            csv_file.close()
            return data[row][col]
    elif(d == "Tue"):
        with open('data/trafficDataTue.csv', 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            
            #for row in reader:
            #    print(row)
            data = list(reader)
            csv_file.close()
            return data[row][col]
    elif(d == "Wed"):
        with open('data/trafficDataWed.csv', 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            
            #for row in reader:
            #    print(row)
            data = list(reader)
            csv_file.close()
            return data[row][col]
    elif(d == "Thu"):
        with open('data/trafficDataThu.csv', 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            
            #for row in reader:
            #    print(row)
            data = list(reader)
            csv_file.close()
            return data[row][col]
    elif(d == "Fri"):
        with open('data/trafficDataFri.csv', 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            
            #for row in reader:
            #    print(row)
            data = list(reader)
            csv_file.close()
            return data[row][col]
    else:
        print("[ERROR] Invalid day!")
        return -655.0
    

def toTime (t : str,amPm : str) -> int:
    '''
    toTime: when given a string and a time of day (AM/PM), the function returns the time as an int as army time
    
    Arg(s):
        time (str): the time as a string in the format "hour:minute"
        amPm (str): whether or not the time is in the morning or afternoon
    
    Returns:
        int: the current time in military time
    
'''
    timeHours = int(t.split(":")[0])
    timeMinutes = int(t.split(":")[1])
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
print("========================")
print("#    TransitTracker    #")
print("========================")
print()
print("Made by: D3CL4NZ, DopoTSLol, Haiya-P, and ggellebazi")
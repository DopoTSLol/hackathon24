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
STREET = ["S College Ave","W DE Ave","W Main St", "E Main St", "S Main St", "E DE Ave","Academy St", "N College Ave", "David Hollowell Dr", "New London Road", "New London Ave", "E Park Pl"]
DATE = ["Mon","Tue","Wed","Thu","Fri"]
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
        
    if((t >= 6) and (t <= 22)):
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
        
def printOptions(typeOfInput: int):
    iterationVar = 0
    if(typeOfInput == 0):
        for date in DATE:
            print(str(iterationVar)+" : "+date)
            iterationVar += 1
    else:
        for street in STREET:
            print(str(iterationVar)+" : " + street)
            iterationVar += 1
    print("\n========================\n")#formatting line
#end of function printOptions
    
def askForBool(message : str) -> bool:
    userAnswer = ""
    while(userAnswer.upper() != "Y" and userAnswer.upper() != "N"):
        userAnswer = input(message+"\n")
        if(userAnswer.upper() != "Y" and userAnswer.upper() != "N"):
            print("ERROR: Please input the characters Y or N")
    
    if(userAnswer.upper() == "Y"):
        return True
    else:
        return False
#end of function askForBool
    
def numToString(userInput : int, typeOfInput: int) -> str:
    if(typeOfInput == 0):
        if(len(DATE)-1 < userInput or 0 > userInput):
            return "" #failsafe case
        else:
            return DATE[userInput] #returns the date
    else:
        if(len(STREET)-1 < userInput or 0 > userInput):
            return "" #failsafe case
        else:
            return STREET[userInput] #returns the street
#end of function numToString
        
def detectActivityLevels(activityLevels : float)-> str:
    if(activityLevels == 1.0):
        return "little to none."
    elif(activityLevels <= 1.5):
        return "small."
    elif(activityLevels <= 2.0):
        return "moderate."
    elif(activityLevels <= 2.5):
        return "high."
    else:
        return "extreme."

# start of actual code lol

repeatVar = True
currentStreet = ""
currentDay = ""
currentActivity = -3.0
#^^ declaration of global variables^^

print("========================\n")
print("#    TransitTracker    #\n")
print("========================\n")
print("Made by: D3CL4NZ, DopoTSLol, Haiya-P, and ggellebazi\n")
print("========================\n")
print("TransitTracker is a simple python program designed to help you figure out where traffic currently is on the University of Delaware Campus")
print("You will soon be prompted to put in a day of the week")
input("Press enter to continue")
while(repeatVar):
    if(repeatVar):
        print("========================\n")
        print("Please input the current day of the week:")
        printOptions(0)
        
        while(currentDay == ""):
            
            currentDay = numToString(int(input("Please input a number between 0 and 4 [inclusive]")),0)#sets current day to the input of the user
            
            if(currentDay == ""):
                print("ERROR: Your number was not inside the bounds of 0 and 4 [inclusive]. Please submit a number within that range")#incase input isnt valid
            else:
                if(askForBool("You have selected : "+currentDay+".\nWould you like to change your answer? (Y or N)")):
                    currentDay = "" #incase user submitted the wrong thing
        #end of currentDay while loop
        print("\n========================\n")
        print("Please input your current relative locaion:")
        printOptions(1)
        
        while(currentStreet == ""):
            
            currentStreet = numToString(int(input("Please input a number between 0 and 11 [inclusive]")),1)#sets the current location/street name to the input of the user
            
            if(currentStreet == ""):
                print("ERROR: Your number was not inside the bounds of 0 and 11 [inclusive]. Please submit a number within that range")#incase input isnt valid
            else:
                if(askForBool("You have selected : "+currentStreet+".\nWould you like to change your answer? (Y or N)")):
                    currentStreet = "" #incase user submitted the wrong thing
        #end of currentStreet while loop
        print("\n========================\n")
        
        while (currentActivity == -3.0):
            
            currentHour = int(input("Please input an hour of the day in army time in army time between 6 and 22 [inclusive]"))#declaration of local currentHour variable
            
            currentActivity = getTraffic(currentDay, currentHour ,currentStreet)
            if(currentActivity == -3.0):
                print("ERROR: Your number was not inside the bounds of 6 and 22 [inclusive]. Please submit a number within that range")#incase input isnt valid
            else:
                if(askForBool("You have selected the hour: "+str(currentHour)+".\nWould you like to change your answer? (Y or N)")):
                    currentActivity = -3.0 #incase user submitted the wrong thing
            
        #end of currentHour while loop
        print("The current activity levels at "+currentStreet+" is "+detectActivityLevels(float(currentActivity))+", or a level of "+currentActivity)#prints the current users street, as well as the current 
        repeatVar = askForBool("Would you like to continue? Y to continue, N to quit")#asks user if they want to input something again
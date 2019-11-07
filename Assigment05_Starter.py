# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# <YOUR NAME HERE>,<DATE>,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants

strFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A dictionary that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python Dictionary.
open(strFile, "a")
objFile = open(strFile, "r")
for row in objFile:
    strData = row.split(",")
    dicRow = {"Task":strData[0], "Priority":strData[1]}
    lstTable.append(dicRow)
objFile.close()



# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item. (Note that pressing this will automatically delete the last item)
    4) Save Data to File
    5) Exit Program (Note that this will automatically exit the program.)
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        objFile = open(strFile, "r")
        print(lstTable)
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        Task = input("Please enter a Task:")
        Priority = input("Please enter a Priority:")
        dicRow = {"Task": Task, "Priority":Priority}
        lstTable.append(dicRow)

        continue
    # Step 5 - Remove a new item to the list/Table
    elif (strChoice.strip() == '3'):
        del lstTable[len(lstTable)-1]
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(strFile, "w")
        for row in lstTable:
            objFile.write(row['Task'] + ", " + row['Priority'] + '\n')
        objFile.close()
        print("File was successfully saved!")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):

        break  # and Exit the program

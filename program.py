import sys
import time

#Options
def optionA():
    print("option A")

def optionB():
    pass

def optionC():
    print("The system will now exit")
    time.sleep(2)
    sys.exit()

#Main Menu Function
def menu():
    print("***Main Menu***")
    time.sleep(1)

    choice = input ("""

                       A: Option 1 
                       B: Option 2
                       C: Quit

                       Please make a selection from above:
    
    """)
    
    if choice == "A" or choice == "a":
        optionA()
    elif choice == "B" or choice == "b":
        optionB()
    elif choice == "C" or choice == "c":
        optionC()
    else:
        print("Error Occured")
        menu()

menu()

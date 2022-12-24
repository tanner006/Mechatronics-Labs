#Demonstration of user inout and Error Handling
while True: #Cntinuously running loop
    userinput1 = input("Enter Character: \n") #This prompts the user to provide an input and assigns it to the variable string
    if userinput1 == "a": #evaluates if the user entered a string of "a"
        print ("Success") #Prints to the user
    elif userinput1 == "b": #evaluates if the user entered a string of "b"
        print ("Failure") #Prints to the user
    elif userinput1 == "stop": #evaluates if the user entered a string of "stop"
        break #This breaks out of the loop if the user entered stop, effectively stopping the program
    else:
        print ("Invalid Input, please try again.") #Prints to the user
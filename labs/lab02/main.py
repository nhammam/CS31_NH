# Starting file for LAB 2
# Include your course number, student first and last name, and date in the comment header
# CS 31 Nazar Hammam. 10/7/2026

#print out tilte
print() # print an empty line
print("My First Quiz on Python Concepts")
print() # print an empty line
print("*" * 20) # print a line of 20 astericks

#Ask for the use's name 
print()
username = input("What is your name"?)
print(f"Hello,{username}!") # f-string format

#Ask if they want to take a quiz 

print()
start_quiz = input("Do you want to take my First quiz? Y/N")
if start_quiz.upper()== "Y": # this will make any ;owercase input into an uppercase for compaariso 
    print("Great ! Let's get started!")
    #put our quiz questions here all indented 
    #START OUR QUESTIONs

    #Set our counter to 0
    counter = 0

    #Question 1
    q1 = int(input("How would Python solve 5*5?"))
    if q1 == 25:
        # update my counter because the they got the answer rigth 
        counter +=1 # short than for counter  = counter + 1
        print("Yes! you correctt. Python would solve this as 25.")
    else: # INCORRECT
        print("Sorry . That is not correct.")
    #Question 2
    print()
    print("What is the function that we use to output something to the terminal?")
    print()

 # Question 3
 # Question 4
 # Question 5





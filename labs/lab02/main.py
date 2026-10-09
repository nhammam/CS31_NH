# Starting file for LAB 2
# Include your course number, student first and last name, and date in the comment header
# CS 31 Nazar Hammam. 10/7/2026

#print out tilte
print() # print an empty line
print("My First Quiz on Python Concepts")
print() # print an empty line
print(" * " * 20) # print a line of 20 astericks

#Ask for the use's name 
print()
username = input("What is your name?")
print(f"Hello,{username}!") # f-string format

#Ask if they want to take a quiz 

print()
start_quiz = input("Do you want to take my First quiz? Y/N ")
if start_quiz.upper()== "Y": # this will make any owercase input into an uppercase for compaarison 
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
        print("Yes! you are correctt. Python would solve this as 25.")
    else: # INCORRECT
        print("Sorry . That is not correct.")
   
    #Question 2
    print()
    print(" *** Questions Two *** ")
    print("What is the function that we use to output something to the terminal?")
    print(" A - output()")
    print(" B - print ()")
    print(" C -format ()")
    print(" D - Non of the above")
    q2 = input("Your Answer - choose A/B/C/D: ")
    if q2.upper()== "B":
        # upper my counter because the got the answer right 
        counter += 1 # shortthand for counter = counter +1 
        print("Yes! You are correct. Python  would use the print() dunction to output something to the terminal.")
    else: #INCORRECT
        print("Sorry . That is not correct.")

 # Question 3
    print()
    print(" *** Questions Three *** ")
    q3 = input("What  function Python  use to prompt the user to enter a value?")
    if q3 == "input":
        counter +=1 # short than for counter  = counter + 1
        print("Yes! Python use Input Function.")
    else: # INCORRECT
           print("Sorry . That is not correct.")

 # Question 4
    print()
    print(" *** Questions Four *** ")

    print("What Python function is used to prompt a user to enter a value in a GIS application?")

    print("A - print()")
    print("B - input()")
    print("C - int()")
    print("D - type()")

    q4 = input("Your answer - choose A/B/C/D: ")

    if q4.upper() == "B":
    # Increase the counter because the answer is correct
        counter += 1
        print("Yes! You are correct. Python uses input() to prompt the user to enter a value.")
    elif q4.upper() in ["A", "C", "D"]:
        print("Sorry, that is not correct. The correct answer is B - input().")
    else:
        print("Invalid choice. Please enter A, B, C, or D.")

    print("Your score:", counter)
 # Question 5
    print()
    print(" *** Questions Four *** ")
    print("Which Python library is commonly used for data analysis and manipulation?")

    print("A - Matplotlib")
    print("B - Pandas")
    print("C - Turtle")
    print("D - Pygame")

    q5 = input("Your answer - choose A/B/C/D: ")

    if q5.upper() == "B":
    # Increase the counter because the answer is correct
        counter += 1
        print("Yes! You are correct. Pandas is commonly used for data analysis and manipulation.")

    elif q5.upper() in ["A", "C", "D"]:
        print("Sorry, that is not correct. The correct answer is B - Pandas.")

    else:
        print("Invalid choice. Please enter A, B, C, or D.")

    print("Your score:", counter)
 # Out the score 
    print(" * * * * YOUR FINAL SCORE * * * *")
    print(f"{username},your final score is: {counter} out of 5.")

    #Give them feedback on their overall score 
    if counter == 5:
        print("You are a rockstar ! You got them all correct !")
    elif counter >= 3 and counter < 5:
        print("Great work!")
    elif counter >= 1 and counter < 3:
        print("Keep studying and try again !")
    else:
       print("Maybe this isn't your genre? Try again later.")
elif start_quiz == "N":
    print("Sorry, maybe next time!")
else:  # if they type anything else tell them its invalid 
    print("Sorry, That is an invalid response. Try again.")

    #print a farewell message 
print("Thanks and have  agreat day !")


    








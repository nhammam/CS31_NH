# Starting file for LAB 3-1
# Include your course number, student first and last name, and date in the comment header

# Display a welcome message
print("The Miles Per Gallon program")
print()
# Setting a default choice for the  while loop
repeat_mpg ="y"
while repeat_mpg.lower() == "y"
# get input from the user
miles_driven = float(input("Enter miles driven:         "))
gallons_used = float(input("Enter gallons of gas used:  "))

if miles_driven <= 0:
    print("Miles driven must be greater than zero. Please try again.")
elif gallons_used <= 0:
    print("Gallons used must be greater than zero. Please try again.")
else:
    # calculate and display miles per gallon
    mpg = round(miles_driven / gallons_used, 2)
    print("Miles Per Gallon:          ", mpg)
print()
# Ask if they would like to repeat the program
repeat_mpg = input("Would you like to enter data for another trip?
(y/n) ")
print()

print("Bye!")

# Starting file for LAB 3-1
# Include your course number, student first and last name, and date in the comment header
# CS 31 Nazar Hammam. 10/14/2026
#Setting a defult choice for the while loop
repeat_mpg = "y"
while repeat_mpg.lower()== "y":
    # display a welcome message
    print("The Miles Per Gallon program")
    print() 

    # get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    cost_per_gallon = float(input("Enter the cost per gallon of gass:   "))

    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif cost_per_gallon <= 0:
        print("Cost per gallon must be greater than zero.Please try again.")
    else:
        # calculate and display miles per gallon
        mpg = round(miles_driven / gallons_used, 2)
        total_gas_cost = round(gallons_used * cost_per_gallon , 2)
        cost_per_mile = round(total_gas_cost / miles_driven ,2)
        print("Miles Per Gallon:          ", mpg)
        print("total Gas Cost: "           ,total_gas_cost)
        print("Cost Per Mile:   "          , cost_per_mile)
    print()
    #Ask if they would like to repeat the program
    repeat_mpg = input("Get entries for another trip (y/n)?")
    print()

print("Bye!")

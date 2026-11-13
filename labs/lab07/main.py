# CS 31 Nazar Hammam. 11/13/2026
# LAB 7: Miles Per Gallon program
# This program asks for miles driven and gallons used, calculates miles per gallon,
# and saves each trip to a CSV file so the data builds up over time.

# import the csv module so we can write comma-delimited data
import csv

# file name for our csv file
FILENAME = "trips.csv"


# function that saves all trips to the csv file
def write_trips(trips):
    # open the file with "a" (append) so existing data is kept
    # "w" would overwrite the file every time the program runs
    # newline="" stops blank lines from appearing between rows
    with open(FILENAME, "a", newline="") as file:
        # create a csv writer that uses the open file
        writer = csv.writer(file)
        # write every row (list) in trips to the file at once
        writer.writerows(trips)


# function that gets the miles driven from the user
def get_miles_driven():
    # keep asking until the entry is greater than zero
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:
        # invalid entry, show a warning and ask again
        print("Entry must be greater than zero. Please try again.\n")
    # valid entry, return it to the part of the program that called this function
    return miles_driven


# function that gets the gallons of gas used from the user
def get_gallons_used():
    # keep asking until the entry is greater than zero
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:
        # invalid entry, show a warning and ask again
        print("Entry must be greater than zero. Please try again.\n")
    # valid entry, return it to the caller
    return gallons_used


# main function where the program runs
def main():
    # display a welcome message
    print("The Miles Per Gallon program")
    print()

    # create a placeholder list to hold all of the trips
    trips = []

    # start with "y" so the loop runs at least once
    more = "y"

    # keep running while the user wants more entries
    while more.lower() == "y":
        # get the inputs from the user
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()

        # calculate miles per gallon and round it to two places
        mpg = round((miles_driven / gallons_used), 2)

        # display the calculation
        print(f"Miles Per Gallon:\t{mpg}")
        print()

        # create a list for the three values of this calculation (one record)
        trip = []
        # append miles driven first
        trip.append(miles_driven)
        # append gallons used second
        trip.append(gallons_used)
        # append the calculated miles per gallon third
        trip.append(mpg)

        # append this entire row to the trips list
        trips.append(trip)

        # ask whether the user wants to enter another trip
        more = input("More entries? (y or n): ")

    # the user said no, so save all of the trips to the csv file
    write_trips(trips)

    # say goodbye
    print("Bye!")


# run main() only when this file is run directly
if __name__ == "__main__":
    main()
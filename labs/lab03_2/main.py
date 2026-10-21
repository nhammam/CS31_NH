# Starting file for LAB 3-2
# Include your course number, student first and last name, and date in the comment header
# CS 31 Nazar Hammam. 10/14/2026
# display a welcome message
print("The Test Scores application")
print()
# Set the  default for while loop to run the first time
repeat_test_scores = "y"
while repeat_test_scores.lower() == "y":
    print("Enter test scores")
    print("Enter end to end input")
    print("======================")


    # initialize variables
    counter = 0
    score_total = 0
    test_score = 0

    while test_score != 999:
        test_score = input("Enter test score or end to end input: ")
        if test_score.lower() == "end":
         break
        else:
        #change the input to an intger
         test_score = int(test_score)

        if test_score >= 0 and test_score <= 100:
            score_total += test_score
            counter += 1
        
        else:
            print(f"Test score must be from 0 through 100. "
                f"Score discarded. Try again.")

    # calculate average score
    average_score = round(score_total / counter)
                    
    # format and display the result
    print("======================")
    print("Total Score:",score_total ,"\n Average Score:",average_score)
    print()
    repeat_test_scores = input("Would you like to enter another set of test scores (y/n)? ")
print()
print("Goodbye. Thanks for using the test scores program!")



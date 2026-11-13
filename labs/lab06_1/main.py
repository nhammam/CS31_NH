# Starting file for LAB 6-1
# Include your course number, student first and last name, and date in the comment header
# CS 31 Nazar Hammam. 11/05/2026

def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

def get_scores():
    scores = [] # initialize an empty list
    while True:
        score = input("Enter test score: ")
        if score == "x":
            return  scores
        else:
            score = int(score)
            if score >= 0 and score <= 100:
                # add the score to our list
                scores.append(score)
            else:
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")

def process_scores(scores):
    total = 0 #set a counter for total scores
    for score in scores:
        total += score

    # calculate average score
    average = round(total / len(scores))

    #get the min and max values
    low_score = min(scores)
    high_score = max(scores)

    #get the medain
    median_index = len(scores) // 2 

    if len(scores) % 2== 1: # if it is odd 
        median_score = scores[median_index]
    else:#if it id even 
        middle1 = scores[median_index]
        middle2 = scores[median_index - 1]# find the item of the one next to it
        median_score = (middle1+middle2) / 2


    
                
    # format and display the result
    print()
    print("Score total:       ", total)
    print("Number of Scores:  ", len(scores))
    print("Average Score:     ", average)
    print("Low Score:         ",low_score)
    print("High Score:        ",high_score)
    print("Median Score:        ",median_score)


def main():
    display_welcome()
    scores = get_scores()
    process_scores(scores)
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()


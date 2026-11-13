# Starting file for LAB 6-2
# Include your course number, student first and last name, and date in the comment header
# CS 31 Nazar Hammam. 11/05/2026
def list(movie_list):
    if len(movie_list) == 0:
        print("There are no movies in the list.\n")
        return
    else:
        for i, movie in enumerate(movie_list, start=1):
            print(f"{i}. {movie[0]} ({movie[1]})) ${movie[2]}")
        print()
def find_by_year(movie_list):
    year = int(input("Year: "))
    found_match = False # SET a flag for matches
    for movie in movie_list:
        if movie[1] == year:
            print(f"{movie[0]} was released in {year}.")
            found_match = True
    if found_match == False:
        print(f"No movies found for release in {year}.")
        print
    print()

def add(movie_list):
    name = input("Name: ")
    year = int(input("Year: "))
    price = float(input("Price:  "))
    movie = [name, year,price]
    movie_list.append(movie)
    print(f"{movie[0]} was added.\n")
    
def delete(movie_list):
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list):
        print("Invalid movie number.\n")
    else:
        movie = movie_list.pop(number-1)
        print(f"{movie[0]} was deleted.\n")

def display_menu():
    print("COMMAND MENU")
    print("list - List all movies")
    print("Find by year")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()
    
def main():
    movie_list = [["Monty Python and the Holy Grail", 1975,9.99],
                  ["On the Waterfront", 1954,8.99],
                  ["Cat on a Hot Tin Roof", 1958,1099]]
    
    display_menu()
    
    while True:        
        command = input("Command: ")
        if command.lower() == "list":
            list(movie_list)
        elif command.lower() == "find":
            find_by_year(movie_list)

        elif command.lower() == "add":
            add(movie_list)
        elif command.lower() == "del":
            delete(movie_list)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()

# Starting file for Project01
# Include your course number, student first and last name, and date in the comment header
# CS 31-Programming Project 1- Nazar Hammam. 10/25/2026
#Welcome to TechStore Online
print("======================================================")
print("TechStore Online")
print("Welcome to TechStore Online, your convenient destination for discovering technology products that support your education, career, business, and everyday life.")

# TechStore Online Virtual Shopping Assistant

print("TechStoreBot: Hello! Welcome to TechStore Online.")
print("TechStoreBot: Your trusted destination for technology products!")

learn = input("Would you like to learn more about our products? (y/n): ").lower()

if learn == "y":

    print("\n" + "=" * 50)
    print("          WELCOME TO TECHSTORE ONLINE")
    print("=" * 50)

    print("TechStore Online offers computers, laptops,")
    print("smartphones, tablets, accessories, audio products,")
    print("and storage devices to meet your technology needs.")

    print("\nTechStoreBot: Imagine a world where technology")
    print("makes your daily life easier! Whether you are a")
    print("student completing assignments, a programmer")
    print("building your next big idea, or a professional")
    print("working from home, TechStore Online can help you")
    print("find the right technology for your needs and budget.")
    print("We make shopping simple, convenient, and exciting!")

    print("\nTechStoreBot: Our featured product is a laptop.")
    print("It is perfect for studying, working, and exploring")
    print("your next big idea.")

    buy = input("\nWould you like to purchase a laptop? (y/n): ").lower()

    if buy == "y":

        print("\nTechStoreBot: Excellent choice!")
        print("Let's prepare your order.")

        first_name = input("Please enter your first name: ")
        last_name = input("Please enter your last name: ")
        email = input("Please enter your email address: ")
        phone = input("Please enter your phone number: ")

        price = 799.99

        print("\nTechStoreBot: The price of one laptop is $799.99.")

        quantity = int(input("How many laptops would you like to purchase? "))

        subtotal = quantity * price
        tax = subtotal * 0.10
        total = subtotal + tax

        print("\n" + "=" * 50)
        print("             TECHSTORE RECEIPT")
        print("=" * 50)

        print("Customer Name: ", first_name, last_name)
        print("Email Address: ", email)
        print("Phone Number:  ", phone)

        print("-" * 50)
        print("Product:       Laptop")
        print("Quantity:     ", quantity)
        print(f"Price per item: ${price:.2f}")# .2f = show as float with 2 decimal places

        print("-" * 50)
        print(f"Subtotal:      ${subtotal:.2f}")# .2f = show as float with 2 decimal places
        print(f"Sales Tax (10%): ${tax:.2f}")# .2f = show as float with 2 decimal places
        print("=" * 50)
        print(f"TOTAL DUE:     ${total:.2f}")# .2f = show as float with 2 decimal places
        print("=" * 50)

        print("\nTechStoreBot: Thank you for shopping with us!")
        print("We appreciate your business.")
        print("Have a wonderful day!")

    elif buy == "n":

        print("\nTechStoreBot: No problem!")
        print("Thank you for visiting TechStore Online.")
        print("Have a great day!")

    else:

        print("TechStoreBot: Please enter y or n.")

elif learn == "n":

    print("TechStoreBot: No problem!")
    print("Thank you for your time.")
    print("Have a wonderful day!")

else:

    print("TechStoreBot: Please enter y or n.")

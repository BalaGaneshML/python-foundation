import random
while True:
    print('''Enter the following numbers to particular programs:
        1:Contact Book
        2:FizzBuzz
        3:Inventory System
        4:Student Grade Book
        5:Multipliation Table Printer
        6:Number Guessing Game
        ''')

    choice= int(input("Enter the Value: "))
    if choice==1:
        contact={
            'bala':{'phone_no':123,'email':'123@gmail.com'},
            'ganesh':{'phone_no':456,'email':'456@gmail.com'},
            'raj':{'phone_no':789,'email':'789@gmail.com'},
            'arun':{'phone_no':246,'email':'246@gmail.com'},
            'jegan':{'phone_no':135,'email':'135@gmail.com'}}
        
        def display_all_contacts():
            for keys,values in contact.items():
                print(f"\nName : {keys}")
                print(f"Phone : {values['phone_no']}")
                print(f"Email : {values['email']}")

        def search_contact():
            name=input("enter name: ")
            find=contact.get(name)
            if find:
                print("\nContact Found!")
                print(f"Name : {name}")
                print(f"Phone : {find['phone_no']}")
                print(f"Email : {find['email']}")
            else:
                print("\nContact not found.")
        
        def add_contact():
            name=input("enter Name: ")
            if name in contact:
                print("Contact already exist.")
            else:
                phone=input("Enter Phone Number: ")
                email=input("Enter Email: ")
                contact[name]={
                    'phone_no':phone,
                    'email':email
                }     
                print("Contact Added Successfully")
                display_all_contacts()

        def update_contact():
            name=input("enter Name: ")
            if name not in contact:
                print("Contact not exist.")
            else:
                choice_1=int(input("Press 1 to update Phone\npress 2 to update Email:"))
                if choice_1==1:
                    phone=input("Enter Phone Number: ")
                    contact[name]['phone_no']=phone
                    print("Updated Successfully")
                    display_all_contacts()
                elif choice_1==2:
                    email=input("Enter Email: ")
                    contact[name]['email']=email
                    print("Updated Successfully") 
                    display_all_contacts()  
                else:
                    print("Enter Valid Response")

        def delete_contact():
            name=input("enter name: ")
            if name not in contact:
                print("Contact not exist.")
            else:
                choice_1=input("Are you Sure you want to delete this contact(Type yes to confirm, no to decline): ")
                choice_2=choice_1.lower()
                if choice_2=="yes":
                    deleted=contact.pop(name)
                    print("Deleted Successfully")
                    display_all_contacts()
                elif choice_2=="no":
                    print("Nothing Deleted")
                    display_all_contacts()
                else:
                    print("Enter Valid Response")
        
        while True:
            print("\n------ Contact Book ------")
            print("1: View All Contacts")
            print("2:Search Contacts")
            print("3: Add Contact")
            print("4: Update Contact")
            print("5: Delete Contact")
            print("6: Exit")

            choice_2= int(input("Enter your Choice: "))
            
            if choice_2==1:
                display_all_contacts()
            elif choice_2==2:
                search_contact()
            elif choice_2==3:
                add_contact()
            elif choice_2==4:
                update_contact()
            elif choice_2==5:
                delete_contact()
            elif choice_2==6:
                print("Exiting contact Book...") 
                break
            else:
                print("Invalid Choice")    


    elif choice==2:
        print(''' This Program can be done in two ways:
            type 1 for: Using if and else method
            tupe 2 for: using string method 
    ''')
        choice_3=int(input("Enter the choice: "))
        if choice_3==1:
            for i in range(1,101):
                if i%3==0 and i%5==0:
                    print("FizzBuzz")
                elif i%3==0:
                    print("Fizz")
                elif i%5==0:
                    print("Buzz")
                else:
                    print(i)

        if choice_3==2:
            for i in range(1,101):
                result= ""
                if i%3==0:
                    result +="Fizz"
                if i%5==0:
                    result +="Buzz"
                if result=="":
                    print(i)
                else:
                    print(result)


    elif choice==3:
        inventory = {
            'rice': 50,
            'sugar': 30,
            'oil': 20,
            'flour': 40,
            'salt': 60
        }

        def display_items():
            print("\nItem\t\tQuantity")
            print("-" * 25)

            for item, quantity in sorted(inventory.items()):
                print(item, "\t\t", quantity)

        def add_restock():
            item = input("Enter Item Name : ")
            quantity = int(input("Enter Quantity : "))

            if item in inventory:
                inventory[item] += quantity
                print("Stock Updated Successfully")
            else:
                inventory[item] = quantity
                print("New Item Added Successfully")

        def remove_item():
            item = input("Enter Item Name : ")

            if item not in inventory:
                print("Item Not Found")

            else:
                quantity = int(input("Enter Quantity To Remove : "))

                if inventory[item] - quantity < 0:
                    print("Operation Impossible")
                    print("Current Stock :", inventory[item])

                else:
                    inventory[item] -= quantity
                    print("Stock Updated Successfully")

        def search_item():
            item = input("Enter Item Name : ")

            if item in inventory:
                print("Quantity :", inventory[item])

            else:
                print("Item Not Found")

                print("Similar Items :")

                found = False

                for key in inventory:
                    if item in key:
                        print(key)
                        found = True

                if found == False:
                    print("No Similar Items Found")

        while True:

            print("\n===== INVENTORY MENU =====")
            print("1. Display All Items")
            print("2. Add / Restock Item")
            print("3. Remove Item")
            print("4. Search Item")
            print("5. Exit")

            choice = input("Enter Choice : ")

            if choice == "1":
                display_items()

            elif choice == "2":
                add_restock()

            elif choice == "3":
                remove_item()

            elif choice == "4":
                search_item()

            elif choice == "5":
                print("Exiting Program...")
                break

            else:
                print("Invalid Choice")
    

    elif choice==4:
        students = {
    'bala': [90, 92, 88, 95, 91],
    'ganesh': [45, 52, 38, 61, 49],
    'raj': [78, 82, 75, 80, 77],
    'arun': [60, 65, 58, 70, 62],
    'jegan': [35, 55, 65, 70, 80]
}

        def display_students():

            print("\n----- STUDENT DETAILS -----")

            for name, marks in students.items():

                average = sum(marks) / len(marks)

                print("\nName :", name)
                print("Marks :", marks)
                print("Average :", round(average, 2))


        def find_topper():

            topper = ""
            topper_marks = []
            highest = 0

            for name, marks in students.items():

                average = sum(marks) / len(marks)

                if average > highest:
                    highest = average
                    topper = name
                    topper_marks = marks

            print("\n----- CLASS TOPPER -----")
            print("Name :", topper)
            print("Marks :", topper_marks)
            print("Average :", round(highest, 2))


        def failed_students():

            print("\n----- FAILED BY AVERAGE -----")

            found = False

            for name, marks in students.items():

                average = sum(marks) / len(marks)

                if average < 55:
                    print(name)
                    found = True

            if found == False:
                print("No Students Failed By Average")

            print("\n----- FAILED BY SUBJECT -----")

            found = False

            for name, marks in students.items():

                for mark in marks:

                    if mark < 40:
                        print(name)
                        found = True
                        break

            if found == False:
                print("No Students Failed By Subject")


        def add_student():

            name = input("Enter Student Name : ")

            marks = []

            for i in range(5):

                while True:

                    mark = int(input(f"Enter Subject {i+1} Mark : "))

                    if 0 <= mark <= 100:
                        marks.append(mark)
                        break

                    else:
                        print("Invalid Mark. Enter Between 0 and 100")

            students[name] = marks

            print("Student Added Successfully")


        def rank_students():

            ranking = []

            for name, marks in students.items():

                average = sum(marks) / len(marks)

                ranking.append((average, name))

            ranking.sort(reverse=True)

            print("\n----- STUDENT RANK LIST -----")

            rank = 1

            for average, name in ranking:

                print(rank, ".", name, "-", round(average, 2))

                rank += 1


        while True:

            print("\n===== STUDENT GRADE BOOK =====")
            print("1. Display All Students")
            print("2. Find Class Topper")
            print("3. Find Failed Students")
            print("4. Add New Student")
            print("5. Rank All Students")
            print("6. Exit")

            choice = input("Enter Your Choice : ")

            if choice == "1":
                display_students()

            elif choice == "2":
                find_topper()

            elif choice == "3":
                failed_students()

            elif choice == "4":
                add_student()

            elif choice == "5":
                rank_students()

            elif choice == "6":
                print("Exiting Program...")
                break

            else:
                print("Invalid Choice")
    

    elif choice==5:
        for row in range(1, 11):

            for column in range(1, 11):

                result = row * column

                print(f"{result:4d}", end="")

            print()
    

    elif choice==6:

        number = random.randint(1, 100)

        attempts = 0

        print("Welcome to the Number Guessing Game!")
        print("I have selected a number between 1 and 100. Can you guess it?")

        while True:

            if attempts >= 10:
                print(f"Game Over! You've used all 10 attempts. The number was {number}.")
                break

            try:
                guess = int(input("Enter your guess : "))

            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            attempts += 1

            if guess==number:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
            
            difference = abs(guess - number)
            if difference <= 10:
                print("Very Hot!")
            elif difference <= 20:
                print("Hot!")
            elif difference <= 40:
                print("Warm!")
            else:
                print("Cold!")
            if guess < number:
                print("Guess Higher!")
            else:
                print("Guess Lower!")  

    else:
        print("Invalid Choice")  
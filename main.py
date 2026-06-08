students = []
hosts = []
workshops = []
bookings = []

def register_student():

    name = input("Enter student name: ")
    email = input("Enter student email: ")
    password = input("Enter password: ")

    student = {
        "name": name,
        "email": email,
        "password": password
    }

    students.append(student)

    print("Student registered successfully!")

def register_host():
    name = input("Enter host name: ")
    email = input("Enter host email: ")
    password = input("Enter password: ")
    verified = False

    host = {
        "name": name,
        "email": email,
        "password": password,
        "verified": verified
    }
    hosts.append(host)

    print("Host registered successfully!")

while True:
    print("\n===== SkillBridge =====")
    print("1. Register Student")
    print("2. Register Host")
    print("3. View Students")
    print("4. View Hosts")
    print("5. Create Workshop")
    print("6. View Workshops")
    print("7. Book Workshop")
    print("8. View Bookings")
    print("9. Verified host")
    print("10. Exit")
    


    choice = int(input("Enter your choice: "))

    if choice == 1:
        register_student()

    elif choice == 2:
        register_host()

    elif choice == 3:
        print("\nRegistered Students:")
        for student in students:
            print("Name:", student["name"])
            print("Email:", student["email"])
            print("password:", student["password"])
            print()

    elif choice == 4:
        print("\nRegistered Hosts:")
        for host in hosts:
            print("Name:", host["name"])
            print("Email:", host["email"])
            print("password:", host["password"])
            print("Verified:", host["verified"])
            print()

    elif choice == 5:
        title = input("Enter workshop title: ")
        host_name = input("Enter host name: ")
        fee = float(input("Enter workshop fee: "))
        category = input("Enter workshop category: ")
        capacity = int(input("Enter the number of seats available: "))
        workshop = {
            "title": title,
            "host": host_name,
            "fee": fee,
            "category": category,
            "capacity": capacity,
            "available_seats": capacity,
        }

        host_found = False

        for host in hosts:
            if host["name"] == host_name and host["verified"]:
              host_found = True
              break

        if host_found:
            workshops.append(workshop)
            print("Workshop created successfully!")

        else:
            print("only verified hosts can create workshops!")

    elif choice == 6:
        print("\nAvailable Workshops:")

        for workshop in workshops:
            print("Title:", workshop["title"])
            print("Host:", workshop["host"])
            print("Fee:", workshop["fee"])
            print("Category:", workshop["category"])
            print("Capacity:", workshop["capacity"])
            print("available seats in the workshop:", workshop["available_seats"])    
            print()

    elif choice == 7:
        student_name = input("Enter student name: ")
        workshop_title = input("Enter workshop title: ")

        student_found = False
        for student in students:
            if student["name"] == student_name:
                student_found = True
                break

        workshop_found = False
        selected_workshop = None
        for workshop in workshops:
            if workshop["title"] == workshop_title:
                workshop_found = True
                selected_workshop = workshop
                break
        


        if student_found and workshop_found:


            if student_found and workshop_found:

              if selected_workshop["available_seats"] == 0:
                print("Sorry, no seats available for this workshop!")
                continue

            selected_workshop["available_seats"] -= 1

            booking = {
                "student_name": student_name,
                "workshop_title": workshop_title
                    }

            bookings.append(booking)

            print("Workshop booked successfully!")

        else:
             print("Student or Workshop not found!")



    elif choice == 8:
        print("\nBooked Workshops:")
        for booking in bookings:
            print("Student:", booking["student_name"])
            print("Workshop:", booking["workshop_title"])
            print()

    elif choice == 9:
        host_name = input("Enter host name to verify: ")

        found = False
        for host in hosts:
            if host["name"] == host_name:
    
                host["verified"] = True
                found = True
                print("Host verified successfully!")
                break

        if not found:
                print("Host not found!")

    elif choice == 10:
        print("Thank you for using SkillBridge!")
        break

    else:
        print("Invalid choice!")
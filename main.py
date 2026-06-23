from db import connection, cursor

students = []
hosts = []
workshops = []
bookings = []


def register_student():
    name = input("Enter student name: ")
    email = input("Enter student email: ")
    password = input("Enter password: ")

    cursor.execute(
        "INSERT INTO students(name,email,password) VALUES(%s,%s,%s)",
        (name, email, password)
    )

    connection.commit()

    print("Student registered successfully!")


def register_host():
    name = input("Enter host name: ")
    email = input("Enter host email: ")
    password = input("Enter password: ")

    cursor.execute(
        """
        INSERT INTO hosts(name,email,password,verified)
        VALUES(%s,%s,%s,%s)
        """,
        (name, email, password, False)
    )

    connection.commit()

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
    print("9. Verify Host")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        register_student()

    elif choice == 2:
        register_host()

    elif choice == 3:

        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()

        print("\nRegistered Students:")

        for student in students:
            print("ID:", student[0])
            print("Name:", student[1])
            print("Email:", student[2])
            print("Password:", student[3])
            print()

    elif choice == 4:

        cursor.execute("SELECT * FROM hosts")
        hosts = cursor.fetchall()

        print("\nRegistered Hosts:")

        for host in hosts:
            print("ID:", host[0])
            print("Name:", host[1])
            print("Email:", host[2])
            print("Password:", host[3])
            print("Verified:", host[4])
            print()

    elif choice == 5:

        title = input("Enter workshop title: ")
        host_name = input("Enter host name: ")
        fee = float(input("Enter workshop fee: "))
        category = input("Enter workshop category: ")
        capacity = int(input("Enter the number of seats available: "))

        cursor.execute(
            """
            SELECT * FROM hosts
            WHERE name = %s
            AND verified = TRUE
            """,
            (host_name,)
        )

        host = cursor.fetchone()

        if host:

            cursor.execute(
                """
                INSERT INTO workshops
                (title, host_name, fee, category, capacity, available_seats)
                VALUES(%s,%s,%s,%s,%s,%s)
                """,
                (
                    title,
                    host_name,
                    fee,
                    category,
                    capacity,
                    capacity
                )
            )

            connection.commit()

            print("Workshop created successfully!")

        else:
            print("Host not found or not verified!")

    elif choice == 6:

        cursor.execute("SELECT * FROM workshops")
        workshops = cursor.fetchall()

        print("\nAvailable Workshops:")

        for workshop in workshops:
            print("ID:", workshop[0])
            print("Title:", workshop[1])
            print("Host:", workshop[2])
            print("Fee:", workshop[3])
            print("Category:", workshop[4])
            print("Capacity:", workshop[5])
            print("Available Seats:", workshop[6])
            print()

    elif choice == 7:

        student_name = input("Enter student name: ")
        workshop_title = input("Enter workshop title: ")

        # Check student exists
        cursor.execute(
            """
            SELECT * FROM students
            WHERE name = %s
            """,
            (student_name,)
        )

        student = cursor.fetchone()

        if not student:
            print("Student not found!")
            continue

        # Check workshop exists
        cursor.execute(
            """
            SELECT * FROM workshops
            WHERE title = %s
            """,
            (workshop_title,)
        )

        workshop = cursor.fetchone()

        if not workshop:
            print("Workshop not found!")
            continue

        # Check seats available
        available_seats = workshop[6]

        if available_seats <= 0:
            print("Sorry, no seats available!")
            continue

        # Check duplicate booking
        cursor.execute(
            """
            SELECT * FROM bookings
            WHERE student_name = %s
            AND workshop_title = %s
            """,
            (student_name, workshop_title)
        )

        existing_booking = cursor.fetchone()

        if existing_booking:
            print("You have already booked this workshop!")
            continue

        # Create booking
        cursor.execute(
            """
            INSERT INTO bookings(student_name, workshop_title)
            VALUES(%s,%s)
            """,
            (student_name, workshop_title)
        )

        # Reduce seats
        cursor.execute(
            """
            UPDATE workshops
            SET available_seats = available_seats - 1
            WHERE title = %s
            """,
            (workshop_title,)
        )

        connection.commit()

        print("Workshop booked successfully!")

    elif choice == 8:

        cursor.execute("SELECT * FROM bookings")
        bookings = cursor.fetchall()

        print("\nBooked Workshops:")

        for booking in bookings:
            print("ID:", booking[0])
            print("Student:", booking[1])
            print("Workshop:", booking[2])
            print()

    elif choice == 9:

        host_name = input("Enter host name to verify: ")

        cursor.execute(
            """
            UPDATE hosts
            SET verified = TRUE
            WHERE name = %s
            """,
            (host_name,)
        )

        connection.commit()

        print("Host verified successfully!")

    elif choice == 10:

        print("Thank you for using SkillBridge!")
        break

    else:
        print("Invalid choice!")
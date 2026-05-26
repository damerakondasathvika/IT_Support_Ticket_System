tickets = []

while True:

    print("\nHELPDESK TICKET MANAGEMENT SYSTEM")

    print("1. Add Ticket")
    print("2. View Tickets")
    print("3. Search Ticket")
    print("4. Update Ticket Status")
    print("5. Delete Ticket")
    print("6. Exit")

    try:

        choice = int(
            input(
                "Enter choice: "
            )
        )

    except ValueError:

        print(
            "Invalid input! Enter a number"
        )

        continue

    if choice == 1:

        ticket_id = input(
            "Enter Ticket ID (Example: T101): "
        )

        if not (
            ticket_id.startswith("T")
            and
            ticket_id[1:].isdigit()
        ):

            print(
                "Invalid Ticket ID Format"
            )

            continue

        duplicate = False

        for t in tickets:

            if t[
                "ticket_id"
            ] == ticket_id:

                duplicate = True

                break

        if duplicate:

            print(
                "Ticket ID already exists"
            )

            continue

        employee_name = input(
            "Enter Employee Name: "
        )

        print("\nIssue Types")

        print("1. Hardware")
        print("2. Software")
        print("3. Network")
        print("4. Access Issue")
        print("5. System Error")

        try:

            issue_choice = int(
                input(
                    "Enter choice: "
                )
            )

        except ValueError:

            print(
                "Invalid input"
            )

            continue

        if issue_choice == 1:

            issue_type = "Hardware"

            print(
                "\nExamples: Monitor issue, Printer issue, Keyboard issue"
            )

        elif issue_choice == 2:

            issue_type = "Software"

            print(
                "\nExamples: VS Code crash, Excel not opening"
            )

        elif issue_choice == 3:

            issue_type = "Network"

            print(
                "\nExamples: WiFi disconnected, VPN issue"
            )

        elif issue_choice == 4:

            issue_type = "Access Issue"

            print(
                "\nExamples: Login failed, Password reset"
            )

        elif issue_choice == 5:

            issue_type = "System Error"

            print(
                "\nExamples: Application error, Server issue"
            )

        else:

            print(
                "Invalid Choice"
            )

            continue

        issue_description = input(
            "Enter Issue Description: "
        )

        if len(
            issue_description.strip()
        ) < 5:

            print(
                "Enter valid issue description"
            )

            continue

        print("\nStatus")

        print("1. Open")
        print("2. In Progress")
        print("3. Resolved")
        print("4. Closed")

        try:

            status_choice = int(
                input(
                    "Enter choice: "
                )
            )

        except ValueError:

            print(
                "Invalid input"
            )

            continue

        if status_choice == 1:

            status = "Open"

        elif status_choice == 2:

            status = "In Progress"

        elif status_choice == 3:

            status = "Resolved"

        elif status_choice == 4:

            status = "Closed"

        else:

            print(
                "Invalid Choice"
            )

            continue

        ticket = {

            "ticket_id":
            ticket_id,

            "employee_name":
            employee_name,

            "issue_type":
            issue_type,

            "issue_description":
            issue_description,

            "status":
            status

        }

        tickets.append(
            ticket
        )

        print(
            "Ticket Added Successfully"
        )

    elif choice == 2:

        if len(
            tickets
        ) == 0:

            print(
                "No Tickets Found"
            )

        else:

            print(
                "\nALL TICKETS"
            )

            for t in tickets:

                print(
                    "\n--------------------"
                )

                print(
                    "Ticket ID:",
                    t["ticket_id"]
                )

                print(
                    "Employee:",
                    t["employee_name"]
                )

                print(
                    "Issue Type:",
                    t["issue_type"]
                )

                print(
                    "Description:",
                    t["issue_description"]
                )

                print(
                    "Status:",
                    t["status"]
                )

    elif choice == 3:

        search_id = input(
            "Enter Ticket ID: "
        )

        found = False

        for t in tickets:

            if t[
                "ticket_id"
            ] == search_id:

                found = True

                print(
                    "\nTicket Found"
                )

                print(
                    t
                )

                break

        if not found:

            print(
                "Ticket Not Found"
            )

    elif choice == 4:

        update_id = input(
            "Enter Ticket ID: "
        )

        found = False

        for t in tickets:

            if t[
                "ticket_id"
            ] == update_id:

                found = True

                print("\nStatus")

                print("1. Open")
                print("2. In Progress")
                print("3. Resolved")
                print("4. Closed")

                status_choice = int(
                    input(
                        "Enter choice: "
                    )
                )

                if status_choice == 1:

                    t[
                        "status"
                    ] = "Open"

                elif status_choice == 2:

                    t[
                        "status"
                    ] = "In Progress"

                elif status_choice == 3:

                    t[
                        "status"
                    ] = "Resolved"

                elif status_choice == 4:

                    t[
                        "status"
                    ] = "Closed"

                else:

                    print(
                        "Invalid Choice"
                    )

                    break

                print(
                    "Ticket Updated"
                )

                break

        if not found:

            print(
                "Ticket Not Found"
            )

    elif choice == 5:

        delete_id = input(
            "Enter Ticket ID: "
        )

        found = False

        for t in tickets:

            if t[
                "ticket_id"
            ] == delete_id:

                found = True

                tickets.remove(
                    t
                )

                print(
                    "Ticket Deleted"
                )

                break

        if not found:

            print(
                "Ticket Not Found"
            )

    elif choice == 6:

        print(
            "Exiting System"
        )

        break

    else:

        print(
            "Invalid Choice"
        )
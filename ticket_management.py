ticket_management=[
    {"ticket_id":1231,"emp_name":"Sathvika","issue_type":"hardware","issue_description":"monitor issue","status":"in_progress"},
    {"ticket_id":1232,"emp_name":"Bhavya","issue_type":"software","issue_description":"update failure","status":"open"},
    {"ticket_id":1233,"emp_name":"Durgasree","issue_type":"network","issue_description":"vpn issue","status":"resolved"},
    {"ticket_id":1234,"emp_name":"Tirumala","issue_type":"hardware","issue_description":"cpu issue","status":"in_progress"},
    {"ticket_id":1235,"emp_name":"Sidharth","issue_type":"software","issue_description":"login failed","status":"in_progress"},
    {"ticket_id":1236,"emp_name":"Venky","issue_type":"printer","issue_description":"printer issue","status":"open"}
]
for ticket in ticket_management:
    print(ticket)
    if ticket["issue_type"]=="hardware":
        print("Valid Hardware Category")
    elif ticket["issue_type"]=="software":
        print("Valid Software Category")
    elif ticket["issue_type"]=="network":
        print("Valid Network Category")
    else:
        print("Invalid Ticket Category")
    print()

ticket_management=[
    {"ticket_id":1231,"emp_name":"Sathvika","issue_type":"hardware","issue_description":"monitor issue","status":"in_progress","priority":"high"},
    {"ticket_id":1232,"emp_name":"Bhavya","issue_type":"software","issue_description":"update failed","status":"open     ","priority":"low"},
    {"ticket_id":1233,"emp_name":"Durgasree","issue_type":"network","issue_description":"vpn issue","status":"resolved","priority":"medium"},
    {"ticket_id":1234,"emp_name":"Tirumala","issue_type":"hardware","issue_description":"cpu issue","status":"in_progress","priority":"low"},
    {"ticket_id":1235,"emp_name":"Sidharth","issue_type":"software","issue_description":"login failed","status":"in_progress","priority":"medium"},
    {"ticket_id":1236,"emp_name":"Venkey","issue_type":"network","issue_description":"slow network","status":"open    ","priority":"high"}
]
print("ticket_id\t emp_name\t issue_type\t issue_description\t status\t\t priority")
for i in ticket_management:
    print(i["ticket_id"],"\t\t",i["emp_name"],"\t",i["issue_type"],"\t",i["issue_description"],"\t\t",i["status"],"\t",i["priority"])
print("\n")
x=input("enter issue type:")
print("\n")
print("ticket_id\t emp_name\t issue_type\t issue_description\t status\t\t priority")
for i in ticket_management:
    if i["issue_type"]==x:
          print(i["ticket_id"],"\t\t",i["emp_name"],"\t",i["issue_type"],"\t",i["issue_description"],"\t\t",i["status"],"\t",i["priority"])


       

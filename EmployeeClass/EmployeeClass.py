class Employee:
    def __init__(self,name,ID_number,department,job_title):
        self.name = name
        self.id_num = ID_number
        self.department = department
        self.job = job_title
susan_meyers = Employee("Susan Meyers",47899,"Acounting","Vice President")
mark_jones = Employee("Mark Jones",39119,"IT","Programmer")
joy_rogers = Employee("Joy Rogers", 81774,"Manufacturing","Engineer")
save_to_nonvolitile = input("would you like to save the employee data to a file? Y/N")
list_of_employees = [susan_meyers,mark_jones,joy_rogers]
if save_to_nonvolitile == "Y" or save_to_nonvolitile == "y":
    with open ("EmployeeData.txt","w") as f:
        for employee in list_of_employees:
            f.write(f"Name: {employee.name}, ID Number: {employee.id_num}, Department: {employee.department}, Job Title: {employee.job} \n")
            print(employee.name,"saved to file")
else:
    print("have a wonderfull day")

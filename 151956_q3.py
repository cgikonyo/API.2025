class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}, ID: {self.employee_id}, Salary: {self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"{self.name}'s salary updated to {self.salary}")


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Added {employee.name} to {self.department_name}")

    def total_salary_expenditure(self):
        total = sum(emp.salary for emp in self.employees)
        print(f"Total salary expenditure: {total}")

    def display_all_employees(self):
        if not self.employees:
            print("No employees yet.")
        else:
            for emp in self.employees:
                emp.display_details()


# Interactive session
department = Department("IT Department")

while True:
    print("\n--- Department Management Menu ---")
    print("1. Add employee")
    print("2. Update employee salary")
    print("3. Display all employees")
    print("4. Show total salary expenditure")
    print("5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter employee name: ")
        eid = input("Enter employee ID: ")
        salary = float(input("Enter salary: "))
        employee = Employee(name, eid, salary)
        department.add_employee(employee)

    elif choice == "2":
        emp_name = input("Enter employee name to update salary: ")
        for emp in department.employees:
            if emp.name == emp_name:
                new_salary = float(input("Enter new salary: "))
                emp.update_salary(new_salary)
                break
        else:
            print("Employee not found.")

    elif choice == "3":
        department.display_all_employees()

    elif choice == "4":
        department.total_salary_expenditure()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
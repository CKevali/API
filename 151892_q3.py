class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}, Salary: {self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Updated salary for {self.name} to {self.salary}.")

class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Added {employee.name} (ID: {employee.employee_id}) to {self.department_name} department.")

    def total_salary_expenditure(self):
        total = sum(employee.salary for employee in self.employees)
        print(f"Total salary expenditure for {self.department_name} department is: {total}")
        return total

    def display_all_employees(self):
        print(f"Employees in {self.department_name} department:")
        for employee in self.employees:
            employee.display_details()

    def interactive_mode(self):
        while True:
            print("\nOptions:")
            print("1: Add an employee")
            print("2: Update an employee's salary")
            print("3: Display all employees")
            print("4: Display total salary expenditure")
            print("5: Exit")
            choice = input("Enter your choice: ")
            
            if choice == "1":
                name = input("Enter employee name: ")
                employee_id = input("Enter employee ID: ")
                salary = float(input("Enter employee salary: "))
                employee = Employee(name, employee_id, salary)
                self.add_employee(employee)
            
            elif choice == "2":
                employee_id = input("Enter employee ID: ")
                employee = next((e for e in self.employees if e.employee_id == employee_id), None)
                if employee:
                    new_salary = float(input("Enter new salary: "))
                    employee.update_salary(new_salary)
                else:
                    print("Employee not found.")
            
            elif choice == "3":
                self.display_all_employees()
            
            elif choice == "4":
                self.total_salary_expenditure()
            
            elif choice == "5":
                print("Exiting interactive mode.")
                break
            
            else:
                print("Invalid choice. Please try again.")



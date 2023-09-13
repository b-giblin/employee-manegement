class Employee:
  def __init__(self, emp_id, name, title, salary):
    self.emp_id = emp_id
    self.name = name
    self.title = title
    self.salary = salary

  def display(self):
    return f"{self.emp_id}: {self.name} - {self.title} - ${self.salary}"
  
  def promote(self, new_title, raise_amount):
    self.title = new_title
    self.salary += raise_amount



class ManagementSystem:
  def __init__(self):
    self.employees = []


  def add_employee(self, emp_id, name, title, salary):
    employee = Employee(emp_id, name, title, salary)
    self.employees.append(employee)

  def promote_employee(self, emp_id, new_title, raise_amount):
    try:
      for emp in self.employees:
        if emp.emp_id == emp_id:
          emp.promote(new_title, raise_amount)
          print(f"Promoted {emp.name} to {new_title} with a raise of ${raise_amount}.")
          return
    except:
      print(f"Employee ID {emp_id} not found.")
  
  def display_all_employees(self):
    for emp in self.employees:
      print(emp.display())


# Using the class
system = ManagementSystem()

# Add Employees
system.add_employee(1, "Brian", "Software Developer", 75000)
system.add_employee(2, "Bob", "Data Scientist", 65000)
system.add_employee(3, "Marissa", "UI/UX Designer", 60000)

# display list of employees just added

system.display_all_employees()


# promote an employee 

system.promote_employee(2,"Senior Data Scientist", 10000)
system.display_all_employees()
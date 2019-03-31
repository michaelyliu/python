class Employee():
	def __init__(self, first,last,pay):
		self.first = first
		self.last =last
		self.pay = pay
	

class Developer(Employee):
	def __init__(self, first,last,pay,lang):
		super().__init__(first,last,pay)
		self.lang=lang



class Manager(Employee):
	def __init__(self, first, last, pay, employees):
		super().__init__(first,last,pay)
		self.employees = employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)




emp_1 = Employee("Michael", "Liu", 50000)

print(emp_1)


#employees = [emp_1]

mgr_1 = Manager("Michael", "Liu", 50000, [emp_1])

print (mgr_1)


dev_1 = Developer("Michael", "Liu", 50000, "Java")
print(dev_1)

#print(help(Developer))

print (dir(object))


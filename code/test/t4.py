class Employee():
	def __init__(self, first,last,pay):
		self.first = first
		self.last =last
		self.pay = pay
	

class Developer(Employee):
	def __init__(self, first,last,pay,lang):
		Super(first,last,pay)
		self.lang=lang

emp_1 = Developer("Michael", "Liu", 50000)

print(emp_1)

dev_1 = Developer("Michael", "Liu", 50000, "Java")
print(dev_1)


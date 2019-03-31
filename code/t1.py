courses = ["His","her","math","art"]

for index, value in enumerate (courses, start =5):
	print (index, value)


course_str = ", ".join(courses)
print (course_str)

new_list = course_str.split(",")
print new_list



student = {"name": "Michael", "age": 25, "course": ["math","sci"] }
print student .get('name1', "NG")


for key, value in student.items():
	print key, 
value



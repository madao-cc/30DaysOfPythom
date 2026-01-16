#!/usr/bin/env python3

# DAY 8

# 1. Declare an empty dictionary
empty_dict = {}

#Add name, color, breed, legs, age to the dog dictionary
dog = {
	'name' : 'Zira',
	'color' : 'Brown',
	'breed' : 'From the streets',
	'legs' : 4,
	'age' : 10
}

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital_status, skills, country, city and address as keys for the dictionary
student = {
	'first_name' : 'Miguel',
	'last_name' : 'Couceiro',
	'gender' : 'Male',
	'age' : 16,
	'marital_status' : 'Single',
	'skills' : ['Python', 'C++', 'C', 'HTML', 'CSS'],
	'country' : 'Portugal',
	'city' : 'Porto',
	'address' : '123 Main St, Anytown'
}

# 4. Get the length of the student dictionary
print("Length of student dictionary:", len(student))

# 5. Get the value of skills and check the data type, it should be a list
skills = student.get('skills')
print("Skills:", skills)
print(f"Data type of skills: {type(skills)}")

# 6. Modify the skills values by adding one or two skills
student['skills'].extend(['JavaScript', 'Java'])
print("Updated skills:", student['skills'])
# or 
# student['skills'] += ['JavaScript', 'Java']

# 7. Get the dictionary keys as a list
print(student.keys())

# 8. Get the dictionary values as a list
print(student.values())

# 9. Change the dictionary to a list of tuples using items() method
student = student.items()
print("Student dictionary as list of tuples:", student)

# 10. Delete one of the items in the dictionary
student = dict(student)  # Convert back to dictionary for deletion
del student['marital_status']
print("Student dictionary after deletion:", student)

# 11. Delete the dictionary completely
del student

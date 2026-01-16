#!/usr/bin/env python3

# DAY 9

# LEVEL 1

# 1.
age = input("Enter your age: ")
while not age.isdigit():
	age = input("Please enter a valid age (number): ")
age = int(age)
if age >= 18:
    print("You are old enough to drive.")
else:
    years_left = 18 - age
    print(f"You need to wait {years_left} more year(s) to drive.")

# 2.
age = input("Enter your age: ")
while not age.isdigit():
	age = input("Please enter a valid age (number): ")
age = int(age)
my_age = 16
diff = abs(my_age - age)
if age > my_age:
	if diff == 1:
		print(f"You are {diff} year older than me.")
	else:
		print(f"You are {diff} years older than me.")
elif age < my_age:
	if diff == 1:
		print(f"You are {diff} year younger than me.")
	else:
		print(f"You are {diff} years younger than me.")
else:
    print("We are the same age.")

# 3.
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
while not (num1.isdigit() and num2.isdigit()):
	num1 = input("Please enter a valid first number: ")
	num2 = input("Please enter a valid second number: ")
num1 = int(num1)
num2 = int(num2)
if num1 > num2:
    print(f"{num1} is greater than {num2}.")
elif num1 < num2:
    print(f"{num1} is less than {num2}.")
else:
    print(f"{num1} is equal to {num2}.")

# LEVEL 2

# 1.
score = input("Enter your score (0-100): ")
while not (score.isdigit()):
	score = input("Please enter a valid score: ")
score = int(score)
if 90 <= score <= 100:
	grade = 'A'
elif 80 <= score < 90:
	grade = 'B'
elif 70 <= score < 80:
	grade = 'C'
elif 60 <= score < 70:
	grade = 'D'
elif 50 <= score < 60:
	grade = 'E'
elif 0 <= score < 50:
	grade = 'F'
else:
	grade = None
if grade:
	print(f"Your grade is: {grade}")
else:
	print("Invalid score entered.")

# 2.
months_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
month = input("Enter month name: ")
month = month.capitalize()
if month in months_list:
	index = months_list.index(month)
	season_index = index // 3
	seasons = ['Winter', 'Spring', 'Summer', 'Fall']
	print(f"{month} is in {seasons[season_index]}.")
else:
	print("Invalid month entered.")

# 3.
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter a fruit: ")
if (fruit in fruits):
	print(f"{fruit} was found in the list.")
	print(fruits)
else:
	print(f"{fruit} was not found in the list, adding it now.")
	fruits.append(fruit)
	print(fruits)

# LEVEL 3

# 1.
# Takes to much effort for a simple exercise
print("Got too tired... Do it yourself if you trully want it...🥱")
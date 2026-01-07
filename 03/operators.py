#!/usr/bin/env python3

# DAY 3

import math

# 1 , 2 , 3
age = int(16)
height = float(2.00)
complex_number = complex(4 + 3j)

# 4
base = int(input("Enter base: "))
height = int(input("Enter height: "))
area_of_triangle = 0.5 * base * height
print("The area of the triangle is:", area_of_triangle)

# 5
side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))
perimeter_of_triangle = side_a + side_b + side_c
print("The perimeter of the triangle is:", perimeter_of_triangle)

# 6
length = int(input("Enter length: "))
width = int(input("Enter width: "))
area_of_rectangle = length * width
perimeter_of_rectangle = 2 * (length + width)
print("The area of the rectangle is:", area_of_rectangle)
print("The perimeter of the rectangle is:", perimeter_of_rectangle)

# 7
radius = int(input("Enter radius: "))
area_of_circle = math.pi * radius**2
circum_of_circle = 2 * math.pi * radius
print("The area of the circle is:", area_of_circle)
print("The circumference of the circle is:", circum_of_circle)

# 8 - Calculate the slope (m) x-intercept and y-intercept of y = 2x -2
slope = 2
y_intercept = -2
x_intercept = -y_intercept / slope
print("Slope (m):", slope)
print("Y-Intercept:", y_intercept)
print("X-Intercept:", x_intercept)

# 9 - Slope and euclidean distance between point (2, 2) and (6, 10)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_points = (y2 - y1) / (x2 - x1)
euclidean_distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Slope between points:", slope_points)
print("Euclidean distance between points:", euclidean_distance)

# 10 - Compare the slopes
print("Is the slope of the line equal to the slope between the points?", slope == slope_points)

# 11 - Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
for x in range(-5, 5):
	y = x**2 + 6*x + 9
	if y == 0:
		print("When x =", x, ", y is 0.")
		break
else: # The else block executes if the loop completes without a break
	print("No x value found in the range that makes y equal to 0.")

# 12 - Find the length of 'python' and 'dragon' and make a falsy comparison statement.
len_python = len('python')
len_dragon = len('dragon')
print("Is length of 'python' equal to length of 'dragon'?", len_python == len_dragon)

# 13 - Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("Is 'on' found in both 'python' and 'dragon'?", 'on' in 'python' and 'on' in 'dragon')

# 14 - I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = "I hope this course is not full of jargon."
print("Is 'jargon' in the sentence?", 'jargon' in sentence)

# 15 - Find the length of the text 'python' and convert the value to float and then to string
length_python = len('python')
length_as_float = float(length_python)
length_as_string = str(length_as_float)
print("Length of 'python' as float:", length_as_float)
print("Length of 'python' as string:", length_as_string)

# 16 - Even numbers are divisible by 2 and the remainder is zero. Write a code that checks if a number is even or not.
number = int(input("Enter a number to check if it's even: "))
is_even = (number % 2) == 0
print("Is the number even?", is_even)

# 17 - Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
floor_division_result = 7 // 3
int_converted_value = int(2.7)
print("Is the floor division of 7 by 3 equal to int(2.7)?", floor_division_result == int_converted_value)

# 18 - Check if type of '10' is equal to type of 10
print("Is type of '10' equal to type of 10?", type('10') == type(10))

# 19 - Check if int('9.8') is equal to 10
print("Is int(float('9.8')) equal to 10?", int(float('9.8')) == 10)

# 20 - Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = float(input("Enter hours worked: "))
rate_per_hour = float(input("Enter rate per hour: "))
pay = hours * rate_per_hour
print("The pay of the person is:", pay)

# 21 - Write a script that prompts the user to enter number of years. Calculate the number of seconds a person have lived. Assume a person can live hundred years
years = int(input("Enter number of years you have lived: "))
seconds_in_a_year = 365 * 24 * 60 * 60
total_seconds_lived = years * seconds_in_a_year
print("You have lived for", total_seconds_lived, "seconds.")

# 22 - Write a Python script that displays the table
for i in range(1, 6)
	print(1, i, i**2, i**3)
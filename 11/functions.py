#!/usr/bin/env python3

# DAY 11

# 1. Define a function called add_two_numbers. It should take two parameters and return their sum

def add_two_numbers(a, b):
	return a + b

# 2. Define a function called area_of_circle. It should take one parameter (radius) and return the area of the circle
import math

def area_of_circle(radius):
	return math.pi * radius ** 2

# 3. Define a function called add_all_sum wich takes arbitrary number of arguments and sums all the arguments. Check if the list arguments are all number types. If not give a reasonable feedback
def add_all_sum(*args):
	total = 0
	for num in args:
		if type(num) not in [int, float]:
			return "All arguments must be numbers."
		total += num
	return total

# 4. Function that converts Celsius to Fahrenheit
def convert_celsius_to_fahrenheit(celsius):
	if type(celsius) not in [int, float]:
		return "Input must be a number."
	return (celsius * 9/5) + 32

# 5. check_seanson function
def check_season(month):
	month = month.lower()
	if month in ['december', 'january', 'february']:
		return 'Winter'
	elif month in ['march', 'april', 'may']:
		return 'Spring'
	elif month in ['june', 'july', 'august']:
		return 'Summer'
	elif month in ['september', 'october', 'november']:
		return 'Autumn'
	else:
		return "Invalid month name."

# 6. calculate_slope function
def calculate_slope(x1, y1, x2, y2):
	if x2 - x1 == 0:
		return "Slope is undefined (vertical line)."
	return (y2 - y1) / (x2 - x1)

# 7. Calculates solution set of a quadratic equasion
def solve_quadratic(a, b, c):
	discriminant = b**2 - 4*a*c
	if discriminant < 0:
		return "No real solutions."
	elif discriminant == 0:
		x = -b / (2*a)
		return (x,) # returning a tuple with one element
	else:
		x1 = (-b + math.sqrt(discriminant)) / (2*a)
		x2 = (-b - math.sqrt(discriminant)) / (2*a)
		return (x1, x2)

# 8. takes a list as a parameter and returns eaxh element
def print_list(items: list): # this just says "I excpect a list here"
	for item in items:
		print(item)

# 9.  takes an array as parameter and returns the reverse of the array (use loops)
def reverse_array(arr):
	reversed_arr = []
	for item in arr:
		reversed_arr.insert(0, item)
	return reversed_arr

# 10. takes a list and returns a capitalized list
def capitalize_list(strings: list):
	capitalized= []
	for c in strings:
		capitalized.append(c.capitalize())
	return capitalized

# 11. takes a list and an item parameters. Returns list with item added at the end
def add_item(arr: list, item):
	arr.append(item)
	return arr

# 12. takes a list and an item parameters. Returns list with item removed from the list
def remove_item(arr: list, item):
	if item in arr:
		arr.remove(item)
	return arr

# 13. takes a number and adds all the numbers from 0 to that number
def sum_of_numbers(n: int):
	total = 0
	for i in range(n + 1):
		total += i
	return total

# 13. Takes a number and adds all the odd numbers from 0 to that number
def sum_of_odds(n: int):
	total = 0
	for i in range(n + 1):
		if i % 2 != 0:
			total += i
	return total

# 14. Takes a number and adds all the even numbers from 0 to that number
def sum_of_evens(n: int):
	total = 0
	for i in range(n + 1):
		if i % 2 == 0:
			total += i
	return total

# LEVEL 2

# 1. It takes a positive integer as parameter and it counts number of evens and odds in the number.
def count_evens_and_odds(n: int):
	if not isinstance(n, int):
		return "Input must be an integer."
	if n < 0:
		return "Input must be a positive integer."
	even_count = 0
	odd_count = 0
	for i in range(n + 1):
		if i % 2 == 0:
			even_count += 1
		else:
			odd_count += 1
	return even_count, odd_count

# 2. takes a whole number as a parameter and return a factorial of the number
def factorial(n: int):
	if not isinstance(n, int) or n < 0:
		return "Input must be a non-negative integer."
	result = 1
	while n > 1:
		result *= n
		n -= 1
	return result

# 3. It takes a parameter an check if it is empty or not
def is_empty(param):
	if param:
		return False
	else:
		return True

# 4. Write different functions wich take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std_deviation
def calculate_mean(numbers: list):
	if not isinstance(numbers, list) or len(numbers) == 0:
		return "Input must be a non-empty list."
	return sum(numbers) / len(numbers)

def calculate_median(numbers: list):
	if not isinstance(numbers, list) or len(numbers) == 0:
		return "Input must be a non-empty list."
	sorted_numbers = sorted(numbers)
	mid = len(sorted_numbers) // 2
	if len(sorted_numbers) % 2 == 0:
		return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
	else:
		return sorted_numbers[mid]

def calculate_mode(numbers: list):
	if not isinstance(numbers, list) or len(numbers) == 0:
		return "Input must be a non-empty list."
	frequency = {}
	for num in numbers:
		if num in frequency:
			frequency[num] += 1
		else:
			frequency[num] = 1
	max_freq = max(frequency.values()) # find the highest frequency
	modes = [num for num, freq in frequency.items() if freq == max_freq] # This returns a list of all numbers with the highest frequency
	if len(modes) == len(frequency): # if all numbers occur with the same frequency, no mode exists
		return "No mode found."
	return modes

def calculate_range(numbers: list):
	if not isinstance(numbers, list) or len(numbers) == 0:
		return "Input must be a non-empty list."
	return max(numbers) - min(numbers)

def calculate_variance(numbers: list):
	if not isinstance(numbers, list) or len(numbers) == 0:
		return "Input must be a non-empty list."
	mean = calculate_mean(numbers)
	variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
	return variance

def calculate_std(numbers: list):
	if not isinstance(numbers, list) or len(numbers) == 0:
		return "Input must be a non-empty list."
	variance = calculate_variance(numbers)
	return math.sqrt(variance)

# 4. Write a function called greet wich takes a default argument "name". If no argument is supplied it should print ""Hello, Guest", otherwise it should freet the person by name
def greet(name = "Guest"):
	return f"Hello, {name}"

"""
Alternative version:
def greet(name):
	if not name:
		return "Hello, Guest"
	else:
		return f"Hello, {name}"
"""

# 4.1 Worte a function show_args to take an arbitrary number of arguments and print their names and values
def show_args(**kargs):
	for key, value in kargs.items():
		print(f"{key}: {value}")

# LEVEL 3

# 1. Write a function called is_prime, wich checks if a number is prime
def is_prime(n: int):
	if not isinstance(n, int) or n <= 1:
		return False
	for i in range(2, int(math.sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

# 2. Write a function wich checks if all itmes are unique in the list
def are_items_unique(items: list):
	if not isinstance(items, list):
		return "Input must be a list."
	return len(items) == len(set(items))

# 3. Write a function wich checks if all items of the list are of the same data type
def are_items_same_type(items: list):
	if not (isinstance(items, list) or len(items) == 0):
		return "Input must be a non-empty list."
	first_type = type(items[0])
	for item in items:
		if type(item) != first_type:
			return False
	return True

# 4. Write a function wich checks if the provided variable is a valid Python variable
def is_valid_variable(var: str):
	if not isinstance(var, str):
		return "Input must be a string."
	valid_vars = ["int", "float", "complex", "str", "list", "tuple", "range", "dict", "set", "frozenset", "bool", "bytes", "Bytearray", "memoryview", "NoneType"]
	return var in valid_vars

# 5. Go to the data folder and acces the countries-data.py:
import sys
sys.path.append(0, '../data')
from countries_data import countries_data as countries # type: ignore

# 5.1. Create a function called most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
def most_spoken_languages(n = 10):
	language_count = {}
	for country in countries:
		if "languages" in country:
			for lang in country["languages"]:
				if lang in language_count:
					language_count[lang] += 1
				else:
					language_count[lang] = 1
	sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
	return sorted_languages[:n]

# 5.2 Create a function most_populated_countries. It should return 10 or 20 most populated countries in descending order
def most_populated_countries(n = 10):
	country_population = {}
	for country in countries:
		country_population[country['name']] = country['population']
	sorted_countries = sorted(country_population.items(), key=lambda x: x[1], reverse=True)
	return sorted_countries[:n]

# Clean up
del countries
#!/usr/bin/env python3
# type: ignore
# Day 10

# LEVEL 1

# 1. Iterate 0 to 10 using for loop, do the same using while loop
print("For loop from 0 to 10:")
for i in range(11):
	print(i, end=' ')
print()
print("While loop from 0 to 10:")
i = 0
while i <= 10:
	print(i, end=' ')
	i += 1
print()

# 2. Iterate 10 to 0 using for loop, do the same using while loop
print("For loop from 10 to 0:")
for i in range(10, -1, -1):
	print(i, end=' ')
print()
print("While loop from 10 to 0:")
i = 10
while i >= 0:
	print(i, end=' ')
	i -= 1
print()

# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
for i in range(7):
	print('#' * (i + 1))

# 4. Use nested loops to create the following:
for i in range(8):
	for j in range(i + 1):
		print('#', end=' ')
	print()

# 5. Print the following pattern:
for i in range(11):
	    print(f"{i} x {i} = {i * i}")

# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items
technologies = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for tech in technologies:
    print(tech)

# 7. Use a for loop to iterate from 0 to 100 and print only even numbers
for i in range(101):
	if i % 2 == 0:
		print(i, end=' ')
print()

# 8. Use a for loop to iterate from 0 to 100 and print only odd numbers
for i in range(101):
	if i % 2 != 0:
		print(i, end=' ')
print()

# LEVEL 2

# 1. Use a for loop to iterate from 0 to 100 and print the sum of all numbers.
total_sum = 0
for i in range(101):
	total_sum += i
print(f"Sum of all numbers from 0 to 100: {total_sum}")

# 2. Use a for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
even_sum = 0
odd_sum = 0
for i in range(101):
	if i % 2 == 0:
		even_sum += i
	else:
		odd_sum += i
print(f"Sum of even numbers from 0 to 100: {even_sum}")
print(f"Sum of odd numbers from 0 to 100: {odd_sum}")

# LEVEL 3

# 1. Extract all the countries containing the word land
import sys
sys.path.insert(0, '../data')
from countries import countries

for country in countries:
	if 'land' in country:
		print(country)
del countries

# 2. Reverse the order of this list using loop
fruit = ['banana', 'orange', 'mango', 'lemon']
reversed_fruit = []
for i in range(len(fruit) - 1, -1, -1):
    reversed_fruit.append(fruit[i])
print("Reversed fruit list:", reversed_fruit)

# 3.
# I. What are the total number of unique languages in the data
from countries_data import countries_data as countries
languages = set()
for country in countries:
	for lang in country["languages"]:
		languages.add(lang)
print(f"Total unique languages: {len(languages)}")

# II. Find the ten most spoken languages from the data
language_count = {}
for country in countries:
	if 'languages' in country:
		for lang in country['languages']:
			if lang in language_count:
				language_count[lang] += 1
			else:
				language_count[lang] = 1
sorted_languages = sorted(language_count.items(), key=lambda x: x[1])
# sorted() returns a new sorted list of tuples (language, count)
# It will be sorted regarding the x[1] which is the count
print("Ten most spoken languages:")
for lang, count in sorted_languages[-10:]:
	print(f"{lang}: {count}")


# III. Find the ten most populated countries in the world
country_population = {}
for country in countries:
	country_population[country['name']] = country['population']
sorted_countries = sorted(country_population.items(), key=lambda x: x[1])
print("Ten most populated countries:")
for name, population in sorted_countries[-10:]:
	print(f"{name}: {population}")

del countries

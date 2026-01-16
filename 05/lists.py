#!/usr/bin/env python3

# DAY 5

# 1. Declare an empty list
empty_list = []

# 2. Declare a list with more than 5 items
fruits = ['apple', 'banana', 'cherry', 'peach', 'grape', 'pear']

# 3. Find the length of your list
fruits_length = len(fruits)
print(f"Length of fruits list: {fruits_length}")
# or write t like this:
# print("Lenght of te fruits list:", fruits_length)

# 4. Get the first item, the middle item and the last item of the list
print("First item:", fruits[0])
print(f"Middle item: {fruits[len(fruits) // 2]}")
print("Last item:", fruits[-1])

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Miguel Couceiro', 16, 2.00, 'Single', '123 Main St, Anytown']

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Print the list using print()
print(f"IT Companies: {it_companies}")

# 8. Print the number of companies in the list
print(len(it_companies))

# 9. Print the first, middle and last company
print("First company:", it_companies[0])
print("Middle company:", it_companies[len(it_companies) // 2])
print("Last company:", it_companies[-1])

# 10. Print the list after modifying one of the companies
it_companies[0] = 'Meta'
print("Modified IT Companies:", it_companies)

# 11. Add an IT company to it_companies
it_companies.append('Critical Software')

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies) // 2, 'Intel')

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()
print(f"IT companies: {it_companies}")

# 14. Join the it_companies with a string '#;  '
joined_companies = '#; '.join(it_companies)
print("Joined IT Companies:", joined_companies)

# 15. Check if a certain company exists in the it_companies list.
print('Apple' in it_companies)  # True or False

# 16. Sort the list using sort() method
it_companies.sort()
print("Sorted IT Companies:", it_companies)

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print("Reversed IT Companies:", it_companies)

# 18. Slice out the first 3 companies from the list
print("First 3 companies:", it_companies[:3])

# 19. Slice out the last 3 companies from the list
print("Last 3 companies:", it_companies[-3:])

# 20. Slice out the middle IT company or companies from the list
it_companies.append('Cisco')
print(f"IT companies: {it_companies}")
middle_index = len(it_companies) // 2
if len(it_companies) % 2 == 0:
	print("Middle companies:", it_companies[middle_index - 1:middle_index + 1])
else:
	print("Middle company:", it_companies[middle_index])

# 21. Remove the first IT company from the list
it_companies.pop(0)
print("After removing first company:", it_companies)

# 22. Remove the middle IT company or companies from the list
middle_index = len(it_companies) // 2
if len(it_companies) % 2 == 0:
	it_companies.pop(middle_index - 1)
	it_companies.pop(middle_index - 1)  # middle_index shifts after first pop
else:
	it_companies.pop(middle_index)
print("After removing middle company/companies:", it_companies)

# 23. Remove the last IT company from the list
it_companies.pop(-1)
print("After removing last company:", it_companies)

# 24. Remove all IT companies from the list
it_companies.clear()
print("After removing all companies:", it_companies)

# 25. Destroy the IT companies list
del it_companies

# 26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joined = front_end + back_end
print("Full Stack:", joined)

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack_2. Then insert Python and SQL after Redux.
full_stack = joined.copy()
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')
print("Full Stack 2:", full_stack)

# LEVEL 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# 1. Sort the ages list and find the min and max age
ages.sort()
min_age = ages[0]
max_age = ages[-1]
print(f"Sorted ages: {ages}")
print(f"Min age: {min_age}, Max age: {max_age}")

# 2. Find the median age (one middle item or two middle items divided by two)
middle_index = len(ages) // 2
if len(ages) % 2 == 0:
	median_age = (ages[middle_index - 1] + ages[middle_index]) / 2
else:
	median_age = ages[middle_index]
print(f"Median age: {median_age}")

# 3. Find the average age (sum of all items divided by their number)
average_age = sum(ages) / len(ages)
print(f"Average age: {average_age}")

# 4. Find the range of the ages (max minus min)
age_range = max_age - min_age
print(f"Age range: {age_range}")

# 5. Compare the value of (min - average) and (max - average), use abs() method
min_avg_diff = abs(min_age - average_age)
max_avg_diff = abs(max_age - average_age)
print(f"Min-Average difference: {min_avg_diff}")
print(f"Max-Average difference: {max_avg_diff}")

# Find the middle country(ies) in the countries list
import sys
sys.path.append('../data')
from countries import countries

middle_index = len(countries) // 2
if len(countries) % 2 == 0:
	print("Middle countries:", countries[middle_index - 1:middle_index + 1])
else:
	print("Middle country:", countries[middle_index])

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
if len(countries) % 2 == 0:
	first_half = countries[:len(countries) // 2]
	second_half = countries[len(countries) // 2:]
else:
	first_half = countries[:len(countries) // 2 + 1]
	second_half = countries[len(countries) // 2 + 1:]

# Unpack the first three countries and the rest as scandic countries.
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first, second, third, *scandic_countries = countries
print("First three countries:", first, second, third)
print("Scandic countries:", scandic_countries)
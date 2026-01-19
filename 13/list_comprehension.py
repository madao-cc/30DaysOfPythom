#!/usr/bin/env python3

# DAY 13

# LEVEL 1

# 1. 
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_nbrs = [nbr for nbr in numbers if nbr <= 0]

# 2.
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [item for lst in list_of_lists for item in lst]
""" This is equivalent to:
flattened_list = []
for lst in list_of_lists:
	for item in lst:
		flattened_list.append(item) """

# 3.
tuples_list = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range (11)]

# 4.
countries = [[("Finland", "Helsinki"), ("Sweden", "Stockholm"), ("Norway", "Oslo")]]
result = [[country[0].upper(), country[0][:3].upper(), country[1].upper()] for country in countries[0]]
""" This is equivalent to:
result = []
for country in countries[0]:
	country_info = []
	country_info.append(country[0].upper())
	country_info.append(country[0][:3].upper())
	country_info.append(country[1].upper())
	result.append(country_info)
"""

# 5. 
countries  = [[("Finland", "Helsinki"), ("Sweden", "Stockholm"), ("Norway", "Oslo")]]
result = [{'country': country[0].upper(), 'city': country[1].upper()} for country in countries[0]]

# 6. 
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
result = [f'{first} {last}' for name in names for (first, last) in name]
""" This is equivalent to:
result = []
for name in names:
	for (first, last) in name:
		result.append(f'{first} {last}')
"""

# 7. Write a lamda function wich can solve a slope or y-intercept of linear functions
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
y_intercept = lambda m, x, y: y - m * x

# Example usage:
# m = slope(2, 3, 4, 7)  # Slope
# b = y_intercept(m, 2, 3)  # Y-intercept
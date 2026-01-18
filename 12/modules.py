#!/usr/bin/env python3

# DAY 12

# Level 1

# 1. Function that generates a siz digit/character ramdon_user_id
import random , string

def generate_random_id():
	size = 6
	alphabet = string.ascii_letters + string.digits
	return "".join(random.choices(alphabet, k=size))

# 2. user_id_gen_by_user function. Don't take any parameter but it takes two inputs using input(). nbr of characters and number of IDs wich are suppose to be generated.
def user_id_gen_by_user():
	nbr_chars = int(input("Enter number of characters: "))
	nbr_ids = int(input("Enter number of IDs to generate: "))
	alphabet = string.ascii_letters + string.digits
	ids = []
	for i in range(nbr_ids):
		ids.append("".join(random.choices(alphabet, k=nbr_chars)))
	return ids

# 3. rgb_color_gen. It generates rgb colors
def rgb_color_gen():
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	return f"rgb({r}, {g}, {b})"

# LEVEL 2

# 1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors(n: int):
	colors = []
	for _ in range(n):
		color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
		colors.append(color)
	return colors

# 2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(n: int):
	colors = []
	for _ in range(n):
		r = random.randint(0, 255)
		g = random.randint(0, 255)
		b = random.randint(0, 255)
		colors.append(f"rgb({r}, {g}, {b})")
	return colors

# 3. Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(color_type: str, n: int):
	if color_type == 'hexa':
		return list_of_hexa_colors(n)
	elif color_type == 'rgb':
		return list_of_rgb_colors(n)
	else:
		return "Invalid color type. Please choose 'hexa' or 'rgb'."
	
# LEVEL 3

# 1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(lst: list):
	shuffled = lst[:] # If we just wrote shuffled = lst, both variables would point to the same list in memory. We want to make a shallow copy of the list so that we can change it freely and avoid errors later on.
	random.shuffle(shuffled)
	return shuffled

# 2. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def unique_random_numbers():
	numbers = random.sample(range(10), 7)
	return numbers

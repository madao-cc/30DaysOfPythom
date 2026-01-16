#!/usr/bin/env python3

# DAY 6

# LEVEL 1

# 1. Declare an empty tuple
empty_tuple = ()

# 2. Create a tuple with names of brothers and sisters
brothers = ('Luis', 'Carlos')
sisters = ('Ana', 'Zira')

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print("Siblings:", siblings)

# 4. How many siblings do you have?
print(f"Number of siblings: {len(siblings)}")

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ('Rui', 'Maria')
print("Family Members:", family_members)

# LEVEL 2

# 1. Unpack siblings tuple into brother1, brother2, sister1 and sister2
# Option A
*siblings, parent1, parent2 = family_members
parents = (parent1, parent2)

# Option B
# siblings = family_members[:-2]
# parents = family_members[-2:]

print("Siblings unpacked:", siblings)
print("Parents unpacked:", parents)

# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple', 'banana', 'cherry')
vegetables = ('carrot', 'broccoli', 'spinach')
animal_products = ('milk', 'cheese', 'yogurt')

food_stuff_tp = fruits + vegetables + animal_products
print("Food Stuff Tuple:", food_stuff_tp)

# 3. Change the food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print("Food Stuff List:", food_stuff_lt)

# 4. Slice out the middle item(s) from the food_stuff_tp tuple
middle_index = len(food_stuff_tp) // 2
if len(food_stuff_tp) % 2 == 0:
	middle_items = food_stuff_tp[middle_index - 1:middle_index + 1]
else:
	middle_items = (food_stuff_tp[middle_index],)
print("Middle item(s):", middle_items)

# 5. Slice out the first three items and the last three items from food_stuff_tp tuple
first_three = food_stuff_tp[:3]
last_three = food_stuff_tp[-3:]
print("First three items:", first_three)
print("Last three items:", last_three)

# 6. Delete the food_stuff_tp tuple completely
del food_stuff_tp

# 7. Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)  # Should return False
print('Iceland' in nordic_countries)  # Should return True
#!/usr/bin/env python3

# DAY 7

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# LEVEL 1

# 1. Find the length of the set it_companies
print("Length of it_companies set:", len(it_companies))

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print("it_companies after adding Twitter:", it_companies)

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['Tesla', 'Intel', 'AMD'])
print("it_companies after adding multiple companies:", it_companies)

# 4. Remove one of the companies from the set it_companies
removed_company = it_companies.pop()  # removes an arbitrary element
print(f"Removed company: {removed_company}")
print("it_companies after removing one company:", it_companies)

# 5. What is the difference between remove and discard
# remove() raises a KeyError if the element is not found, while discard() does not
it_companies.discard('NonExistentCompany')  # No error raised

# LEVEL 2

# 1. Join A and B
union_set = A.union(B)
print("Union of A and B:", union_set)

# 2. Find A intersection B
intersection_set = A.intersection(B)
print("Intersection of A and B:", intersection_set)

# 3. Is A subset of B
is_subset = A.issubset(B)
print("Is A a subset of B?:", is_subset)

# 4. Are A and B disjoint sets
are_disjoint = A.isdisjoint(B)
print("Are A and B disjoint sets?:", are_disjoint)

# 5. Join A with B and B with A
A_update = A.union(B)
B_update = B.union(A)
print("A joined with B:", A_update)
print("B joined with A:", B_update)

# 6. What is the symmetric difference between A and B
symmetric_diff = A.symmetric_difference(B)
print("Symmetric difference between A and B:", symmetric_diff)

# 7. Delete the sets completely
del A
del B

# LEVEL 3

# 1. Convert the ages list to a set and compare the length of the list and the set
ages_set = set(age)
print("Length of ages list:", len(age))
print("Length of ages set:", len(ages_set))

# 2. Explain the difference between the following data types: string, list, tuple and set
# - String: An immutable sequence of characters used to store text.
# - List: A mutable ordered collection of items that can contain duplicates.
# - Tuple: An immutable ordered collection of items that can contain duplicates.
# - Set: A mutable unordered collection of unique items (no duplicates).

# 3. I am a teacher and I love to inspire and teach people. How many unique words have I used? Use the split methods and set to find the unique words.
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
unique_words = set(words)
print(f"Words in the sentence: {words}")
print("Unique words in the sentence:", unique_words)
print("Number of unique words:", len(unique_words))
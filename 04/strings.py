#!/usr/bin/env python3

# DAY 4

# 1 - Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string
str1 = 'Thirty'
str2 = 'Days'
str3 = 'Of'
str4 = 'Python'
joined_string = ' '.join([str1, str2, str3, str4])
print(joined_string)

# 2 - Concatenate the string 'Coding', 'For' , 'All' to a single string
str1 = 'Coding'
str2 = 'For'
str3 = 'All'
joined_string = ' '.join([str1, str2, str3])
print(joined_string)

# 3 - Declare a variable named company and assign it to an initial value 'Coding For All'
company = 'Coding For All'

# 4 - Print the variable company using print()
print(company)

# 5 - Print the length of the company string using len() method and print()
print(len(company))

# 6 - Change all the characters to uppercase letters using upper() method
print(company.upper())

# 7 - Change all the characters to lowercase letters using lower() method
print(company.lower())

# 8 - Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9 - Cut(slice) out the first word of Coding For All string
company = "Coding For All"
first_word = company[0:6]
print(first_word)

# 10 - Check if Coding For All string contains the word 'Coding' using the method index, find or other methods
print(company.find('Coding'))  # returns the starting index of the substring
print('Coding' in company)  # returns True if substring is found
print(company.index('Coding'))  # returns the starting index of the substring
print(company.count('Coding'))  # returns the number of occurrences of the substring

# 11 - Replace the word 'Coding' in the string 'Coding For All' to 'Python'
print(company.replace('Coding', 'Python'))

# 12 - Change Python for Everyone to Python for All using the replace method or other methods
company = 'Python for Everyone'
print(company.replace('Everyone', 'All'))

# 13 - Split the string 'Coding For All' using space as the separator (split())
print(company.split(' '))

# 14 - "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma
tech_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(tech_companies.split(', '))

# 15 - What is the character at index 0 in the string Coding For All
print(company[0])

# 16 - What is the last index of the string Coding For All
print(len(company) - 1)

# 17 - What character is at index 10 in "Coding For All" string
print(company[10])

# 18 - Create an acronym or an abbreviation for the name 'Python For Everyone'
phrase = 'Python For Everyone'
acronym = phrase.split()
acronym = f"{acronym[0][0]}{acronym[1][0]}{acronym[2][0]}"
print(acronym)

# or all in one line:
# acronym = f"{phrase.split()[0][0]}{phrase.split()[1][0]}{phrase.split()[2][0]}"

# 19 - Create an acronym or an abbreviation for the name 'Coding For All'
phrase = 'Coding For All'
acronym = phrase.split()
acronym = f"{acronym[0][0]}{acronym[1][0]}{acronym[2][0]}"
print(acronym)

# 20 - Use index to determine the position of the first occurrence of C in Coding For All
company = 'Coding For All'
print(company.index('C'))

# 21 - Use index to determine the position of the first occurrence of F in Coding For All
print(company.index('F'))

# 22 - Use rfind to determine the position of the last occurrence of l in Coding For All People
print(company.rfind('l'))

# 23 - Use index or find to find the position of the first occurrence of the word 'because' in the following sentence:
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))
print(sentence.index('because'))

# 24 - Use rindex to find the position of the last occurrence of the word 'because' in the following sentence:
print(sentence.rindex('because'))
print(sentence.rfind('because'))

# 25 - Slice out the phrase 'because because because' in the following sentence:
start = sentence.find('because')
end = start + len('because because because')
sliced_phrase = sentence[start:end]
print(sliced_phrase)

# 26 - Find the position of the first occurrence of the word 'because' in the following sentence:
print(sentence.find('because'))

# 27 - Slice out the phrase 'because because because' in the following sentence:
sentence = sentence.replace("because because because ", "")
print(sentence)

# 28 - Does 'Coding For All' start with a substring Coding?
company = 'Coding For All'
print(company.startswith('Coding'))

# 29 - Does 'Coding For All' end with a substring coding?
print(company.endswith('coding'))

# 30 - '   Coding For All      '  , remove the left and right trailing spaces in the given string.
company_with_spaces = '   Coding For All      '
print(company_with_spaces.strip())

# 31 - Which one of the following variables return True when we use the method isidentifier():
var1 = '30DaysOfPython'
var2 = 'thirty_days_of_python'
print(var1.isidentifier())  # False, because it starts with a digit
print(var2.isidentifier())  # True

# 32 - Join the list with a hash with space string
lybraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_lybraries = ' # '.join(lybraries)
print(joined_lybraries)

# 33 - Use the new line escape sequence to separate the following sentences.
print("I am enjoying this challenge.\nI just wonder what is next.")

# 34 - Use a tab escape sequence to write the following lines.
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

# 35 - Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius**2
print("The area of a circle with radius {} is {} meters square.".format(radius, area))

# 36 - Make the following using string formatting methods:
a = 8
b = 6
print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))

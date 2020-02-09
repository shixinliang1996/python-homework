# -*- coding: utf-8 -*-
"""
Python for MSSP Homework #1
"""

# Python Homework #1: Exercises with lists, loops, and functions
# Q1
# (a)
# Create a list to store the numbers
list_1a = []
# Use for loop to create numbers
for i in range(1,21):
    # Use append function to add number to the end of the list
    list_1a.append(i)

print('Question 1 (a)')
print(list_1a)
print()

# (b)
list_1b = []
for i in range(1,21):
    # Use insert function to add number to the head of the list
    list_1b.insert(0,i)

print('Question 1 (b)')
print(list_1b)
print()

# (c)
# Combine question(a)'s list and question(b)'s list
list_1c = list_1a[0:-1] + list_1b

print('Question 1 (c)')
print(list_1c)
print()

# (d)
list_1d = 10 * [4,6,3]
print('Question 1 (d)')
print(list_1d)
print()

# (e)
list_1e = 11 * [4,6,3]

# Delete the last 3
del list_1e[-1]
# Delete the last 6
del list_1e[-1]
print('Question 1 (e)')
print(list_1e)
print()



# Q2
import math

def q2(x):
    return (math.exp(x) * math.cos(x))

# Use for loop to get a list for x=3, 3.1, 3.2, … 6.
x_value = []
for i in range(30,61):
    x_value.append(i/10)

print('Question 2')
# Show x value
print("x value:")
print(x_value)

# Use map function to apply q2() function to all elements in x_value
list_2 = list(map(lambda x: q2(x), x_value))

# Show result
print("Final result:")
print(list_2)
print()



# Q3
def q3(x):
    return ((2 ** x)/x)

# Use map function to apply q3() function to 1,2,3...25. 
list_3 = list(map(lambda x: q3(x), range(1,26)))

print('Question 3')
print(list_3)
print()



# Q4
# Re-use the list from 1(a) as variable a.
a = list_1a
# Get variable a's length n.
n = len(a)

# (a)
# Get a first list of a0, a1, a2, ...an.
a_1st = a[0:n]

# Get a second list of an, an-1, an-2, ...a2, a1, a0.
a_2nd = []
for i in a_1st:
    a_2nd.insert(0,i)
   
# Calculate the first list - the second list
list_4a = []
for j in range(n):
    q4_a_value = a_1st[j] - a_2nd[j]
    list_4a.append(q4_a_value)

print('Question 4 (a)')
print(list_4a)
print()

# (b)
list_4b = []   
for i in a:
    # Use bool function to judge whether the number is even and odd.
    boolean_i = bool((i % 2) == 0)
    list_4b.append(boolean_i)

print('Question 4 (b)')
print("The Boolean list:")
print(list_4b)
print()



# Q5
# (a)
# read the file
with open('lorem.txt','r') as lorem:
    # Read the contents into a string
    text = lorem.read()
    lorem.close()

# import the re module
import re

# Define a pattern that will match:
#    string length: between 1 and 4
#    string length: between 4 and 7
#    string length: 8 or greater
# And then compile it into a pattern object.

pat = re.compile('([a-zA-Z]{1,4})|\W([a-zA-Z]{4,7})\W|\W([a-zA-Z]{8,})\W')

# Use the findall method to find all matches.
match = pat.findall(text)

# Create three lists to store the matches
one_four = []
four_seven = []
eight_longer = []

for m in match:
    # If this matched string's length is between 1 and 4
    if len(m[0]) > 0:
        one_four.append(m[0])
    # If this matched string's length is between 4 and 7
    elif len(m[1]) > 0:
        four_seven.append(m[1])
    else: # otherwise it's the other matched group (8 or greater)
        eight_longer.append(m[2])
        
print('Question 5 (a)')
print('The number of strings whose lengths are between 1 and 4: %s\n' % len(one_four))
print('The number of strings whose lengths are between 4 and 7: %s\n' % len(four_seven))
print('The number of strings whose lengths are between 8 or greater: %s\n' % len(eight_longer))


# (b)
# Define a pattern that will match:
#    All capitalized words
# And then compile it into a pattern object.
pat_b = re.compile('([A-Z][a-z]+)')

# Use the findall method to find all matches.
match_b = pat_b.findall(text)

print('Question 5 (b)')
print('The number of capitalized characters in the file: %s\n' % len(match_b))




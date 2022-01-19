
# 17 list comprehension problems in python

from select import KQ_FILTER_WRITE


fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())

print(1+1)
# Exercise 1 
uppercased_fruits = [fruit.upper() for fruit in fruits]
print(uppercased_fruits)

# Exercise 2 
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print(capitalized_fruits)

#Exercise 3
fruits_with_more_than_two_vowels = []

vowels = 'aeiouAEIOU'
for fruit in fruits:
    
    count = 0
    for char in fruit:
        if char in vowels:
            count += 1 
    
    if count > 2:
        fruits_with_more_than_two_vowels.append(fruit)
print(fruits_with_more_than_two_vowels)


#Exercise 4
fruits_with_only_two_vowels = []
for fruit in fruits: 
    count = 0 
    for char in fruit:
        if char in vowels:
            count += 1

    if count == 2:
        fruits_with_only_two_vowels.append(fruit)
print(fruits_with_only_two_vowels)

#Exercise 5

more_than_five_characters = []
for fruit in fruits:
    if len(fruit) > 5:
        more_than_five_characters.append(fruit)
print(more_than_five_characters)

#Exercise 6 

five_character = []
for fruit in fruits: 
    if len(fruit) ==  5:
        five_character.append(fruit)
print(five_character)

#Exercise 7

less_than_five_character = []
for fruit in fruits: 
    if len(fruit) ==  5:
        less_than_five_character.append(fruit)
print(less_than_five_character)

#Exercise 8 
count_character = []

for fruit in fruits: 
    count_character.append(len(fruit))

print(count_character)

#Exercise 9 

have_letter_a = []

for fruit in fruits:
    if 'a' in fruit: 
        have_letter_a.append(fruit)
print(have_letter_a)

#Exercise 10 

have_even_number =[]

for number in numbers: 
    if number % 2 == 0:
        have_even_number.append(number)
print(have_even_number)

# Exercise 11
have_odd_number =[]

for number in numbers: 
    if number % 2 == 1:
        have_odd_number.append(number)
print(have_odd_number)

#Exercise 12
have_postive_number =[]

for number in numbers: 
    if number >0 :
        have_postive_number.append(number)
print(have_postive_number)

#Exercise 13

have_negative_number =[]

for number in numbers: 
    if number <0 :
        have_negative_number.append(number)
print(have_negative_number)

#Exercise 14 

[number for number in numbers if number > 2 ]

#Exercise 15 

numbers_squared = [number ** 2 for number in numbers]
print(numbers_squared)

#Exercise 16 
odd_negative_numbers =[]

for number in numbers: 
    if number <0 and number %2 ==1:
        odd_negative_numbers.append(number)
print(odd_negative_numbers)

#Exercise 17 
numbers_plus_5 = [number +5 for number in numbers]
print(numbers_plus_5)
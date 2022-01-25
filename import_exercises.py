#1. Import and test 3 of the functions from your functions exercise file. Import each function in a different way:

# import sys
# sys.path
# sys.path.append('')

from audioop import avg
from itertools import permutations, product
from posixpath import split
import pandas
from sklearn.inspection import permutation_importance
from only_function_definition import is_vowel

user_input = input("Please enter a vowel string")
if is_vowel(user_input): 
    print(True)

else:
    print(False)


from only_function_definition import calculate_tip

tip = float(input("Please enter the tip percentage,(a number between 0 and 1)"))
bill = float(input("Please enter your bill amount"))
calculate_tip(tip,bill)



from only_function_definition import get_letter_grade

from only_function_definition import get_letter_g


num = input("Please enter your score to get your grade")
get_letter_grade(num)

#2.a How many different ways can you combine the 
# letters from "abc" with the numbers 1, 2, and 3?

from itertools import product

def number_letter(a,b):
    return list(product(a,b))

if __name__ == "__main__":
    a = ["a", "b","c"]
    b = ["1","2","3"]

    print(len(number_letter(a,b)))

#2.b How many different combinations are there of 2 letters from "abcd"?

from itertools import combinations

def two_letter_combinations(two_letter_com):
    return list(combinations(two_letter_com,2))

if __name__ == "__main__":
    two_letter_com = ["a", "b","c","d"]

    print(len(two_letter_combinations(two_letter_com)))

#How many different permutations are there of 2 letters from "abcd"?
from itertools import permutations

def two_letter_permutations(two_letter_per):
    return list(permutations(two_letter_per,2))

if __name__ == "__main__":
    two_letter_per = ["a", "b","c","d"]

    print(len(two_letter_permutations(two_letter_per)))



import json

users = json.load(open('profiles.json'))

#Total number of users

print(len(users))

#Number of active users

active = []
for user in users:
    if user['isActive'] == True:
        active.append(user)
print(len(active))

#Number of inactive users 
inactive = []
for user in users:
    if user['isActive'] == False:
        inactive.append(user)
print(len(inactive))

#Grand total of balances for all users
total_balances = []
for user in users: 
    user['balance']= user['balance'].replace("$", "")
    user['balance']= user['balance'].replace(",", "")
    user['balance']= float(user['balance'])
    total_balances.append(user['balance'])
print(sum(total_balances))


#Average balance per user
from statistics import mean
print(mean(total_balances))

#User with the lowest balance
print(min(total_balances))
#User with the highest balance
print(max(total_balances))
#Most common favorite fruit
from statistics import mode
most_favorite = []
for user in users: 
    most_favorite.append(user['favoriteFruit'])
print(max(most_favorite))


#Least most common favorite fruit
least_favorite = []
for user in users: 
    least_favorite.append(user['favoriteFruit'])
print(min(most_favorite))

#Total number of unread messages for all users

import json

users = json.load(open('profiles.json'))

unread = []
for user in users: 
    if user['greeting']:
        for letter in user['greeting']:
            if letter.isdigit():
                letter = int(letter)
                unread.append(int(letter))

print(sum(unread))

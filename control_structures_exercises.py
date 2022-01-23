#Control Structures Exercises
#1.a. conditional basics 


user_input = input('What day is today?').lower()

if user_input != 'monday':
    print("It is not Monday")
else: 
    print("Yay!! Happy Monday")


#1.b. 
user_input = input('What day is today?').lower()
if user_input in ['Saturday', 'Sunday']:
    print("Finally It's the weekend")
else: 
    print("It is a weekday")

#1.c 

hours_worked = 38
rate = 40 

if hours_worked <= 40: 
    print('Paycheck amount is', hours_worked * rate)
else: 
    overtime_hour = hours_worked - 40
    overtime_paycheck = overtime_hour * (rate*1.5)

    regular_hour = hours_worked - overtime_hour
    print('Paycheck amount is', regular_hour * rate + overtime_paycheck) 

#2.a
#Create an integer variable i with a value of 5.
i = 5

#Create a while loop that runs 
#so long as i is less than or equal to 15
while i <= 15:
    print(i)
#output the current value of i, 
#then increment i by one.
    i += 1

#Create a while loop that will count by 2's 
#starting with 0 and ending at 100. 

i = 1
while i <= 100:

    if i % 2 == 0:
        print(i)
    
    i += 1


#count backwards by 5's from 100 to -10.
i = 100
while -10 <= i <= 100: 
    print(i)
    
    i -= 5

#Create a while loop that starts at 2, 
# and displays the number squared 
# on each line while the number 
# is less than 1,000,000. Output should equal:

i = 2
while i < 1_000_000:
    print(i)

    i = i ** 2

#print to create the output shown below.

i = 100
while 5 <= i <= 100:
    print(i)

    i -= 5

#For loop 
#Write some code that prompts the user for a 
# number, then shows a multiplication table up 
# through 10 for that number.
#include <stdio.h>
proposed_num = input('Please insert a positive number')
#case this to make it a number

for n in range(1, 11):
    print(int(proposed_num), 'x', n, '=', int(proposed_num)*n)
    n += 1

#Create a for loop that uses print to 
# create the output shown below.
#1
#22
#333
#4444
#55555
#......

for i in range(10):

    print(f'{i}'* i)
    i += 1


#break and continue

#Prompt the user for
# an odd number between 1 and 50. 
#Use a loop and a break statement 
# to continue prompting the user if they enter invalid input.
while True: 
    posited_num = input('Please insert an odd number between 1 and 50')
    if posited_num.isdigit(): 
        if int(posited_num) % 2 == 1 and int(posited_num) <= 50: 
            break
posited_num = int(posited_num)
for num in range(1,50,2): 
    if num == posited_num:
        print('Yikes! skipping number:', num)
    else:
        print('Here is an odd number', num)



type(posited_num)
print('Number to skip is :', 27)

for n in range(1,51):
    if n == 27: 
        print('Yikes! Skipping number:', n)
        
    elif n % 2 == 1:
        print(f'Here is an odd number: {n}')
        


#The input function can be used to prompt for input and use 
# that input in your python code. Prompt the user to enter a 
# positive number and write a loop that counts from 0 to that
#  number. 

number = input("Please enter a posive number: ")

while int(number) < 0:
    number = input("Please enter a posive number: ")

result_str = ""
for i in range(0,int(number)+1):
    result_str += str(i)
print(result_str)



#Write a program that prompts the user for a positive integer.
#  Next write a loop that prints out the numbers from the 
# number the user entered down to 1.

number = input("Please enter a posive number: ")

while int(number) < 0:
    number = input("Please enter a posive number: ")

result_str = ""
for i in reversed(range(0,int(number)+1)):
    result_str += str(i)
print(result_str)

#Fizzbuzz

#One of the most common interview questions for 
# entry-level programmers is the FizzBuzz test. 
# Developed by Imran Ghory, the test is designed to 
# test basic looping and conditional logic skills.
#Write a program that prints the numbers from 1 to 100.
i = 1
for i in range(101):
 
#For multiples of three print "Fizz" instead of the number
    if i % 3 == 0: 
        print('Fizz')

#For the multiples of five print "Buzz".
    elif i % 5 == 0:
        print('Buzz')
#For numbers which are multiples of both three and five print "FizzBuzz".
    elif i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    else:
         print(i)
i += 1

i = 1
for i in range(101):

#For numbers which are multiples of both three and five print "FizzBuzz".
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
#For multiples of three print "Fizz" instead of the number
    elif i % 3 == 0: 
        print('Fizz')
#For the multiples of five print "Buzz".
    elif i % 5 == 0:
        print('Buzz')
    else:
         print(i)
i += 1

#Display a table of powers.
num1 = int()
while num1 != '0':
    num1 = input("What number would you like to go up to?, to exit enter 0")
    print("What number would you like to go up to?", num1)
    print("Here is your table!")
    print('number', 'squared', 'cubed')
    for num1 in range(1,int(num1)+1): 

        print(int(num1),"    ", int(num1)** 2, "     ", int(num1) ** 3)


#Convert given number grades into letter grades.
while True: 
     num = input("Please enter your score to get your grade")
     if num.isdigit():
         num = int(num)
         if num <0 or num > 100:
             print('Got to this poiont')
             continue
            break



if 88<= int(num)<=100: 
        print('A')
elif 80<= int(num)<=87:
        print('B')
elif 67<= int(num)<=79:
        print('C')
elif 60<= int(num)<=66:
        print('D')
else: 
        print('F')

#Create a list of dictionaries where each dictionary 
# represents a book that you have read. Each dictionary in 
# the list should have the keys title, author, and genre. 
# Loop through the list and print out information about each book.

#Prompt the user to enter a genre, then loop through your books 
# list and print out the titles of all the books in that genre.

books = [
    {
        "title": "The Lord of the Rings.",
        "author": "J. R. R. Tolkien",
        "genre": 'Novel'
    },
    {
        "title": "THE GREAT GATSBY",
        "author": "F. Scott Fitzgerald",
        "genre": 'fiction'
    }, 
    {
        "title": "Weapons of Math Destruction",
        "author": "Cathy O'Neil",
        "genre": 'Non-fiction'
    }
    ]   
user_input = input("What kind of genre do you prefer?")
result = []
for book in books:
    if book['genre'] == user_input:
        result.append(book['title'])
if result ==[]:
    print("no books abailable")
else:
    print(f'{user_input}')

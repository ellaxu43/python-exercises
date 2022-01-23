#Define a function named is_two. It should accept one input and return 
# True if the passed input is either the number or the string 2, 
# False otherwise.


def is_two(x):

    # step 1: convert input value to number
    x = int(x)
    
    # step 2: if condition, see if x equals to 2 or not
    if x == 2:
        return True 

    else:
        return False
is_two(2)

#step 1, build input
x = input("Please enter a number")
#step 2, set x is int
x = int(x)
#step 3, define the function
def is_two(x):
    if x == 2:
        return True 
#step 4, set else
    else:
        return False
#step 5, print (x)
is_two(x)


#Step 1, def the function, transfter x to int and set the condition to 2
def is_two(x):
    x = int(x)
    return x == 2
#step 2, set input, and if input matches the condition, then true. 
user_input = input("please enter a number")
if is_two(user_input):
    print(True)
else:
    print(False)


#2. Define a function named is_vowel. It should return True 
# if the passed string is a vowel, False otherwise.

def is_vowel(y): 
    #1. set up vowel 
    vowel = 'aeiou'
    #2. see if the string is vowel
    if y.lower() in vowel:
        return True

    else:
        return False
is_vowel('E')


#1. set up vowel
y = input("Please enter a vowel string")
vowel = 'aeiou'
def is_vowel(y): 
    #2. see if the string is vowel
    if type(y) == str:
        result = y.lower() in ['a','e','i','o','u']
        return result

    else:
        return False


#3. Define a function named is_consonant. 
# It should return True if the passed string is a consonant, 
# False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(some_string):
    if type(some_string) == str:
        only_letters = some_string.isalpha()
        return only_letters and not vowel
    return False



def is_consonant(z): 
    #1. define vowel
    vowel = 'aerou'
    #2. see if string in conconant
    if z.lower() not in vowel:
        return True

    else:
        return False 

is_consonant('W')


def is_consonant(z): 
    #1. define vowel
    vowel = 'aeiou'
    #2. set up the condition, if not in vowel then will return true
    return z.lower() not in vowel
#3. user_input 
user_input = input("Please enter a cosonant")
#4. if the user input matches the condition that we set for is_consonant then true 
if is_consonant(user_input): 
    print(True)
#5. else print false
else:
    print(False)

#4.Define a function that accepts a string that is a word. 
# The function should capitalize the first letter of the 
# word if the word starts with a consonant.
#step 1, first define the function,if first letter not in vowel, return true 
def capitalize_word_start_with_consonant(c):
    vowel = 'aeiou'
    return c[0].lower() not in vowel
#step 2, input
user_input = input("Please enter a word")
#step 3, if this condition is met, print the first letter with capitalized. 
if capitalize_word_start_with_consonant(str(user_input)):
    print(str(user_input).capitalize())
#step 4, else print others. 
else:
    print("The word you entered isn't start with consonant")

#5. Define a function named calculate_tip. It should accept a tip percentage 
# (a number between 0 and 1) and the bill total, and return the amount to tip.

#step 1. def the function, return the total amount 
def calculate_tip(tip,bill): 
    if type(bill) != float:
        return False
    if tip <0 or tip>1:
        return 'the tip percentage must be between 0 and 1'
    return tip * bill + bill
#step 2, input
tip = float(input("Please enter the tip percentage,(a number between 0 and 1)"))
bill = float(input("Please enter your bill amount"))
#step 3. ask to print the whole function. 
calculate_tip(tip,bill)

#6. Define a function named apply_discount. It should accept a original price,
# and a discount percentage, and return the price after the discount is applied.
def apply_discount(original_price, discount_percent):
    return original_price - original_price * discount_percent/100
original_price = float(input("The original price is"))
discount_percent = float(input("The discount percent is such like 20% just enter 20"))
apply_discount(original_price, discount_percent)

#7.Define a function named handle_commas. It should accept a string 
#that is a number that contains commas in it as input, and return a number as output.

#step 1 def the commas function to return the result without commas 
def handle_commas(commas):
    return str(commas).replace(',',"")
#step 2, input
commas = input("please enter a number with commas")
#step 3, bring input values back to the function. 
handle_commas(commas)

#Define a function named get_letter_grade. 
# It should accept a number and return the letter grade 
# associated with that number (A-F).
   
def get_letter_grade(num):
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
num = input("Please enter your score to get your grade")
get_letter_grade(num)

#9. Define a function named remove_vowels that accepts a 
#string and returns a string with all the vowels removed.
def remove_vowels(text):
    for i in 'aeiouAEIOU':
        text = text.replace(i,"")
    return text
#step 2, input
text = input("please enter a word")
#step 3, bring input values back to the function. 
remove_vowels(text)

#10. anything that is not a valid python identifier should be removed
#leading and trailing whitespace should be removed
#everything should be lowercase
#spaces should be replaced with underscores

def normalize_name(string):
    output = ''
    string = string.lower()
    for character in string:
        if character.isidentifier() or character == ' ':
            output += character
    output = output.strip()
    output = output.replace(' ', '_')
    return output

normalize_name("Hello ")

#11.Write a function named cumulative_sum that accepts a list of numbers 
#and returns a list that is the cumulative sum of the numbers in the list.

#step 1, define the function list 
def cumulative_sum(lists):

    cu_list = [] # create a blank list
    length = len(lists) # get the length of the list 
    cu_list = [sum(lists[0:x:1]) for x in range(0, length+1)] #
    return cu_list[1:]

cumulative_sum([1, 1, 1])



def new_list(xx):
    newlist=[]
    newlist=[sum(list[0:4:1]) in range(0,4)]

    return newlist
new_list([1,1,1])


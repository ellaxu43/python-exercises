#Exercises Part 1
99.9
"False"
'1' + 2
6 % 4
type(6 % 4)
type(type(6 % 4))
'3 + 4 is ' + 3 + 4
0 < 0
'False' == False
True == 'True'
True or "42"
5 >= -5
6 % 5
5 < 4 and 1 == 1
'codeup' == 'codeup' and 'codeup' == 'Codeup'
4 >= 0 and 1 !== '1'
6 % 3 == 0
5 % 2 != 0
[1] + 2
[1] + [2]
[1] * 2
[1] * [2]
[] + [] == []
{} + {}
#Exercises Part 2
#movies for your kids:
lit_mer = 3
bro_bear = 5
hercules = 1

rentallist = [lit_mer, bro_bear, hercules]
price = sum(rentallist) * 3 

print(price)

#receive payment
amazon = 380
google = 400
facebook = 350

amazon_work_hours = 4
google_work_hours = 6
facebook_work_hours = 10

paycheck = amazon* amazon_work_hours + google*google_work_hours + facebook* facebook_work_hours
print(paycheck)
print(f'total amount is {paycheck}')

# student question

class_not_full = True

no_conflict = True 

enrolled = class_not_full and no_conflict 

print(f'Can student enroll? \n {enrolled}')

# product offer question 
premium_member = True
offer_not_expired = True 
qualifying_items = 3 
discount_applied = offer_not_expired and (qualifying_items > 2 or premium_member)


#username and password question 
username= 'codeup'
password = 'password'

if len(username) <= 20 and len(password) >= 5 and username != password:
    print('username and password registered')
else: 
    'the password must be at least 5 characters, the username must be no more than 20 characters, the password must not be the same as the username'









vowel = 'aeiou'
def is_vowel(y): 
    return y.lower() in vowel




def calculate_tip(tip,bill): 
    if type(bill) != float:
        return False
    if tip <0 or tip>1:
        return 'the tip percentage must be between 0 and 1'
    return tip * bill + bill




def get_letter_grade(num):
    if 88<= int(num) <=100: 
        return 'A'
    elif 80<= int(num) <=87:
        return'B'
    elif 67<= int(num) <=79:
        return 'C'
    elif 60<= int(num) <=66:
        return 'D'
    else: 
        return 'F'

def get_letter_g(num):
    if 88<= num <=100: 
        return 'A'

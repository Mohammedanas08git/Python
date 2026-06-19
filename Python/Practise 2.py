def rev(num):
    rev=0
    while num>0:
        digit=num%10     # Take last digit of an number .
        rev=rev*10+digit # Build revrese of an number .
        num=num//10      # Remove last digit of an number .
    return rev
print(rev(123))    

def digits(num):
    return num
    
print(len(digits("1234")))    

def count_a(vowel,consonant):
    vowel="aeiouAEIOU"
    

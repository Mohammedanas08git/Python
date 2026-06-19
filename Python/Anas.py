#def anas():
#    print("Hello Python")
#anas()

#def name():
#    n=input("Enter your name")
#    print("Welcome",n)
#name()   

#def sum(a,b):
#    sum=a+b
#    print(sum)
#    return sum
#sum(5,6)

#def check(a):
#   if(a%2==0):
#        print("EVEN VALUE")
#   else:
#        print("ODD VALUE")
#check(10)  

#def num(a,b,c):
#    if(a>b):
#       print(a)
#    elif(b>c):
#        print(b)
#    elif(c>a):
#        print(c)
#num(5,90,9)    

#def sqr(a):
#    sqr=a*a
#    print("Square=",sqr)
#sqr(8)    

#def num(n):
#    fact=1
#    for i in range(1,n+1):
#        fact=fact*i
#    print("Factorial :",fact)
#num(6)


#def sum_of_list(numbers):
#   total = 0
#    for num in numbers:
#        total += num
#    return total
#
#print(sum_of_list([1, 2, 3, 4, 5]))

#def vowel(text):
#    c=0
#    vowel="aeiouAEIOU"
#    for char in text:
#        if char in vowel:
#            c=c+1
#    return c
#print(vowel("Mohammed Anas"))

#def prime(n):
#    if n<=1:
#        print("not prime")
#    for i in range(2,n):
#        if(n%i==0):
#            print("not prime")
#    print("prime") 
#prime(4)           

def div(divisor,divident):
    quotient=divisor//divident
    remainder=divisor%divident
    print("remainder :",remainder)
    print("qoutient",quotient)
div(476,8) 

def reversestring(text):
    rev=""
    for char in text:
        rev=char+rev
    print(rev)    
reversestring("THOR")

def palindrome(num):
    original=sum
    rev=0
    if(rev==original):
        print("Number is Palindrome")
    #else:
     #   print("Number is not Palindrome")              
palindrome(12321)  

def converter(fahrenheit):
    celsius=(fahrenheit-32)*5/9
    print(fahrenheit,"Fahrenheit=",celsius,"Celsius")
converter(2)

def grade(marks):
    if (marks>=90):
        print("Grade A")
    elif(90>marks>=70):
        print("Grade B")
    elif(70>marks>=50):
        print("Grade C")
    else:
        print("fail You didn't reach limit :")
grade(98)                    


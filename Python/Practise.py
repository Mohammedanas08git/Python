#def fun(num):
   # if num>=1:
  #      print("Number is positive .")
   # elif num<=-1:
   #     print("Number is negative .")
  #  elif num==0:
 #       print("number is zero .")
#fun(9)
#fun(-9)
#fun(0)    

#def fun(a,b):
 #   if a>b:
 #       print("greater number =",a)
 #   elif b>a:
 #   elif(a>=b and b>=a):
 #       print("anyone number=",a or b)
#fun(9,3)
#fun(5,9)
#fun(12,12)
#
#def sum(n):
#   total=0
#   for i in range(1,n+1):
#        total=total+i
#   return total    
#print(sum(5))   

#def count_a(text):
#    count_a=text.count("a")
#    print(count_a) 
#count_a("anas")

#def fun(num):
#    if(num%5==0):
#        return True
#    return False
#print(fun(11))

def count_vow(text):
    vowel="aeiouAEIOU"
    v=0
    c=0
    for char in text:
        if(v==vowel):
            return v
        return c
print(count_vow("anas"))    
     
    
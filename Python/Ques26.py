# Wap to search for a number x in this tuple using for loop ??
#            (1,4,9,16,25,36,49,64,81,100)

num=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter an x:"))
i=0
for el in num:
    if(el==x):
        print("number found at i",i)
    i=i+1    
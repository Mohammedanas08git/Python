while True:
    print("<<<------------SIMPLE CALCULATOR-------------->>>")
    print("1-Addition")
    print("2-Substraction")
    print("3-Multiplication")
    print("4-Division")
    print("5-Exit")

    choice=int(input("enter user choice"))
    #a=int(input("Enter first number"))
    #b=int(input("Enter Second number"))
    if(choice==1):
        a=float(input("Enter first number"))
        b=float(input("Enter Second number"))
        result=a+b
        print("Addition=",result)
    elif(choice==2):
        a=float(input("Enter first number"))
        b=float(input("Enter Second number"))
        result=a-b
        print("Substraction=",result)
    elif(choice==3):
        a=float(input("Enter first number"))
        b=float(input("Enter Second number"))  
        result=a*b
        print("Multiplication=",result)
    elif(choice==4):
        a=float(input("Enter first number"))
        b=float(input("Enter Second number"))
        if(b==0):
            print("Error calculator can't divide by zero")
        else:
            result=a/b
            print("Division=",result)
    elif(choice==5):
        print("Exit")
        break   
    else:
        print("Invalid Choice please try again later :")
        
        

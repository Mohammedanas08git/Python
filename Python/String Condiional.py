# Conditional Statement
#light=(input("enter the colour of light"))
#if(light=="Green"):
#    print("Veichles can move")
#elif(light=="yellow"):
#    print("wait for red light")
#elif(light=="red"):
#    print("veichles can't move")  
#else:
#    print("light is broken")

# Nesting -->
age=int(input("enter an age"))
if(age>=18):
    if(age>=80):
        print("Cannot drive")
    else:
        print("Can drive")
else:
    print("Cannot drive")            
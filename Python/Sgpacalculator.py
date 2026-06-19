Physics=int(input("Enter your Physics 1st term Marks :"))
Physics2=int(input("Enter your Physics 2nd term Marks :"))
Assignment1=int(input("Enter your Physics assignment Marks :"))  

DDAI=int(input("Enter your DDAI 1st term Marks :"))
DDAI2=int(input("Enter your DDAI 2nd term Marks :"))
Assignment2=int(input("Enter your DDAI assignment Marks :"))

CPLT=int(input("Enter your CPLT 1st term Marks :"))
CPLT2=int(input("Enter your CPLT 2nd term Marks :"))
Assignment3=int(input("Enter your CPLT assignment Marks :"))

Maths=int(input("Enter your Maths 1st term marks :"))
Maths2=int(input("Enter your Maths 2nd term marks :"))
Assignment4=int(input("Enter your Maths assignment Marks :"))

CS=int(input("Enter your CS 1st term Marks :"))
CS2=int(input("Enter your CS 2nd term Marks :"))
Assignment5=int(input("Enter your CS assignment Marks :"))

physicsHalfsem=((Physics)+(Physics2))*0.375+Assignment1
ddaiHalfsem=((DDAI)+(DDAI2))*0.375+Assignment2
cpltHalfsem=((CPLT)+(CPLT2))*0.375+Assignment3
mathsHalfsem=((Maths)+(Maths2))*0.375+Assignment4
csHalfsem=((CS)+(CS2))*0.375+Assignment5

EndTermPhysics=int(input("Enter your Physics End term marks"))
EndTermDDAI=int(input("Enter your DDAI End term marks"))
EndTermCPLT=int(input("Enter your CPLT End term marks"))
EndTermMaths=int(input("Enter your Maths End term marks"))
EndTermCS=int(input("Enter your CS End term marks"))
cpltprac=int(input("Enter your cplt Practical marks :"))
ddaiprac=int(input("Enter your ddai practical marks :"))
physicsprac=int(input("Enter your physics practical marks :"))
digitalprac=int(input("Enter your digital literacy practical marks :"))
csprac=int(input("Enter your cs practical marks :"))

physicsend=physicsHalfsem+((EndTermPhysics)/2)
ddaiend=ddaiHalfsem+((EndTermDDAI)/2)
cpltend=cpltHalfsem+((EndTermCPLT)/2)
mathsend=mathsHalfsem+((EndTermMaths)/2)
csend=csHalfsem+((EndTermCS)/2)

percentage=((physicsend+ddaiend+cpltend+mathsend+csend+physicsprac+cpltprac+ddaiprac+csprac
+digitalprac)/1000)*100
SGPA=(percentage+7.5)/10

print("------------CONGRATS YOUR REPORT CARD-------------")
print("Physics :",physicsend)
print("DDAI :",ddaiend)
print("CPLT :",cpltend)
print("Maths :",mathsend)
print("CS :",csend)
print("CPLT Practical :",cpltprac)
print("Physics Practical :",physicsprac)
print("DDAI Practical :",ddaiprac)
print("CS Practical :",csprac)
print("Digital Practical :",digitalprac)
print("Percentage =",percentage)
print("SGPA =",SGPA)
print("------------GOOD JOB FOR YOUR ACHIEVEMENT------------")



    

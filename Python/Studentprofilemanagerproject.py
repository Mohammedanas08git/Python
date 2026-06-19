name=input("Enter student name")
age=int(input("Enter student age"))
hometown=input("Enter student hometown ")
branch=input("Enter student branch")
semester=int(input("Enter student semester"))
college=input("Enter college name")
#dict={name,age,hometown,branch,semester,college}

skills=[]
skills1=input("Enter skill 1")
skills2=input("Enter skill 2")
skills3=input("Enter skill 3")
skills4=input("Enter skill 4")
skills5=input("Enter skill 5")
skills=[skills1,skills2,skills3,skills4,skills5]

intrest=set()
intrest1=input("Enter your intrest")
intrest2=input("Enter your intrest2")
intrest3=input("Enter your intrest 3")
intrest.add(intrest1)
intrest.add(intrest2)
intrest.add(intrest3)

print("<<--------------STUDENT DETAILS--------------->>")
print("Name:",name)
print("Age:",age)
print("Hometown:",hometown)
print("Branch:",branch)
print("Semester:",semester)
print("College:",college)
print(skills)
print(intrest)

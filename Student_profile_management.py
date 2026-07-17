class Student:
    def __init__(self,fullname,m1,m2,m3):
        self.name=fullname
        self.phy=m1
        self.chem=m2
        self.math=m3
    def average(self):
       sum=self.phy+self.chem+self.math
       avg=sum/3
       return avg
    def result(self):
        avg=self.average()
        if avg >= 40 :
            return "PASS :"
        else:
            return "FAIL :"
    def display(self):
        print("Name = ",self.name)
        print("Physics = ",self.phy)
        print("Chemistry = ",self.chem)
        print("Maths = ",self.math)
        print("Average = ",self.average())
        print("Result = ",self.result())

students=[]
def add_students():
    name=input("Enter your name :")
    phy=int(input("Enter your physics mark :"))
    chem=int(input("Enter your chem mark :"))
    maths=int(input("Enter your maths mark :"))
    s1=Student(name,phy,chem,maths)
    students.append(s1)
    print("Student Added Successfully :")

def display_students():
    for student in students:
        student.display()
    if not students:
        print("No Student Found :")
        return    
def search_students():
    found = False
    student=input("Enter the name you want to search :")
    for name in students:
        if name.name==student:
            name.display()
            found=True
            break
    if found==False:
        print("Student Not Found :")            

def delete_students():
    student=input("Enter the name of Student you want to delete : ")
    found = False
    for name in students:
        if name.name==student:
            students.remove(name)
            print("Student Deleted Successfully :")
            found=True
            break
    if found == False:
        print("No Student found to delete")    

def topper():
    topper =students[0]
    for student in students:
        if student.average() >= topper.average() :
            topper=student
    topper.display()

while True:
    print("===========STUDENT MANAGEMENT PROFILE =============")
    print("1 . Add Student ")
    print("2 . Display Students ")
    print("3 . Search Students ")
    print("4 . Delete Student")
    print("5 . Find Topper ")
    print("6 . Exit ")
    print("====================================================")

    choice = int(input("Enter your Choice :"))
    if choice == 1:
        add_students()
    elif choice == 2:
        display_students()
    elif choice == 3:
        search_students()
    elif choice == 4:
        delete_students()
    elif choice == 5:
        topper()
    elif choice == 6:
        break
    else:
        print("Invalid Choice :")                
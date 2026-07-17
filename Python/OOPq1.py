#create student names and marks of 3 subjects as arguments in constructor
#then create a method to print the average?????

"""class Student:
    def __init__(self,fullname,marks):
        self.name=fullname
        self.marks=marks
    def average(self):
          print("AVERAGE = ",(self.marks+self.marks+self.marks)/3)  
s1=Student("KARAN",95,89,69)
print(s1.name)
print("physics = ",s1.marks)
print("Chemistry = ",s1.marks)
print("Maths = ",s1.marks)
s1.average()
"""        
"""class Student:
     def __init__(self,fullname,age):
          self.name=fullname
          self.age=age
s1=Student("ANAS",19)
s2=Student("RAHUL",20)
print(s1.name,s1.age)
print(s2.name,s2.age)
"""
class Student :
    def __init__(self,fullname,m1,m2,m3):
        self.name=fullname
        self.physics=m1
        self.chemistry=m2
        self.maths=m3
    """def average(self):
        return (self.physics+self.chemistry+self.maths)/3
        #print("Average = ",average)
    #def result(self):
        avg=self.average()
        if avg>=40:
            print("Result : PASS")
        else:
            print("Result : FAIL")
    """         
    def delete(self):
        student=(input("Enter the name you want to delete :"))
        students=[s1,s2]
        for name in students:
            if name.name==student:
                students.remove(name)
                print("Deleted ")
                break
            else:
                print("NOT FOUND")
        for name in students:
            print(name.name)                           
s1=Student("Anas",8,8,98)
s2=Student("AMIR",89,38,27)
print(s1.name)
print(s2.name)
s1.delete()
s2.delete()            

          
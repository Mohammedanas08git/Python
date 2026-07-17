# 1 init fun ---> also known as constructor .
# all class have init fun which is always executed when the object is being initiated .
# def __init__(self,fullname)

"""class student :
    def __init__(self,fullname):
        self.name=fullname
s1=student("KARAN")
s2=student("VIRAN")
s3=student("MIRAN")
print(s1.name)
print(s2.name)
print(s3.name)
"""        
        
#class and instance attribute ---->        
class student :
    def __init__(self,fullname,marks):
        self.name=fullname
        self.marks=marks
    def hello(self):
        print("HELLO :")
    def get_marks(self):
        print(s1.marks)        
s1=student("KARAN",65)
s1.hello()
print(s1.name)
s1.get_marks()
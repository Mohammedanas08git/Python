#Dictionary==> Dictionary are used to store the data value in key:value pairs.
# They are unorderable , they are mutable(changeable) and don't allow duplicate key.
#dict={
#    "name": "Mohammed Anas",
#    "Sgpa": 8.0,
#    "Marks": [90,95,79]
#}
#print(dict)
#print(type(dict))
#dict["name"]="Mohammed Anas Chhipa"
#dict["Sgpa"]=9.0
#print(dict)

#Nested Dictionary===>
#Student={
#    "Name":"Mohammed Anas",
#    "Class":"XII-A",
#    "Roll Number":9520,
#   "Marks":{
#        "Chemistry":49,
#        "Maths":78,
#        "English":89,
#        "Computer Science":98,
#    }    
#}   
#print(Student)
#print(Student["Marks"]["Computer Science"])

# Dictionary Methods===>

Student={
    "Name":"Mohammed Anas",
    "Class":"XII-A",
    "Roll Number":9520,
   "Marks":{
        "Chemistry":49,
        "Maths":78,
        "English":89,
        "Computer Science":98,
    }    
}
#print(Student.keys())  ==> return all keys in dictionary .
#print(len(Student))

#print(Student.values()) #==> return all values in dictionary .
#print(len(Student))

#print(Student.items()) #===> returns all (key,values) in a tuple .

#print(Student.get("Name")) ==> rettun the key according to value .

#Student.update({"City":"Chittorgarh"})
#print(Student)  ==> insert a specified items to dictionary .
